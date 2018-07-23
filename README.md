# unixpath v1.0 contains common functions for manipulating paths on unix platforms.  

### Specifically it contains functions which are not included in os.path or which combine functions in ways that, honestly, I'm just sick of writing.  
### This is meant primarily for personal use (and may see periodic updates), but is publicly available for use under the terms of the GPL 3.  

Copyright 2018 by Shawn Rupp  

## Installation  

	git clone https://github.com/icwells/unixpath.git  

	cd unixpath/  
	python setup.py install  

## Usage  

	import unixpath
or  
	from unixpath import *  

#### unixpath.checkDir(path, make = False)  
If the directory does not exist and make is False, it will raise a NotADirectoryError. If make is True, it will make the directory.  
If an error was not raised, it returns the path name with a trailing slash (if the input name did not have one).  

#### unixpath.checkFile(infile)
Raises a FileNotFoundError if the file does not exist.   

#### unixpath.getExt(name)
Returns the extension (everything after last period) from the filename.  

#### unixpath.getFileName(path)
Returns the filename stem (everything between last slash and first period) from a given path.  

#### unixpath.getParent(path)   
Returns parent directory from path (i.e. the last directory name in the path).  
