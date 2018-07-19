'''This script contains common functions for manipulating paths in unix platforms.'''

import os

def checkDir(path, make = False):
	# Checks if path exists, throws error if make is false, makes dir if true, returns formatted name
	if path[-1] != "/":
		path += "/"
	if os.path.isdir(path) == False:
		if make == False:
			raise NotADirectoryError(("{} not found.").format(path))
		else:
			os.mkdir(path)
	return path

def checkFile(infile):
	# Raises if infile is not found
	if not os.path.isfile(infile):
		raise FileNotFoundError(("{} not found").format(infile))

def getExt(name):
	# Returns extension from filename
	return name[name.rfind(".")+1:]

def getFileName(path):
	# Returns filename sans path and extension
	return path[path.rfind("/")+1:path.find(".")]
