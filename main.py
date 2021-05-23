import sys
import os


def print_file_detail():
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    parent_dir = os.path.dirname(this_dir)
    print("****************************************")
    print("*** Running  scr.py")
    print("*** __file__\t{}".format(__file__))
    print("\t* file path:\t{:s}".format(this_file))
    print("\t* dir path\t{:s}".format(this_dir))
    print("\t* parent dir:\t{:s}".format(parent_dir))
    print("*** __name__\t{}".format(__name__))
    print("*** __package__\t{}".format(__package__))
    print("*** system paths:")
    for path in sys.path:
        print("\t{:s}".format(path))
    print()


print_file_detail()


# if the script (here main.py) is located next to the package is, and
# that path being added to the sys.path, relative imports works
from package_foobar.module_foo import foo
_ = foo.foo_var
