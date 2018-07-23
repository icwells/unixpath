'''This script contains common functions for manipulating paths in unix platforms.'''

import os

def checkDir(path, make = False):
	# Checks if path exists, throws error if make is false, makes dir if true, returns formatted name
	if path[-1] != "/":
		path += "/"
	if os.path.isdir(path) == False:
		if make == False:
			print(("\n\t[Error] {} not found. Exiting.\n").format(path))
			quit()
		else:
			os.mkdir(path)
	return path

def checkFile(infile):
	# Raises if infile is not found
	if not os.path.isfile(infile):
		print(("\n\t[Error] {} not found. Exiting.\n").format(infile))
		quit()

def getExt(name):
	# Returns extension from filename
	return name[name.rfind(".")+1:]

def getFileName(path):
	# Returns filename sans path and extension
	return path[path.rfind("/")+1:path.find(".")]

def getParent(path):
	# Returns parent directory from path
	if "." in path and path[-1] != "/":
		# Drop filename
		path = path[:path.rfind("/")]
	elif path [-1] == "/":
		path = path[:-1]
	return path[path.rfind("/")+1:]
