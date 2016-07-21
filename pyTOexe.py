import os
import sys

if len(sys.argv) > 1:
	None
else:
	file = input("Which script do you want to compile?:")
	os.system("C:\Python34\Scripts\cxfreeze "+file)
	print("done!")