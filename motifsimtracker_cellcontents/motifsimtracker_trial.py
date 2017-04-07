from motifsimtracker_cell import Cell
from motifsimtracker_population import Population
import random as rand
from copy import deepcopy
from copy import copy

def motifsimtracker_trial(celllist,elonglist,initialtracked,motif,max_strand_nr,maxStrandLength,numCells,numRounds,elong,bias):

	initialdictionary = {}
	for cell in range(len(celllist)):
		if cell in initialtracked:
			motif_counter = 0
			for strand in celllist[cell]:
				if motif in strand:
					motif_counter += 1

			initialdictionary[cell] = {'nr_motifs':[motif_counter]}

	population = Population([],initialdictionary,numCells,'empty','empty','empty')

	population.initial_condition_populate(celllist,elonglist,motif,max_strand_nr)

	# counter lists
	nr_motifs = []
	nr_strands_used = []
	nr_cells_with_motif = []
	population_tracker = []
	elongation_tracker = []

	for time in xrange(numRounds):
		for cell_iterator in xrange(numCells):
			population.cells[cell_iterator].grow(elong,bias,maxStrandLength)

		cell_to_divide = rand.sample(range(numCells),1)[0]

		new_cell = population.cells[cell_to_divide].divide(population)
		population.cells.append(new_cell)

		population.cells = rand.sample(population.cells,numCells)

		population.update_counters()
		population.update_tracker(numCells)

		nr_motifs.append(copy(population.nr_motifs))
		nr_strands_used.append(copy(population.nr_strands))
		nr_cells_with_motif.append(copy(population.nr_cells_with_motif))
		population_tracker_temp, elongation_tracker_temp = population.returncontents()
		population_tracker.append(deepcopy(population_tracker_temp))
		elongation_tracker.append(deepcopy(elongation_tracker_temp))

	tracked_list = deepcopy(population.show_tracked())

	return nr_motifs, nr_strands_used, nr_cells_with_motif, population_tracker, elongation_tracker, tracked_list