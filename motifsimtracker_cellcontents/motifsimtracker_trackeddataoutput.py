
import csv

def motifsimtracker_trackeddataoutput(parameterlist,masterprefix,testprefix,all_tracked,nr_strands_per_time,trials,max_strand_nr,maxStrandLength,numCells,numRounds,motif,elong,bias):

	with open(masterprefix + testprefix +'_TrackedData_motif{motif}_len{maxStrandLength}_bias{bias}_elong{elong}_{trials}trials_numRound{numRounds}.csv'.format(motif = motif, maxStrandLength = maxStrandLength, bias= bias, elong=elong, trials=trials, numRounds=numRounds), 'wb') as f:

		strand_writer = csv.writer(f, quotechar="'", quoting=csv.QUOTE_ALL) # making sure we put quotes around our strings so they're not read as numbers
		parameter_writer = csv.writer(f) # we don't need the quotes for the parameter list

		parameter_writer.writerow(parameterlist)

		for trial in xrange(trials):
			strand_writer.writerow(["Trial {}".format(trial),"Motif Bool","Daughters"])
			for key, value in all_tracked[trial].iteritems():
				row_print = []
				row_print.append(key)
				for inner_key,inner_value in value.iteritems():
					row_print.append(inner_value)
				parameter_writer.writerow(row_print)

	f.close()