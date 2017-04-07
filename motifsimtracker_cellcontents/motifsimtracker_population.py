from motifsimtracker_cell import Cell

class Population:

	def __init__(self,cells,tracked_dict,identity_tracker,nr_motifs,nr_strands,nr_cells_with_motif):
		self.cells = cells
		self.tracked_dict = tracked_dict
		self.identity_tracker = identity_tracker
		self.nr_motifs = self.count_motifs()
		self.nr_strands = self.count_strands()
		self.nr_cells_with_motif = self.count_cells_with_motif()

	def initial_condition_populate(self,celllist,elonglist,motif,max_strand_nr):
		for cell_iterator in xrange(len(celllist)):
			self.cells.append(Cell(cell_iterator,celllist[cell_iterator],elonglist[cell_iterator],motif,max_strand_nr,'empty','empty','empty'))
		self.update_counters()

	def increment_identity(self):
		self.identity_tracker += 1

	def populate(self,numCells,motif,max_strand_nr):
		for cell_iterator in xrange(numCells):
			self.cells.append(Cell(cell_iterator,[],[],motif,max_strand_nr,'empty','empty','empty'))
		self.update_counters()

	def update_counters(self):
		self.nr_motifs = self.count_motifs()
		self.nr_strands = self.count_strands()
		self.nr_cells_with_motif = self.count_cells_with_motif()

	def count_motifs(self):
		motif_count = 0
		for cell in self.cells:
			motif_count = motif_count + cell.motif_count()

		return motif_count

	def count_strands(self):
		strand_count = 0
		for cell in self.cells:
			strand_count = strand_count + cell.nr_strands()
		return strand_count

	def count_cells_with_motif(self):
		cell_count = 0
		for cell in self.cells:
			if cell.has_motif == True:
				cell_count += 1

		return cell_count

	def show_tracked(self):
		return self.tracked_dict

	def update_tracker(self,numCells):
		for cell in self.cells:
			# print cell
			# print cell.identity
			# print cell.nr_motifs
			# print self.tracked_dict[cell.identity]
			# print self.tracked_dict[cell.identity]['nr_motifs']
			# print self.cells
			# print self.tracked_dict
			# print self.tracked_dict[cell_iterator]
			self.tracked_dict[cell.identity]['nr_motifs'].append(cell.nr_motifs)

	def returncontents(self):
		contents = []
		elong_contents = []

		for cell in self.cells:
			contents.append(cell.strands)
			elong_contents.append(cell.elongations)

		return contents, elong_contents
