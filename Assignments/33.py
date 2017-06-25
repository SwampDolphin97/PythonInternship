result = open("student_details.txt","r")
sentence = result.readlines()
dict = {}
list = []
i=0
all_words = map(lambda l: l.split(" "), result.readlines())
print all_words
for count in sentence:
	
	i += 1
       	list.append(count.strip())

#print(dict)
print(list)




