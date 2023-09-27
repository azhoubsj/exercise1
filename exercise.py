data = [1, 3, 5, 7, 9]
with open('exercise.csv', 'w') as f:
	for d in data:
		f.write(str(d) + '\n') 