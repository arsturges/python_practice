import sys, os
path = os.path.abspath(os.path.curdir)
print path
path += '/module_practice'
print path

if path not in sys.path:
	sys.path.insert(0,path)
print sys.path[0]
import andrew

import andrew
print andrew.taunt("Henry")
