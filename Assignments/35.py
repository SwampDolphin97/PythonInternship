mylist = [1,2,3,"4",5]
sum = 0
for i in mylist:
	try:
		sum = sum + i
	except TypeError:
                print "Type Error"

	print sum
	try:
		print mylist[5]
	except TypeError:
                print "Type Error"
        except ValueError:
                print "Value Error"
	except IndexError:
		print "Indexing Error"
