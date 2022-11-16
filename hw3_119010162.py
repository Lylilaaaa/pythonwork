import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "Korea_Data.xlsx"
df = pd.read_excel(path,index_col = 0,names = ["age","population","births","deaths"],skiprows = 1)

dfName = pd.read_excel(path,usecols=[0],names = ["name"],skiprows = 1)
ageName = np.array(dfName["name"])

femaleSize = np.array(df["population"])
births = np.array(df["births"])
deaths = np.array(df["deaths"])



birthsRate = births/femaleSize
deathsRate = deaths/femaleSize

hundredyears = np.zeros((21,len(femaleSize)))

hundredyears[0] = femaleSize

temp = 0
for n in range(1,21):
    for k in range(1,len(femaleSize)):
        temp += hundredyears[n-1][k]*birthsRate[k]
    hundredyears[n][0] = temp
    temp = 0
    for i in range(1,len(femaleSize)):
        hundredyears[n][i] = hundredyears[n-1][i-1]*(1-deathsRate[i-1])


years = [i for i in range(0,101,5)]

fig1=plt.figure(figsize=(21,21))
for col in range(0,21):
    plt.plot(years,hundredyears[:,col],marker='o',label=ageName[col])
plt.xlabel('the next 100 years')
plt.ylabel('female population size in the age range')
plt.legend()
plt.show()
plt.title('age structure of South Korea in the next 100 years')
fig1.savefig("age_structure.jpg")


sum = [i for i in range(0,21)]
temp = 0
for n in range(0,21):
    for k in range(0,21):
        temp = temp + hundredyears[n][k]
    sum[n] = temp
    temp = 0
fig2=plt.figure(figsize=(21,21))
plt.plot(years,sum,marker='o')
plt.xlabel('the next 100 years')
plt.ylabel('female population size in a year')
plt.legend()
plt.show()
plt.title('female population size of South Korea in the next 100 years')
fig2.savefig("pop_size.jpg")