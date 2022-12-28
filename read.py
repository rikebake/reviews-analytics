data = []
count = 0
with open('reviews.txt','r') as file:
	for line in file:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0:  # % is to get the remain (餘數), print the progress every 1k message
			print(len(data)) # to show the progress but "print" takes resouce so it will take time to read the file
print(len(data))
print(data[0]) # print the 1st line