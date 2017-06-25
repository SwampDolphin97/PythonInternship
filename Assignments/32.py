result = open("courses.txt","r")
sentence = result.readlines()
dict = {}
list = []
i=0
for count in sentence:
	dict[i] = count.strip()
	list.append(count.strip())
	i=i+1
print(dict)
print(list)
