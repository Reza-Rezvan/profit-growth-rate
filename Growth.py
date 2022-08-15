# profit 

from calendar import month
from pyexpat import features
import matplotlib.pyplot as plt
import pandas as pd

IN = int(input("Initial Amount "))
print("Starting With ", IN,"Toman")
print("")

mn = int(input("inter month"))
print("number of month is",mn )
print("")

per = int(input("input percent of profit"))
print("percent you want is", per,"%")
print("")

profit = int((IN * per)/ 100)
# print("your profit is",profit,"Toman from ",IN,"Toman")

total = IN
lst = []
for i in range (1,mn+1):
    # print("Now your money is",total)
    profit = (total * per)/ 100
    total = int(total + profit)
    # print("month",i,"is", total)
    lst.append(total)

    if (i % 12) == 0 :
        print("your money at the end of year",int(i/12), "is:", total, "toman")
    if (i % 60) == 0:
        t = int(total/IN) + 1
        m = int((t * 100)/60)
        
        y = int((t * 100)/5)
        print("your money after 5 year is ",str(t)+" multi" )
        print("monthly growth after 5 year: ", str(m))
        print("yearly growth after 5 year: ", y)


plt.plot(lst)
plt.title('profit!')
plt.show(lst)
  

print(lst)

def cagr(start_value, end_value, num_periods):
    return (end_value / start_value) ** (1 / (num_periods - 1)) - 1
    
print("---------------------")
result = cagr(IN, total, mn) 
print("growth rate:")
print("growth rate:{:.2%}".format(result))

print("your last money is" , lst[-1])

r = int(total / IN)
print("--------")
print("your money now is multi " + str(r))



n = int(input("number of month"))

feature = total * (1 + result) ** n
print("-----------")
print(int(feature),"Toman")


