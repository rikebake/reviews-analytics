data = []
count = 0
length_sum = 0 #to sum the length
with open('reviews.txt','r') as file:
	for line in file:
		data.append(line)
		count += 1 #count = count + 1

		length_sum += len(line) # length_sum + len(line)
		if count % 1000 == 0:  # % is to get the remain (餘數), print the progress every 1k message
			print(len(data)) # to show the progress but "print" takes resouce so it will take time to read the file
print('total',len(data), 'message','file loaded completed')
print(data[0]) # print the 1st line
avg_length = length_sum / len(data) # avarage length of the message
print('average',avg_length)

#<<<<< filter the list with length >>>>>
new = []
for line in data:
	if len(line) < 100:
		new.append(line)
print('total',len(new),' messages with length <100') 
#print(new[0])