'''This script will tes the unixpath module'''

import pytest
from unixpath import *

def newTestCases():
	# Returns list of test cases
	return [["testData/comma.csv", ",", "comma", "testData", "csv"],
		["testData/tab.tsv", "\t", "tab", "testData", "tsv"],
		["testData/space.txt", " ", "space", "testData", "txt"]]		

def test_getExt():
	# Tests getExt
	cases = newTestCases()
	for i in cases:
		assert getExt(i[0]) == i[4]

def test_getFileName():
	# Tests getFileName
	cases = newTestCases()
	for i in cases:
		assert getFileName(i[0]) == i[2]

def getParent():
	# Tests getParent
	cases = newTestCases()
	for i in cases:
		assert getParent(i[0]) == i[3]

def test_getDelim():
	# Tests getDelim on test files
	cases = newTestCases()
	for i in cases:
		with open(i[0], "r") as f:
			for line in f:
				assert getDelim(line) == i[1]
				break
