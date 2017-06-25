#1
try:
	result = open("file1.txt","r")
except (FileNotFoundError, IOError):
        print("Wrong file or file path")
sentence = result.read()
result.close()
#2
try:
	result = open("file2.txt","w")
except (FileNotFoundError, IOError):
        print("Wrong file or file path")
for count in sentence:
	if(count==" "):
		result.write(count+"\\")
	else:
		result.write(count)
result.close()

#3
try:
	result = open("file1.txt","r")
except (FileNotFoundError, IOError):
        print("Wrong file or file path")
sentence = result.read()
print sentence
try:
	result = open("file2.txt","r")
except (FileNotFoundError, IOError):
        print("Wrong file or file path")
sentence = result.read()
print sentence
