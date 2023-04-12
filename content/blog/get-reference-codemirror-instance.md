---
title: How to get a reference to a CodeMirror instance
description: 
date_created: 2013-11-12
---

If you want to access a CodeMirror instance, perhaps because it was created programmatically, or by a module you don't control, you can access it like this:

```
//Get a reference to the CodeMirror editor
var editor = $('.CodeMirror')[0].CodeMirror;

//You can then use it as you wish
editor.setValue('lorem ipsum yada yada');
editor.replaceSelection('this is a test');
```

In fact, the CodeMirror wrapper element (which has the CodeMirror class) has a CodeMirror attribute which you can use to access the editor's options and methods.

This can be pretty useful if you use [ui.codemirror](https://github.com/angular-ui/ui-codemirror) from Angular UI

