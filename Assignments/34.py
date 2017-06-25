result = open("rhyme.txt","r")
sentence = result.read()
i = 0
for count in sentence:
	if(count == " "):
		i+=1
print i
