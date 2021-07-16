import matplotlib.pyplot as plt
### ENTER SOLUTION CODE HERE
import math
import re

# TaskA
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

# TaskB
def simulate_to_end_lockdown(initial, R):
    days = 0
    while initial > 100:
        initial = math.ceil(initial*R)			
        days += 1
    print(f"Given your input parameters, {days} number of days until there are less than 100 people infected.")
    return days
# ~~~~~~~~~~~~~~ END of solution ~~~~~~~~~~~~
# MAIN for testing
def main():
    print(simulate_to_end_lockdown(1000, 0.9))	
    print(simulate_covid_and_lockdown( 10, 1.4, 30, 20, 0.6))

main()