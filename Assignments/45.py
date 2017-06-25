import re
cust_details = "Hello John, your customer id is j181"
matched = re.search("Hello\s" or "hello\s", cust_details) 
print(matched.group())
matched = re.search("\D{1}\d{3}$",cust_details)
print(matched.group())
print(re.sub(r"j",r"",cust_details))
print(re.sub(r"id is j",r"ID is ",cust_details))

