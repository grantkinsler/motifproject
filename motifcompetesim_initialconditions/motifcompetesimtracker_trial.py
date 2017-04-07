from motifcompetesimtracker_cell import Cell
from motifcompetesimtracker_population import Population
import random as rand
from copy import deepcopy
from copy import copy

def motifcompetesim_trial(celllist,elonglist,motiflist,max_strand_nr,maxStrandLength,numCells,numRounds,elong,biaslist):

	population = Population([],motiflist,'empty','empty','empty')

	population.populate(numCells,motiflist,max_strand_nr)

	population.initial_condition_populate(celllist,elonglist,motiflist,max_strand_nr)

	# counter lists
	nr_motifs = []
	nr_cells_with_motif = []
	for iterator in xrange(len(motiflist)):
		nr_motifs.append([])
		nr_cells_with_motif.append([])
	nr_strands_used = []
	population_tracker = []
	elongation_tracker = []

	for time in xrange(numRounds):
		for cell_iterator in xrange(numCells):
			population.cells[cell_iterator].grow(elong,biaslist,maxStrandLength)

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

	return nr_motifs, nr_strands_used, nr_cells_with_motif, population_tracker, elongation_tracker