# Task 2 - DrSeuus
import re
def Generate_dictionary(path):
	""" generates a frquency dictionary from the txt file in @Path,
	words will not include special keys and upper case will be ignored"""
	list = []
	dictA = {}
	with open("drseuss/"+path,'r') as file:
		for line in file:      
			for word in line.split():         
				word = re.sub('["?.!@#$\n]', '', word.lower())
				if word in dictA.keys():
					dictA[word] += 1
				else:
					dictA[word] = 1
	return dictA

def get_Unique(a,b):
	"""returns a dictionary with all unique keys in @a"""
	res = {}
	for key in a.keys():
		if key not in b.keys() :
			res[key]  = a[key]
	return res


dictA = Generate_dictionary('cat in a hat.txt')
dictB = Generate_dictionary('green_eggs_and_ham.txt')
uniqueA = get_Unique(dictA,dictB)
uniqueB = get_Unique(dictB,dictA)
str = "cat in a hat" if len(uniqueA) > len(uniqueB) else "green_eggs_and_ham"
print(f"{str} has more unique words")
print(f"cat in a hat has {len(uniqueA)} unique words")
print(f"green_eggs_and_ham has {len(uniqueB)} unique words\n")
print(f"the unique word frequency in cat in a hat is:\n {dictA}\n")
print(f"the unique word frequency in green_eggs_and_ham is:\n {dictB}")

#  ~ ~ ~ End of TASK 2 ~ ~ ~

#for sorting dictionary according to ket ( change 0 -> to sort by value)	
#print({k: v for k, v in sorted(dictA.items(), key=lambda item: item[0])})
