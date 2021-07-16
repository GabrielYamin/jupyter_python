import matplotlib.pyplot as plt
### ENTER SOLUTION CODE HERE
import math
import re

def simulate_covid_and_lockdown(initial, R, days, lock_day, lock_R):
    infected = [initial]
    for i in range(days):
        if i <= lock_day :
            infected.append(math.ceil(infected[-1]*R))
        else:
            infected.append(math.ceil(infected[-1]*lock_R))
    print(infected)
    x = list(range(days+1))

    plt.plot(x, infected, '-o')
    plt.title(f"Number of infected by day, based on constant R = {R}")
    plt.xlabel('# Days since {initial} persons infected')
    plt.ylabel('# of people infected')
    plt.show()

def simulate_to_end_lockdown(initial, R):
    days = 0
    while initial > 100:
        initial = math.ceil(initial*R)			
        days += 1
    print(f"Given your input parameters, {days} number of days until there are less than 100 people infected.")
    return days

def Generate_dictionary(path):
	list = []
	dictA = {}
	with open(path,'r') as file:
		for line in file:      
			for word in line.split():         
				word = re.sub('["?.!@#$\n]', '', word.lower())
				if word in dictA.keys():
					dictA[word] += 1
				else:
					dictA[word] = 1
	#print({k: v for k, v in sorted(dictA.items(), key=lambda item: item[0])})
	return dictA

def get_Unique(a,b):
	res = {}
	for key in a.keys():
		if key not in b.keys() :
			res[key]  = a[key]
	return res

dictA = Generate_dictionary('cat in a hat.txt')
dictB = Generate_dictionary('green_eggs_and_ham.txt')
#print(f"TEST: a {len(dictA)} b: {len(dictB)}")
uniqueA = get_Unique(dictA,dictB)
uniqueB = get_Unique(dictB,dictA)
str = "cat in a hat" if len(uniqueA) > len(uniqueB) else "green_eggs_and_ham"
print(f"{str} has more unique words")
print(f"cat in a hat has {len(uniqueA)} unique words")
print(f"green_eggs_and_ham has {len(uniqueB)} unique words\n")
print(f"the unique word frequency in cat in a hat is: {dictA}\n")
print(f"the unique word frequency in green_eggs_and_ham is: {dictB}")


#print(simulate_to_end_lockdown(1000, 0.9))	
#simulate_covid_and_lockdown( 10, 1.4, 30, 20, 0.6)