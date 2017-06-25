my_string = """Strings are amongst the most popular data types in Python . We can create the strings by enclosing characters in quotes . Python treats single quotes the same as double quotes ."""

sub = "String"
print("Number of times String ocuur:" , my_string.count(sub))
count_words = 0
str1 = my_string.split()

for word in str1:
    a = word.endswith("on")
    if a == True:
        count_words += 1
    b =word.endswith("on" , 0 , len(word))
    if b == True:
        count_words += 1
print(count_words)
