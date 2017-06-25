def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]

str = raw_input("Enter a string:")
revstr=rreverse(str)
print revstr
