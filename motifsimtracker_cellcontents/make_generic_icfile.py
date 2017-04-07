import csv
import sys
import random
import itertools
import numpy as np

def makeKeyorder(maxstrandlen): # create the keyorder for the order of our dictionary
	
	keyorder = []

	for n in xrange(maxstrandlen): # create order of keys for the ordered dictionary
		for key in itertools.product(range(2),repeat = n+1):
			mod_key = str(key).strip(" ,(),','").replace(", ", "")
			if len(keyorder) > 0:
				if len(mod_key) == len(keyorder[-1]):
					for keys_so_far in xrange(len(keyorder)):
						if len(mod_key) == len(keyorder[keys_so_far]):
							if mod_key.count('1') < keyorder[keys_so_far].count('1'):
								keyorder.insert(keys_so_far,mod_key)
								break
					else:
						keyorder.append(mod_key)
				else:
					keyorder.append(mod_key)
			else:
				keyorder.append(mod_key)

	return keyorder

numCells = 100
numStrands = 100
maxStrandLen = 7

strand_list = []
elong_list = []

all_strands = makeKeyorder(maxStrandLen)

no_motifs = []

for strand in all_strands:
	if '10000' not in strand:
		no_motifs.append(strand)

# for cell in range(numCells):
# 	strand_list.append([])
# 	elong_list.append([])
# 	strand_counter = 0
# 	for strand in range(numStrands):
# 		if np.random.uniform() < .5:
# 			strand_list[cell].append(random.choice(all_strands))
# 			elong_list[cell].append('-'*len(strand_list[cell][strand_counter]))
# 			# strand_list[cell].append('10000')
# 			# elong_list[cell].append('-----')
# 			strand_counter += 1
			
for cell in range(numCells):
	strand_list.append([])
	elong_list.append([])
	strand_counter = 0
	for strand in range(numStrands):
		if np.random.uniform() < .5:
			strand_list[cell].append(random.choice(no_motifs))
			elong_list[cell].append('-'*len(strand_list[cell][strand]))
		else:
			strand_list[cell].append('10000')
			elong_list[cell].append('-----')
			

# strands = ['10000'] * numStrands
# elongs = ['-' * 5] * numStrands

output_file = 'initialconditions_halfmotifhalfrandom.csv'

with open(output_file, 'wb') as f:
	writer = csv.writer(f)
	strand_writer = csv.writer(f,quotechar="'", quoting=csv.QUOTE_ALL)
	for cell in range(numCells):
		strand_writer.writerow(strand_list[cell])
		strand_writer.writerow(elong_list[cell])
		# strand_writer.writerow(strands)
		# strand_writer.writerow(elongs)

f.close()



