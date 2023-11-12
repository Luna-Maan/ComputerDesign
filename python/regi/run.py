import sys
import os

if sys.argv[1][-4:] == ".ovt" or sys.argv[1][-5:] == ".rasm":
    file_name = os.path.join(__file__, '../assemblyimport.py')
    exec(open(file_name).read())
elif sys.argv[1][-5:] == ".high":
    file_name = os.path.join(__file__, '../hcompiler.py')
    exec(open(file_name).read())
