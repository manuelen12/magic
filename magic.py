import sys

from class_magic import Magic

if __name__ == "__main__":
    # execute only if run as a script
    magic = Magic(int(sys.argv[1]))
    magic.get_value()
