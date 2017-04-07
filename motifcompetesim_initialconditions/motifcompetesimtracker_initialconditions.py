import csv
from copy import copy

def motifcompetesimtracker_initialconditions(ic_file):

	celllist = []
	elonglist = []

	with open(ic_file) as f:
		handle = csv.reader(f,quotechar="'", quoting=csv.QUOTE_ALL)
		linenum = 0
		for line in handle:
			if linenum % 2 == 0:
				celllist.append(line)
			else:
				elonglist.append(line)
			linenum += 1
			# celllist.append(copy(line))
			# elonglist.append(copy(line))

	f.close()

	return celllist, elonglist