from motifcompetesim_gillespie_cell import Cell
from motifcompetesim_gillespie_population import Population
import random as rand
from copy import deepcopy
from copy import copy
import math

def motifcompetesim_trial(motiflist,max_strand_nr,maxStrandLength,numCells,numRounds,elong,biaslist):

	population = Population([],motiflist,'empty','empty','empty')

	population.populate(numCells,motiflist,max_strand_nr)

	# counter lists
	nr_motifs = []
	nr_cells_with_motif = []
	for iterator in xrange(len(motiflist)):
		nr_motifs.append([])
		nr_cells_with_motif.append([])
	nr_strands_used = []
	population_tracker = []
	elongation_tracker = []
	time_tracker = []

	elongation_rate = elong*numCells*max_strand_nr
	division_rate = 1
	total_rate = elongation_rate + division_rate

	num_divisions = 0
	running_time = 0


	while num_divisions < numRounds:

		rxn_decision = rand.uniform(0,1)

		time_unif = rand.uniform(0,1)

		rxn_time = math.log(1-time_unif)/(-1*total_rate)
		running_time += rxn_time

		if rxn_decision < elongation_rate/total_rate:
			cell_num = rand.sample(range(numCells),1)[0]
			strand_num = rand.sample(range(max_strand_nr),1)[0]
			population.cells[cell_num].grow(strand_num,biaslist,maxStrandLength)
		else:
			cell_to_divide = rand.sample(range(numCells),1)[0]

			new_cell = population.cells[cell_to_divide].divide()
			population.cells.append(new_cell)

			population.cells = rand.sample(population.cells,numCells)

			population.update_counters()

			for index in xrange(len(motiflist)):
				nr_motifs[index].append(copy(population.nr_motifs[index]))
				nr_cells_with_motif[index].append(copy(population.nr_cells_with_motif[index]))
			nr_strands_used.append(copy(population.nr_strands))
			population_tracker_temp, elongation_tracker_temp = population.returncontents()
			population_tracker.append(deepcopy(population_tracker_temp))
			elongation_tracker.append(deepcopy(elongation_tracker_temp))
			time_tracker.append(copy(running_time))

			num_divisions += 1

	return nr_motifs, nr_strands_used, nr_cells_with_motif, population_tracker, elongation_tracker, time_tracker