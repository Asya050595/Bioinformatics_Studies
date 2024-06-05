with open('input-wc.txt') as fin:
	content = fin.read()
	line_count = content.count('\n')
	word_count = len(content.split())
	chr_count = len(content) 		

print('There are ', line_count, ' lines, ', word_count, ' words, and ', chr_count, ' characters in your file.')
