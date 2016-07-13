__author__ = 'Richard'

import os
import subprocess
import sys

os.removedirs("C:\Workspace\SQALab\copy")

if not os.path.isdir("C:\Workspace\SQALab\copy"):
    try:
        string=os.mkdir("C:\Workspace\SQALab\copy",0o777)
        print('Directory Copy is created.')
    except:
        e = sys.exc_info()[1]
        print(e)
else:
    print("Directory already exists")

os.system('whoami')
print('END OF SCRIPT')