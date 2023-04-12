---
title: Parsing 575k military records with Python
description: The Canadian government made the records of the 660 000 Canadians who served in the First World War available as an open dataset. I decided to take a look at it.
date_created: 2016-11-15
---

During the First World War, over 600 thousand Canadians were enlisted in the Canadian Expeditionary Force. My goal is to link various data sets about the Canadians who fought in the First World War and find innovative ways to visualize and analyze the resulting database.

I wish to allow people to pull the military records of individual enlistees, to find individual soldiers involved in a given battle or campaign, and to follow a regiment's position on the battlefield throughout the war. This requires an unprecedented data processing effort, but the increasing availability of linked and open data makes this possible.

The Canadian government made [the 575 thousand military records](http://open.canada.ca/data/en/dataset/6a6e6a79-9e2a-48cc-99ec-163da26d15e9) of Canadian Expeditionary Force enlistees available as an open dataset, and I decided to use it as my starting point.

Although this data set contains all the basic information I was looking for, cracking it open was no small task. The gigantic file could not be parsed all at once, let alone be opened by a conventional text editor, and the data was formatted in a way that would make Jon Bosak cry. Here's how I tamed this 709MB beast.

Playing with large data sets is a nice change from web development, and perhaps my work will prove useful to historians who don't have the resources to work with individual datasets.

## Divide and conquer

As suggested by another user of the dataset, I reduced the file to half its size by converting from UTF-16 to UTF-8. As a side effect, that made it compatible with `sed` and other Linux utilities.

```
iconv -f utf-16 -t utf-8 records.xml > tmp/utf8-records.xml

```

Using Python's XML library, I was able to effortlessly parse through the file and extract records, but the memory usage quickly spiraled out of control.

This was in part caused by the asinine structure of the document. All the nodes were directly under the same root node, and different attributes for a given record were only held together by their order in the document.

```
<CEF_Data>
 <PersonID>1</PersonID>
 <DocumentNumber>000000001</DocumentNumber>
 <Surname>AABEL</Surname>
 <GivenName>NEILS</GivenName>
 <BirthDateList>...</BirthDateList>
 <RegimentalNumberList>...</RegimentalNumberList>
 <Reference>...</Reference>
 <DigitizeList>...</DigitizeList>

 <PersonID>2</PersonID>
 <DocumentNumber>000000002</DocumentNumber>
 <!-- And so on... -->

```

This made it impossible to clear the parsed XML nodes from memory. Instead of tweaking the XML parser and waste a day on a potentially fruitless pursuit, I opted to split the giant file into a few dozen more manageable files. This also opened the door to parallelization, but it was not really a concern given the small size of the dataset.

This seemingly simple operation was met with unexpected problems with Apple's different implementation of `sed` and `split`. Regardless, here is the complete preparation script with comments added ([GitHub mirror](https://github.com/nicbou/canadians-at-war/blob/master/canadian-expeditionary-force-members/fetch-data.sh)):

```
#!/bin/bash 
set -x

wget http://www.collectionscanada.gc.ca/obj/900/f11/001042_20141124.xml records.xml
mkdir tmp

# Convert the file to from UTF-16 UTF-8
iconv -f utf-16 -t utf-8 records.xml > tmp/utf8-records.xml
cd tmp

# Remove root node
# Note: OS X requires a backup file name with -i, hence the empty string
# http://stackoverflow.com/questions/7573368/in-place-edits-with-sed-on-os-x
sed -i '' 's/^\<CEF_Data\>//' utf8-records.xml
sed -i '' 's/\<\/CEF_Data\>$//' utf8-records.xml

# Add line breaks after each record (the original file is on one line)
# Note: OS X doesn't support replacing with \n, so we use real line breaks
# http://superuser.com/questions/307165/newlines-in-sed-on-mac-os-x/582558
sed -i '' 's/\<\/PersonID\>/\<\/PersonID\>\
/g' utf8-records.xml

# Split the file in series of 50000 records. These take ~500mb of RAM each to parse
# Note: OS X doesn't support numeric suffices for split. It's a GNU split feature.
mkdir split-records
split -a4 -l50000 utf8-records.xml split-records/records

# Add the root node back
cd split-records
for file in *; do
 echo -n "<CEF_Data>" > /tmp/tmpfile.$
 cat "$file" >> /tmp/tmpfile.$
 echo "</CEF_Data>" >> /tmp/tmpfile.$;
 mv /tmp/tmpfile.$ "$file"
done

```

The result was a dozen files with 50 000 neatly arranged record that were ready to be parsed.

## From XML to SQL

The end goal was to make this data usable in more complex contexts. In order to make this large dataset queryable, I piped the files generated above to a short Python script that saved the records to a PostgreSQL database.

Parsing the data was a fairly uneventful process, but there were a few gotchas along the way. For instance, dates were formatted in arbitrary formats, making it impossible to properly parse them. This will be the topic of a separate post.

Since every record follows the exact same format, the use of a slow, bulky XML parser was not necessary. However, at 5000 records per second for a one-time operation, we're done in less time than it takes to boil a kettle, so rolling my own parser was pointless.

Here is the script I wrote to create database entries. It takes the XML file path as its first argument. ([GitHub mirror](https://github.com/nicbou/canadians-at-war/blob/master/canadian-expeditionary-force-members/parse-data.py))

```
import xml.etree.ElementTree as etree
import sys
from datetime import datetime, timedelta
import psycopg2

def save_person(person):
 format = {
 'id': person['id'],
 'reference_en': person.get('reference_en'),
 'reference_fr': person.get('reference_fr'),
 'surname': person.get('surname'),
 'given_name': person.get('given_name'),
 'birth_date1': person['birthdates'][0] if len(person['birthdates']) > 0 else None,
 'birth_date2': person['birthdates'][1] if len(person['birthdates']) > 1 else None,
 'regiment_nr1': person['regimental_numbers'][0] if len(person['regimental_numbers']) > 0 else None,
 'regiment_nr2': person['regimental_numbers'][1] if len(person['regimental_numbers']) > 1 else None,
 'regiment_nr3': person['regimental_numbers'][2] if len(person['regimental_numbers']) > 2 else None,
 'image1': person['images'][0] if len(person['images']) > 0 else None,
 'image2': person['images'][1] if len(person['images']) > 1 else None,
 'image3': person['images'][2] if len(person['images']) > 2 else None,
 'document_number': person.get('document_number'),
 }
 cursor.execute(
 """
 INSERT INTO people (
 id, birth_date1, regiment_nr1, regiment_nr2, regiment_nr3, reference_en, reference_fr, document_number, given_name, surname, image1, image2, image3
 )
 VALUES (
 %(id)s, %(birth_date1)s, %(regiment_nr1)s, %(regiment_nr2)s, %(regiment_nr3)s, %(reference_en)s, %(reference_fr)s, %(document_number)s, %(given_name)s, %(surname)s, %(image1)s, %(image2)s, %(image3)s
 )
 """,
 format
 )

def print_progress(start, records_parsed):
 if records_parsed % 250 == 0:
 elapsed = datetime.now() - start
 formatted_elapsed = str(elapsed).split('.')[0]
 output = "{0}, {1} records parsed".format(formatted_elapsed, records_parsed)
 print(output)
 sys.stdout.write("\033[F")
 pass

# This file is a flat list of XML elements under a <CEF_Data> node. Fortunately, they're ordered.
# PersonId is the first element for each record.
person = {}
root_elem = None
ignored_tags = ('CEF_Data', 'Reference', 'RegimentalNumberList', 'BirthDateList', 'DigitizeList')
filename = sys.argv[1]
start = datetime.now()
records_parsed = 0

conn = psycopg2.connect("dbname='canadiansatwar' user='nicolas' host='localhost' password=''")
cursor = conn.cursor()
cursor.execute('BEGIN')

for event, elem in etree.iterparse(filename, events=('end',)):
 if elem.tag not in ignored_tags:
 if elem.tag == 'RegimentalNumber':
 person['regimental_numbers'].append(elem.text)
 elif elem.tag == 'BirthDate':
 person['birthdates'].append(elem.text)
 elif elem.tag == 'ReferenceEn':
 person['reference_en'] = elem.text
 elif elem.tag == 'ReferenceFr':
 person['reference_fr'] = elem.text
 elif elem.tag == 'DocumentNumber':
 person['document_number'] = elem.text
 elif elem.tag == 'Surname':
 person['surname'] = elem.text
 elif elem.tag == 'GivenName':
 person['given_name'] = elem.text
 elif elem.tag == 'Image':
 person['images'].append(elem.text)
 elif elem.tag == 'PersonID': # New person
 person = {
 'birthdates': [],
 'regimental_numbers': [],
 'images': [],
 }
 person['id'] = elem.text
 else:
 print('unexpected tag: {0}'.format(elem))
 elif elem.tag == 'DigitizeList': # Last tag for each person. This means we're done with that person
 records_parsed += 1
 print_progress(start, records_parsed)
 save_person(person)

cursor.execute('COMMIT')

```

To move all the records to the database, I added the following lines to the bash script that fetches, cleans and splits the original data:

```
for file in *; do
 python ../../parser-members.py "$file"
done

```

## Invalid data

While importing data into the database, I realized that the dates were not normalized. Some dates followed the `dd/mm/yyyy` format while others followed the `mm/dd/yyyy`, `yyyy-mm-dd`, `yyyy` and `M yyyy` formats. There were also values such as "unknown", "??", "DD/MM/YYYY", "81/05/1894", "2465019" and so on. I saved them as-is to the database so I can work on that issue later.

Out of the first 50 000 records, 997 had invalid dates, and an untold number had valid-looking dates that might have been parsed with the wrong format.

Despite allowing multiple birth dates, not a single record had more than one. 9 116 records had no birth date at all. This might be a transcription error, as the scans of the original papers showed legible birth dates on some of them.

Only two of the first 50 000 had missing name information, and neither had scans of the original documents. 1931 records did not have a regimental number, but all regimental numbers *seemed* valid according to [this guide](http://www.collectionscanada.gc.ca/obj/001042/f2/Regimental_Number_List_of_the_Canadian_Expeditionary_Force.pdf).

Another oddity was the number of records: 575 535, while the official number of enlistees is 619 646.

## Conclusion

This data set was an excellent start for my project, as it contained a complete and *mostly* reliable list of Canadian Expeditionary Force enlisted personnel to which I could link more data in the future. While I'm disappointed at the lack of standardization for dates, I still consider it an excellent starting point.

The next list I will look at is the Commonwealth War Graves Commission's [list of registered dead](http://www.cwgc.org/find-war-dead.aspx) for the First World War. It contains the names of over 66 000 Canadian war dead along with age, rank, date of death and regiment. Fortunately, these are saved in a large CSV file, and should be fairly easy to parse.

You can find the code used to fetch and parse the Canadian Expeditionary Force dataset [on GitHub](https://github.com/nicbou/canadians-at-war/tree/master/canadian-expeditionary-force-members).

This article is part of a series on Canadians at war, a project that aims to link and visualize open data about Canadians in the First World War. You can find the next article in the series [here](/blog/the-commonwealth-war-graves-commission-data-set "Parsing 65 000 war grave records with Python").

