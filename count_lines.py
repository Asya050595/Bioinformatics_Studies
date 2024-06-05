def code_metric(filename):
	line_count = char_count = 0
	with open(filename) as fin:
		stripped = (line.rstrip() for line in fin)
		for line_count, line in enumerate(filter(None, stripped), 1):
        		char_count += len(line)
	return line_count

number = code_metric('input-countlines.txt')


print("There are ", number , "non-empty lines in your file.")
