#1
result = open("file1.txt","r")
sentence = result.read()
result.close()
#2
result = open("file2.txt","w")
for count in sentence:
	if(count==" "):
		result.write(count+"\\")
	else:
		result.write(count)
result.close()

#3
result = open("file1.txt","r")
sentence = result.read()
print sentence
result = open("file2.txt","r")
sentence = result.read()
print sentence

