---
title: How to get the textarea's maxlength attribute to work in Internet Explorer
description: 
date_created: 2014-02-10
---

If you are developing for an older version of Internet Explorer (IE8 and older), you might have noticed that your chronogically-challenged browser does not support the maxlength attribute. Fortunately, you can solve it with a few lines of jQuery:

```
//textarea maxlength support for chronogically-challenged browsers
$('textarea[maxlength]').keyup(function(){
 //Get the value
 var text = $(this).val();
 //Get the maxlength
 var limit = $(this).attr('maxlength');
 //Check if the length exceeds what is permitted
 if(text.length > limit){
 //Truncate the text if necessary
 $(this).val(text.substr(0, limit)); 
 }
});

```

This snipped of code will apply the fix to all textareas in your page.

