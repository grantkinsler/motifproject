import csv
from motifcompetesim_trial import motifcompetesim_trial
import itertools
import numpy

def flatten(items, seqtypes=(list, tuple)): # used for flattening lists
    for i, x in enumerate(items):
        while isinstance(items[i], seqtypes):
            items[i:i+1] = items[i]
    return items

def motifcompetesim_motifoutput(parameterlist,masterprefix,testprefix,trials,max_strand_nr,maxStrandLength,numCells,numRounds,motiflist,elong,biaslist):
	pop_tracker = []
	elongation_tracker = []


	with open(masterprefix+ testprefix +'_MotifData_motif{motif}_len{maxStrandLength}_bias{bias}_elong{elong}_{trials}trials_numRound{numRounds}.csv'.format(motif = '|'.join([repr(motif) for motif in motiflist]), maxStrandLength = maxStrandLength, bias='|'.join([str(bias) for bias in biaslist]), elong=elong, trials=trials, numRounds=numRounds), 'wb') as f: 
		writer = csv.writer(f)
		writer.writerow(parameterlist)

		motif_freq = [''] * len(motiflist)
		motif_freq_aggregate = [''] * len(motiflist)
		cells_with_freq = [''] * len(motiflist)
		cells_with_freq_aggregate = [''] * len(motiflist)

		for trial in xrange(trials):
			pop_tracker.append([])
			elongation_tracker.append([])
			nr_motifs, nr_strands, nr_cells_with_motif, pop_tracker[trial], elongation_tracker[trial] = motifcompetesim_trial(motiflist,max_strand_nr,maxStrandLength,numCells,numRounds,elong,biaslist)

			for index in xrange(len(motiflist)):
				motif_freq[index] = [motifs / float(total) for motifs,total in itertools.izip(nr_motifs[index],nr_strands)]
				cells_with_freq[index] = [cells / float(numCells) for cells in nr_cells_with_motif[index]]
			strands_freq = [strands / float(max_strand_nr*numCells) for strands in nr_strands]
			
			for index in xrange(len(motiflist)):
				writer.writerow(motif_freq[index])
			for index in xrange(len(motiflist)):
				writer.writerow(cells_with_freq[index])
			writer.writerow(strands_freq)
			

			if trial == 0:
				for index in xrange(len(motiflist)):
					motif_freq_aggregate[index] = motif_freq[index]
					cells_with_freq_aggregate[index] = cells_with_freq[index]
				strands_freq_aggregate = strands_freq	
				nr_strands_per_time = nr_strands
			else:
				for index in xrange(len(motiflist)):
					motif_freq_aggregate[index] = [list(round_data) for round_data in zip(motif_freq_aggregate[index],motif_freq[index])]
					cells_with_freq_aggregate[index] = [list(round_data) for round_data in zip(cells_with_freq_aggregate[index],cells_with_freq[index])]
				strands_freq_aggregate = [list(round_data) for round_data in zip(strands_freq_aggregate,strands_freq)]
				nr_strands_per_time = [list(round_data) for round_data in zip(nr_strands_per_time,nr_strands)]
		
		for time_point in xrange(numRounds):
			for index in xrange(len(motiflist)):
				motif_freq_aggregate[index][time_point] = flatten(motif_freq_aggregate[index][time_point])
				cells_with_freq_aggregate[index][time_point] = flatten(cells_with_freq_aggregate[index][time_point])
			strands_freq_aggregate[time_point] = flatten(strands_freq_aggregate[time_point])
			nr_strands_per_time[time_point] = flatten(nr_strands_per_time[time_point])
		
		means = []
		stdevs = [] 

		for iterator in xrange(1+2*len(motiflist)):
			means.append([])
			stdevs.append([])

		for time_point in xrange(numRounds):
			for index in xrange(len(motiflist)):
				means[index].append(numpy.mean(motif_freq_aggregate[index][time_point]))
				stdevs[index].append(numpy.std(motif_freq_aggregate[index][time_point],dtype=numpy.float64))
				means[index+len(motiflist)].append(numpy.mean(cells_with_freq_aggregate[index][time_point]))
				stdevs[index+len(motiflist)].append(numpy.std(cells_with_freq_aggregate[index][time_point],dtype=numpy.float64))

			means[2*len(motiflist)].append(numpy.mean(strands_freq_aggregate[time_point]))
			stdevs[2*len(motiflist)].append(numpy.std(strands_freq_aggregate[time_point],dtype=numpy.float64))

		for mean_data in means:
			writer.writerow(mean_data)

		for stdev_data in stdevs:
			writer.writerow(stdev_data)
	f.close()

	return pop_tracker, nr_strands_per_time, elongation_tracker
