import csv
import sys
import getopt

def main(argv):

	try:
		opts, args = getopt.getopt(argv, "h", ["help","file=","round="])
	except getopt.GetoptError, error:
		sys.stderr.write(str(error)+"\n")
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt == '--file' :
			input_file = arg
		elif opt == '--round' :
			intended_round = int(arg)
		else:
			sys.stderr.write("Unknown option %s\n" %opt)
			usage()
			sys.exit(2)

	with open(input_file) as f:
		handle = csv.reader(f,quotechar="'", quoting=csv.QUOTE_ALL)
		line_counter = 0
		rows = []
		for line in handle:
			if line_counter == 0:
				numCells = int(line[3])
				numRounds = int(line[4])
				line_counter += 1
			else:
				if line_counter > 2*intended_round*numCells and line_counter < 2*(intended_round+1)*numCells+1:
					rows.append(line)
				line_counter += 1
	f.close()

	output_file = input_file.replace('MotifSimulation','initialconditions').replace('numRound'+str(numRounds),'round'+str(intended_round))

	with open(output_file, 'wb') as f:
		writer = csv.writer(f)
		strand_writer = csv.writer(f,quotechar="'", quoting=csv.QUOTE_ALL)
		for row in rows:
			strand_writer.writerow(row)

	f.close()


if __name__ == "__main__":
	main(sys.argv[1:])