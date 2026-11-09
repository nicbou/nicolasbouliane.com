---
title: How to fix ImportMismatchError in Python
description: If you get this error, it's probably a very easy fix. Here's how to fix this error with a single terminal command.
date_created: 2017-09-25
---

If you get an `ImportMismatchError` when running a Python app, it's likely that you have some Python bytecode files (`*.pyc`) from a different runtime. For example, this happens when I run my Python unit tests inside a Docker container, then try to run them again in PyCharm.

Here is an example error message:

```
/.../env/bin/python2.7 "/Applications/PyCharm CE.app/Contents/helpers/pycharm/_jb_pytest_runner.py" --target app_test.py::TestAppThing
Testing started at 10:51 AM ...
Launching py.test with arguments app_test.py::TestGroundTruthGet in /Users/xxxxxxx/Projects/.../app
Traceback (most recent call last):
 File "/.../env/lib/python2.7/site-packages/_pytest/config.py", line 362, in _importconftest
 mod = conftestpath.pyimport()
 File "/.../env/lib/python2.7/site-packages/py/_path/local.py", line 680, in pyimport
 raise self.ImportMismatchError(modname, modfile, self)
ImportMismatchError: ('module.name.here', '/app/filename.py', local('/Users/xxxxxxx/.../filename.py'))
ERROR: could not load /Users/xxxxxxx/.../filename.py

Process finished with exit code 0
Empty test suite.
```

The solution to this error is simple: delete all `*.pyc` files in your project. You can do this with a simple command:

```bash
find . -name \*.pyc -delete
```

Your Python code should now run properly.

