import requests
import json


saral_url=("https://api.merakilearn.org/courses") 

response=requests.get(saral_url)
k=response.json()
# print(response)
with open("meraki_courses.json","w") as y:
    json.dump(k,y,indent=4)
print("courses_name:")
for i in range(len(k)):
    for j,p in k[i].items():
        if j=="name":
            print(i+1,k[i]["name"],":",k[i]["id"])
# print(p)
print()
select=int(input('which course do you want to select:'))
select1=select-1
print(k[select1]["name"])
print(k[select1]["id"])

h=requests.get("https://api.merakilearn.org/courses/"+k[select1]["id"]+""+"/exercises")

edata=h.json()

with open("meraki_courses_exercise.json","w") as n:
    json.dump(edata,n,indent=4)

serial_no2=1
serial_no3=1
list1=[]
list2=[]
for j in edata["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(serial_no2,j["name"])
        print(" ",serial_no3,j["slug"])
        serial_no2+=1
        list1.append(j)
        list2.append(j)
    elif j["parent_exercise_id"]==j["id"]:
        print(serial_no2,j["name"])
        serial_no2+=1
        list1.append(j)
        new_no=1
    elif j["parent_exercise_id"]!=j["id"]:
        print(" ",new_no,j["slug"])
        new_no+=1
        list2.append(j)
u1=input("what do you want previous or next(n/p):")
if u1=="p":
    print("courses_name:")
    for i in range(len(k)):
        for j,p in k[i].items():
            if j=="name":
                print(i+1,p,k[i]["id"])
# print(p)
    print()
    select=int(input('which course do you want to select:'))
    select1=select-1
    print(k[select1]["name"])
    print(k[select1]["id"])

    h=requests.get("https://api.merakilearn.org/courses/"+k[select1]["id"]+""+"/exercises")
     
    edata=h.json()

    with open("meraki_courses_exercises.json","w") as n:
        json.dump(edata,n,indent=4) 
    
    serial_no2=1
    serial_no3=1
    list1=[]
    list2=[]
    for j in edata["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_no2,j["name"])
            print(" ",serial_no3,j["slug"])
            serial_no2+=1
            # new_no=1
            list1.append(j)
            list2.append(j)
        elif j["parent_exercise_id"]==j["id"]:
            print(serial_no2,j["name"])
            serial_no2+=1
            list1.append(j)
            new_no=1
        elif j["parent_exercise_id"]!=j["id"]:
            print(" ",serial_no3,j["slug"])
            new_no+=1
            list2.append(j)

with open ("list1.json","w") as f:
    json.dump(list1,f,indent=4)
with open("list2.json","w") as f:
    json.dump(list2,f,indent=4)
print()
parent=int(input("Enter the  parent exercise what do you want to do:"))
for g in list1:
    if g["parent_exercise_id"]==g["id"]:
        print(list1[parent-1]["name"])
        break

num=(list1[parent-1]["id"])
var=[]
var3=[]
new_no1=1
for n in list2:
    if n["parent_exercise_id"]==num:
        print(" ",new_no1,n["name"])
        var.append(n["name"])
        var3.append(n["content"])
        new_no1+=1
with open ("list1.json","w") as f:
    json.dump(list1,f,indent=4)

with open("list2.json","w") as f:
    json.dump(list2,f,indent=4)

u2=input("dou want to choose parent exercise again, select previous or next(n/p):")
if u2=="p":
    parent=int(input("enter from parent exerscise what do you want to do:"))
    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
                print(list1[parent-1]["name"])
                num=(list1[parent-1]["id"])
                break
    num=(list1[parent-1]["id"])
    var=[]
    var3=[]
    new_no1=1
    for n in list2:
        if n["parent_exercise_id"]==num:
            print(" ",new_no1,n["name"])
            var.append(n["name"])
            var3.append(n["content"])
            new_no1+=1
    print()
    child=int(input('enter the child exercise what do you want to do:'))
    for s in range (len(var)):
        if (child-1)==s:
            print(var[s])
            print(var3[s])
else:
    child=int(input('enter the child exercise again privious or next(n/p):'))
    for s in range (len(var)):
        if (child-1)==s:
            print(var[s])
            print(var3[s])

u3=input('do you want to choose child exercise again,privious or next(n/p):')
if u3=='p': 
    var=[]
    var3=[]
    new_no1=1
    for n in list2:
        if n["parent_exercise_id"]==num:
            print(" ",new_no1,n["name"])
            var.append(n["name"])
            var3.append(n["content"])
            new_no1+=1
    child=int(input('enter the child exercise what do yuo want to do:'))
    for s in range (len(var)):
        if (child-1)==s:
            print(var[s])
            print(var3[s])                   
