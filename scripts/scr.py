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


def insert_parent_path_to_sys_path(verbose: bool = False):
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)


# The problem with inserting the parent_dir to sys.path is that for
# every file importing from parent the correct path should be
# insterted. That is to say, foo is able to import bar if this script
# is run first and the parent path in inserted. But trying to import
# foo from elsewhere would fail if its parent path in not insterted
# already. This is an issue if we want to build binaries of the
# modules independant of the scripts. Or there is a change new scritp
# is created that does not add the correct path. This means each
# module has to have a copy of this path insertion to access to
# parent.  How about path stuff become a separete package with it's
# own binary target. this will resolve the binary build, not
# interactive execution on the host.
insert_parent_path_to_sys_path(verbose=True)
# from ..module_foo doesn't work here
from package_foobar.module_foo import foo


# conclusion: move python path lib stuff to the script folder and make
# sure all scripts call and add paths! then don't need to add
# insert_parent_path_to_sys_path function, just hard-code the pytool
# path into sys.path
