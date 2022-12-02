#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))

        #if len(sys.argv) == 0 and count == 0:
         #   print("{:d} arguments.".format(len(sys.argv)))
        #elif len(sys.argv) > 1:
         #   print("{:d} arguments:".format(len(sys.argv)))
          #  print("{:d}: {:s}".format(count, x))
       # else:
        #    print("{:d} argument:".format(len(sys.argv)))
         #   print("{:d}: {:s}".format(count, x))
