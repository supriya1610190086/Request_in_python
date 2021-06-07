import requests
import json

parent_api="http://join.navgurukul.org/api/partners"
parentes_url=requests.get(parent_api)
parentes_data=parentes_url.json()
with open("parentes_of_navgurukul.json","w") as parentes:
    json.dump(parentes_data,parentes,indent = 4)
list=[]
dict={}
for i in parentes_data["data"]:
    data1=i['id']
    dict[data1]=i['name']
    list.append(i['name'])
def Asending_decending():
    Asending_decending_order=input("A means Asending and D means Desending")
    if Asending_decending_order=="a":
        for i in sorted(dict):
            print(i,dict[i])
    elif Asending_decending_order=="d":
        for k in sorted(dict,reverse=True):
            print(k,dict[k])
    else:
        print("Invalid")
Asending_decending()