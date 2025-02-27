data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('Finished reading the reviews, there are', len(data), 'reviews in total.')


sum_len = 0
for d in data:
	sum_len += len(d)

print('The average length of reviews is', sum_len/len(data))

new = []

for d in data:
	if len(d) < 100:
		new.append(d)

print('There are', len(new), 'reviews which contain less than 100 characters.')

print(new[0])
print(new[1])
