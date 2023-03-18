import sys

if len(sys.argv) < 4:
    print("Error: Insufficient arguments provided")
else:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    result = arg1 + arg2 + arg3
    print(result)

#