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

# count the same word
wc = {} # word count dictionary 
print('prcessing ....')
for line in data:
	words = line.split(' ')	
	for word in words:
		if word not in wc:
			wc[word] = 1 # new added 
		else:
			wc[word] += 1
'''
for word in wc:
	print(word, wc[word])
'''
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))	

#for user to look for word
while True:
	word = input('what word are you looking for? (q to quit) ')
	if word == 'q':
		print('the end')
		break
	elif word not in wc:
		print('no such word')
	else:
		print(word,'comes out for ',wc[word],'times')



'''
#<<< get the average length>>>
avg_length = length_sum / len(data) # avarage length of the message
print('average',avg_length)



'''
#<<<<< filter the list with length >>>>>
new = []
for line in data:
	if len(line) < 100:
		new.append(line)
print('total',len(new),' messages with length <100') 
#print(new[0])

#<<<< filter the list with "good">>>>
good = []
for line in data:
	if 'good' in line:
		good.append(line)
print('total',len(good),'messages with "good"')
print(good[0])

#<<<< list comprehension >>>>
#good = [line for line in data if 'good' in line]