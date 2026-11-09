---
title: Parsing 65 000 war grave records with Python
description: This week, we take a look at the 65 000 records of the Commonwealth War Graves Commission's data set.
date_created: 2016-11-15
---

The second data set I chose to import in my project is the Commonwealth War Grave Commission's [65 000 grave listings](http://www.cwgc.org/find-war-dead.aspx).

Compared to [the previous data set](/blog/parsing-575k-military-records-with-python), it a walk in the park: a large, properly formatted CSV file containing accurate, normalized information. If only it was always this simple!

```python
ordered_column_names = ( # Ordered as they appear in the CSV file
    'surname',
    'given_name',
    'initials',
    'age_text',
    ...
)
column_count = len(ordered_column_names)

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
        war_grave = dict(zip(ordered_column_names, row))
```

The resulting data only had one minor problem: the servicenumberexport column values were quoted with single quotes which needed to be removed.

```python
with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
        war_grave = dict(zip(ordered_column_names, row))

    if len(war_grave['servicenumberexport']) and war_grave['servicenumberexport'][0] == "'":
        war_grave['servicenumberexport'] = war_grave['servicenumberexport'][1:-1]
```

## Refining the data

After getting the data into the database, I was pleased to find that the date of death was normalized and valid. I changed the schema and refined the script to save date objects.

```python
with open(filename, 'r') as csvfile:
    # ...
    for row in csv_reader:
        # ...
        for field in ('date_of_death1', 'date_of_death2'):
            if len(war_grave[field]):
                raw_date = war_grave[field]
                war_grave[field] = datetime(int(raw_date[6:10]), int(raw_date[3:5]), int(raw_date[0:2]))
            else:
                war_grave[field] = None
```

Likewise, the age column was always numeric or empty, so I converted it to a `SMALLINT` field:

```python
war_grave['age'] = int(war_grave['age']) if len(war_grave['age']) else None
```

## Caveats

Perhaps the most important thing to note is the significance of the date of death. Since these records are about *war graves* and not military casualties, not every enlistee in the records died during the war, or as a result of military activities. As a typical example, Sgt. Nassau Briggs died in 1921 from sickness, and was subsequently buried in a military cemetery.

## Quick facts

I have not yet connected this data set with the previously parsed Canadian Expeditionary Force dataset, but without doing any fancy querying, we can already extract a few interesting facts from this data set.

- 23 enlistees died at 15 years old. 478 died before they turned 18.
- The oldest casualty was Reverent Robert Ker, who died at 75 years old.
- The median age of death is 26 years old, and the average is 27.

## Further reading

You can find the code used to parse this data set [on GitHub](https://github.com/nicbou/canadians-at-war/tree/master/commonwealth-war-graves-commission). You can read more about this data set [on the Library and Archives Canada website](http://www.bac-lac.gc.ca/eng/discover/mass-digitized-archives/commonwealth-war-graves-registers/Pages/commonwealth-war-graves-registers.aspx).

This article is part of a series on Canadians at war, a project that aims to link and visualize open data about Canadians in the First World War. You can find the next article in the series [here](/blog/cracking-open-the-canadian-great-war-project-database "Cracking open the Canadian Great War Project database").

