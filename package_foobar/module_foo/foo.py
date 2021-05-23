import sys
import os


foo_var = "foo var"


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


def insert_parent_path_to_sys_path(verbose: bool = False):
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)


# insert_parent_path_to_sys_path(verbose=True)
from package_foobar.module_bar import bar
# from ..module_bar import bar # also works
