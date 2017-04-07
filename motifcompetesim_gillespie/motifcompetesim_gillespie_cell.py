import random as rand

class Cell:

	def __init__(self,strands,elongations,motiflist,max_strand_nr,nr_motifs,has_motif,nr_bases):
		self.strands = strands
		self.elongations = elongations
		self.motiflist = motiflist
		self.max_strand_nr = max_strand_nr
		self.nr_motifs = self.motif_count()
		self.has_motif = self.check_for_motif()
		self.nr_bases = self.find_nr_bases()


	def check_for_motif(self):
		checked_list = []
		for index in xrange(len(self.motiflist)):
			if self.nr_motifs[index] > 0:
				checked_list.append(True)
			else:
				checked_list.append(False)
		return checked_list

	def motif_count(self):
		motif_count = [0] * len(self.motiflist)
		for strand_iterator in range(self.nr_strands()):
			for index in xrange(len(self.motiflist)):
				if str(self.motiflist[index]) in self.strands[strand_iterator]:
					motif_count[index] += 1
		return motif_count

	def update_motifs(self):
		self.nr_motifs = self.motif_count()
		self.has_motif = self.check_for_motif()

	def update_nr_bases(self):
		self.nr_bases = self.find_nr_bases()

	def find_nr_bases(self):
		nr_bases = 0
		for strand in self.strands:
			nr_bases += len(strand)
		return nr_bases

	def nr_strands(self):
		strand_counter = 0
		for strand in self.strands:
			if len(strand) > 0:
				strand_counter += 1
		return strand_counter

	def grow(self,strand,biaslist,maxStrandLength):

		if strand in xrange(self.nr_strands()):
			if len(self.strands[strand]) < maxStrandLength:
				for index in range(len(self.motiflist)):
					indexvalue = self.nr_motifs.pop(index)
					if indexvalue > max(self.nr_motifs): # it is uniquely the maximum number
						self.nr_motifs.insert(index,indexvalue)
						if rand.uniform(0,1) < biaslist[index]:
							self.strands[strand] = self.strands[strand] + "0"
							self.elongations[strand] = self.elongations[strand] + repr(index)
						else:
							self.strands[strand] = self.strands[strand] + "1"
							self.elongations[strand] = self.elongations[strand] + repr(index)
						break
					else:
						self.nr_motifs.insert(index,indexvalue)
				else:
					if rand.uniform(0,1) < 0.5:
						self.strands[strand] = self.strands[strand] + "0"
						self.elongations[strand] = self.elongations[strand] + "-"
					else:
						self.strands[strand] = self.strands[strand] + "1"
						self.elongations[strand] = self.elongations[strand] + "-"
		else:
			for index in xrange(len(self.motiflist)):
				indexvalue = self.nr_motifs.pop(index)
				if indexvalue > max(self.nr_motifs): # it is uniquely the maximum number
					self.nr_motifs.insert(index,indexvalue)
					if rand.uniform(0,1) < biaslist[index]:
						self.strands.append("0")
						self.elongations.append(repr(index))
					else:
						self.strands.append("1")
						self.elongations.append(repr(index))
					break
				else:
					self.nr_motifs.insert(index,indexvalue)
			else:
				if rand.uniform(0,1) < 0.5:
					self.strands.append("0")
					self.elongations.append("-")
				else:
					self.strands.append("1")
					self.elongations.append("-")

		self.update_motifs()
		self.update_nr_bases()


	def divide(self):
		new_cell = Cell([],[],self.motiflist,self.max_strand_nr,'empty','empty','empty')
		strand_counter = 0
		for strand_number in xrange(self.nr_strands()):
			if rand.uniform(0,1) < 0.5:
				new_cell.strands.append(self.strands.pop(strand_counter)) # this strand is removed from cell and added to new cell
				new_cell.elongations.append(self.elongations.pop(strand_counter)) # this strand is removed from cell and added to new cell
			else:
				strand_counter += 1

		new_cell.update_motifs()
		new_cell.update_nr_bases()
		self.update_motifs()
		self.update_nr_bases()

		return new_cell



