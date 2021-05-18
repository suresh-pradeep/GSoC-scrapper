from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

names=[]
org=[]
pro=[]
i=1
for i in range(1,27):
    URL = requests.get("https://summerofcode.withgoogle.com/api/program/current/project/?page="+str(i)+"&page_size=50")
    soup = BeautifulSoup(URL.text,'html5lib')
    body=str(soup('body'))
    list=re.split(r":|,",body)
    flag=0
    for string in list:
        if((flag>0)&(flag<4)):
            if(flag==1):
                names.append(string[1:-1])
            elif(flag==2):
                org.append(string[1:-1])
            else:
                pro.append(string[1:-1])
            flag=0
        elif(re.search('"display_name"',string)):
            flag=1
        elif(re.search('"name"$',string)):
            flag=2
        elif(re.search('"title"$',string)):
            flag=3
        i=i+1  
dict = {'Name': names, 'Organization': org, 'Project': pro}
df = pd.DataFrame(dict)
df.to_csv('gsoc2021.csv')

        
