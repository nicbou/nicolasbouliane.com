---
title: Fixing Jasmine "encountered a declaration exception"
description: If you ever come upon a Jasmine unit test that ends with "encountered a declaration exception", it's likely because you have committed a simple, subtle mistake.
date_created: 2016-07-08
---

If you ever come upon a Jasmine unit test that ends with "encountered a declaration exception", it's likely because you have committed a simple, subtle mistake. Every few weeks, I would get that error, and forgetting how I fixed it the previous time, spend another 30 minutes to fix it.

Here's the code that caused it:

```
describe('should be hidden when the scope is destroyed', () => {
 this.scope.$broadcast('$destroy');
 expect(this.scope.helpTooltip.hide).toHaveBeenCalledWith();
});
```

Can you spot the problem? It's simple: I used `describe` instead of `it`. Let's fix this...

```
it('should be hidden when the scope is destroyed', () => {
 this.scope.$broadcast('$destroy');
 expect(this.scope.helpTooltip.hide).toHaveBeenCalledWith();
});
```

Voilà! No more error! Sometimes, the solution is that simple.

