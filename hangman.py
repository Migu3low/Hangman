word =  {0:"M", 1:"A", 2:"S", 3:"T", 4:"I", 5:"L"}
letter =  "S"
dict = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"L"}
key = 0
for x in word.values():
  if x in letter:
	    dict[key] = x
	    key += 1
  else:
	    key += 1
	
	
print(dict)
