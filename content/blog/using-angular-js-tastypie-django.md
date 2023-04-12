---
title: Using angular.js with Tastypie for Django
description: 
date_created: 2013-11-05
---

The following angular.js service will allow you to consume a standard TastyPie REST API. As you may know, TastyPie returns its JSON objects a bit differently from what angular expects, so this service fixes it.

This example assumes that you have `always_return_data=True` in your resource. This is the resource I used with this example:

```
class NoteResource(ModelResource):
 class Meta:
 queryset = Note.objects.all()
 resource_name = 'note'
 #...
 list_allowed_methods = ['get', 'post', 'put', 'delete']
 always_return_data = True

```

If you don't have `always_return_data=True`, you will need to remove the `.success` part of the `create` method.

```
angular.module('notes.service', ['ngResource'])
 .factory('Note', ['$http', function($http){
 var Note = function(data) {
 angular.extend(this, data);
 };

 Note.get = function(id) {
 return $http.get('/api/v1/note/' + id).then(function(response) {
 return new Note(response.data);
 });
 };

 Note.getAll = function() {
 return $http.get('/api/v1/note/').then(function(response) {
 return response.data.objects;
 });
 };

 Note.save = function(note) {
 var url = '/api/v1/note/';

 return $http.post(url, note).success(function(returnedNote) {
 //IMPORTANT: You need to activate always_return_data in your ressource (see example) 
 note.id = returnedNote.id;
 }).error(function(data){
 console.log(data);
 });
 };

 Note.remove = function(id) {
 return $http.delete('/api/v1/note/' + id + '/').success(function(){
 console.log("delete successful");
 });
 };

 return Note;
 }]);
```

