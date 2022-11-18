import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "Korea_Data.xlsx"
df = pd.read_excel(path,index_col = 0,names = ["age","population","births","deaths"],skiprows = 1)

dfName = pd.read_excel(path,usecols=[0],names = ["name"],skiprows = 1)
ageName = np.array(dfName["name"])

femaleSize = np.array(df["population"])
femaleSize5 = np.array(df["population"])
femaleSize5 = femaleSize5//5
#print(femaleSize5)
femaleSize100 = np.array([femaleSize5[0],femaleSize5[0],femaleSize5[0],femaleSize5[0],femaleSize5[0]])
for j in range(1,len(femaleSize)):
    femaleSize100 = np.append(femaleSize100, [femaleSize5[j],femaleSize5[j],femaleSize5[j],femaleSize5[j],femaleSize5[j]])
#print(femaleSize100)
births = np.array(df["births"])
deaths = np.array(df["deaths"])

birthsRate = births/femaleSize
deathsRate = deaths/femaleSize

birthsRate100 = np.array([birthsRate[0],birthsRate[0],birthsRate[0],birthsRate[0],birthsRate[0]])
for j in range(1,len(birthsRate)):
    birthsRate100 = np.append(birthsRate100, [birthsRate[j],birthsRate[j],birthsRate[j],birthsRate[j],birthsRate[j]])

deathsRate100 = np.array([deathsRate[0],deathsRate[0],deathsRate[0],deathsRate[0],deathsRate[0]])
for j in range(1,len(deathsRate)):
    deathsRate100 = np.append(deathsRate100, [deathsRate[j],deathsRate[j],deathsRate[j],deathsRate[j],deathsRate[j]])

hundredyears = np.zeros((101,len(femaleSize100)))

hundredyears[0] = femaleSize100

temp = 0
for year in range(1,101):
    for age in range(1,len(femaleSize100)):
        temp += hundredyears[year-1][age]*birthsRate100[age]
    hundredyears[year][0] = temp
    temp = 0
    for age in range(1,len(femaleSize100)):
        hundredyears[year][age] = hundredyears[year-1][age-1]*(1-deathsRate100[age-1])

hundredyears20 = np.zeros((101,len(femaleSize)))
for year in range(0,101):
    for age in range(0,len(femaleSize)):
        hundredyears20[year][age] = hundredyears[year][age*5]+hundredyears[year][age*5+1]+hundredyears[year][age*5+2]+hundredyears[year][age*5+3]+hundredyears[year][age*5+4]


years = [i for i in range(0,101)]

fig1=plt.figure(figsize=(21,21))
for col in range(0,21):
    plt.plot(years,hundredyears20[:,col],marker='o',label=ageName[col])
plt.xlabel('the next 100 years')
plt.ylabel('female population size in the age range')
plt.legend()
plt.show()
#plt.title('age structure of South Korea in the next 100 years')
fig1.savefig("age_structure.jpg")


sum = [i for i in range(0,101)]
temp = 0
for n in range(0,101):
    for k in range(0,21):
        temp = temp + hundredyears20[n][k]
    sum[n] = temp
    temp = 0
print(sum)
fig2=plt.figure(figsize=(21,21))
plt.plot(years,sum,marker='o')
plt.xlabel('the next 100 years')
plt.ylabel('female population size in a year')
plt.legend()
plt.show()
#plt.title('female population size of South Korea in the next 100 years')
fig2.savefig("pop_size.jpg")