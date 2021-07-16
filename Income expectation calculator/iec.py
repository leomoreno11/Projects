import numpy as np
import pandas as pd

amount = float(input('Whats the amount you want to invest ?\n'))
rate = float(input('Whats the growth rate percentage of your investment ?\n'))
months = int(input('For how many months ?\n'))
contribution = float(input('There will be a monthly contribution?\n'))

#testing parameters
#amount  = 16340.25
#rate    = 0.34
#months  = 12
#contribution  = 1233.18

print('-'* 101 + '\nYou plan to invest ' + str(amount) + ' at a ' + str(rate) + '% per month, for ' + str(months) +  ' months and with a ' + str(contribution) + ' monthly contribution\n'
         + '-'* 101)

rate = rate / 100

def investiment(amount, rate, months, contribution):
    results     = []
    profits     = []
    contributions = []
    profitsSum  = []
    contributionSum = []
    i = 0
    j = 0
    x = 0
    c = []

    while j < months:
        contributions.append(contribution)
        j+=1

    while i < months:
        profit = (amount * rate)
        finalAmount = profit + amount
        a = round(finalAmount, 2)
        c.insert(i, 1)
        monthSum = np.cumsum(c)
        results.insert(i, a)
        profits.insert(i, round(profit, 2))
        # print(contributionSum)
        contributionSum   = np.round(np.cumsum(contributions), decimals = 2)
        profitsSum  = np.round(np.cumsum(profits), decimals = 2)
        
        amount = a + contribution
        i += 1

    
    df = pd.DataFrame({'Month': monthSum, 'Result': results, 'Profit' : profits, 'Total Profits' : profitsSum, 'Total Contributions' : contributionSum})
    print(df.to_string(index=False))


investiment(amount, rate, months, contribution)
