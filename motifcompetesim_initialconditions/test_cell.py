from motifcompetesim_cell import Cell
from motifcompetesim_population import Population

def test_cell_object():
	cell1=Cell([],["000","000","1111","111111"],[],4,"empty","empty","empty")
	assert sum(cell1.motif_count())==0
	assert cell1.max_strand_nr==4
	assert sum(cell1.check_for_motif())==0
	cell1.strands=["100","010","0000","000000"]
	cell1.motiflist=["010","000"]
	cell1.update_motifs()
	assert sum(cell1.motif_count())==3
	assert sum(cell1.check_for_motif())==2
	assert sum(cell1.nr_motifs)==3
	for i in range(100):
		assert sum(cell1.nr_motifs)>0
		cell1.grow(0.8,[0.1,0.2],4)
	assert cell1.motif_count()>0	
	assert cell1.motif_count()
	cell2=cell1.divide()
	assert cell2.max_strand_nr==cell1.max_strand_nr
	assert sum(cell2.check_for_motif())>0
	assert cell2.motiflist==["010","000"]
	print "cell1", cell1.strands
	print "cell2", cell2.strands
	print "Cell object tests passed"

def test_population_object():
    # pop1=Population([],[],[],[],[])
    motif_list=['0101','000']
    pop1=Population([],motif_list,'empty','empty','empty')
    pop1.populate(10,motif_list,6)
    # pop1.populate(1,motif_list,10)
    assert len(pop1.cells) >0
    for cell in pop1.cells:
    	for i in range(1000):
    		cell.grow(0.8,[0.1,0.2],4)
    print "motif", motif_list
    print pop1.cells[0].strands
    all_strands=[strand for strand in cell.strands  for cell in pop1.cells]
    #print all_strands
    pop1.update_counters()
    print pop1.motiflist
    print pop1.count_motifs()
    print pop1.nr_motifs
    print pop1.count_strands()
    print pop1.nr_strands

    assert pop1.nr_motifs == pop1.count_motifs()
    # print pop1.cells[0].strands
    if motif_list[0] in all_strands or motif_list[1] in all_strands:
    	print pop1.count_cells_with_motif()
    	assert sum(pop1.count_cells_with_motif()) >=1

    	print "there is a problem here"
    print "Population object tests passed"

