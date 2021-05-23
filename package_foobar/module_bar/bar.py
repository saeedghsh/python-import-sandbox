import sys


bar_var = "bar var"


def print_file_metadata():
    print("****************************************")
    print("*** __file__\t{}".format(__file__))
    print("*** __name__\t{}".format(__name__))
    print("*** __package__\t{}".format(__package__))
    print("*** system paths:")
    for path in sys.path:
        print("\t{:s}".format(path))
    print()


print_file_metadata()
