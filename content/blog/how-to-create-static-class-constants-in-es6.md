---
title: How to create static class constants in ES6
description: ES6 brings classes to JavaScript, but some things are not immediately obvious or entirely supported. For instance, there is no obvious way to create static class constants.
date_created: 2016-04-05
---

ES6 brings classes to JavaScript, but some things are not immediately obvious or entirely supported. For instance, there is no obvious way to create static class constants.

Here is the simplest way I have found to create constants:

```javascript
class CurrentLocation {
    static get GEOLOCATION_ERROR() { return 'GEOLOCATION_ERROR'; }
    static get GEOLOCATION_REFUSED() { return 'GEOLOCATION_REFUSED'; }
    static get GEOLOCATION_ACQUIRED() { return 'GEOLOCATION_ACQUIRED'; }
    static get GEOLOCATION_PENDING() { return 'GEOLOCATION_PENDING'; }

    // ...

    function isValid(){
        return this.status === CurrentLocationItem.GEOLOCATION_ACQUIRED
    }
}
```

In the example below, you can use `CurrentLocation.GEOLOCATION_ERROR` anywhere, but `myGeolocationItem.GEOLOCATION_ERROR` will not exist, as static members are not visible to class instances. Moreover, children of the `CurrentLocation` class will not inherit these attributes.

