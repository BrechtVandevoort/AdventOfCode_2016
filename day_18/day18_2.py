puzzle_input = open('input.txt').read().strip()

def get_next_tile(prev_tiles):
	if prev_tiles == '^^.' or prev_tiles == '.^^' or prev_tiles == '^..' or prev_tiles == '..^':
		return '^'
	else:
		return '.'

def get_next_row(prev_row):
	row = ''
	prev_row = '.' + prev_row + '.'
	for i in xrange(1, len(prev_row) - 1):
		row += get_next_tile(''.join(prev_row[i-1:i+2]))
	return row

row = puzzle_input
count = sum(1 for tile in row if tile == '.')

for _ in xrange(400000-1):
	row = get_next_row(row)
	count += sum(1 for tile in row if tile == '.')

print count
