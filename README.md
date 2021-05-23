# Python import sandbox
Trying to figure out the python import


## problem description
Ideally I would like to have a project structure like:
```bash
├── package_foobar
│   ├── module_bar
│   │   └── bar.py
│   └── module_foo
│       └── foo.py
└── scripts
    └── scr.py
```

Furthermore, I would to:
```python
# in scr.py
import module_foo.foo

# in foo.py 
import module_bar.bar
```

I was hoping simply using `import` with `.`, `..`, and `...` would work here.
But it doesn't if `package_foobar` is not recognized as a package by python interpreter and results in:
```bash
ValueError: attempted relative import beyond top-level package
```

## Solution so far
Unfortunately I couldn't find a solution to this so far.
The only solutions are:
* Move `scr.py` out of `scripts` to sit next to `package_foobar`.
  The path of the script that will have the `__main__` name will be added to `sys.path`.
  Having `scr.py` next to `package_foobar` will make `package_foobar` available in python path.  
  Cons: restriction of the placement of the script.
* Extract the path to the parent of the `scr.py` and add to `sys.path`.  
  Cons: assume the package is in the parent dir of the `scr.py`. Also I don't like manual manipulation of the `sys.path`.

## References
* ["relative imports for the billionth time"](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912) on stackoverflow.com.
* [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/#reader-comments) on "realpython.com"  
  My objective is the section "Subpackages" of this article, but I think it doesn't work.

## License
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/transformation-playground/blob/master/LICENSE).
```
Copyright (C) Saeed Gholami Shahbandi
```
