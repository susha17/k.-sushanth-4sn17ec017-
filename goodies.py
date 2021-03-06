#goodies are made as dictionaries in py code
dict1={
"Fitbit Plus": 7980,
"IPods": 22349,
"MI Band": 999,
"Cult Pass": 2799,
"Macbook Pro": 229900,
"Digital Camera": 11101,
"Alexa": 9999,
"Sandwich Toaster": 2195,
"Microwave Oven": 9800,
"Scale": 4999
}
#sorting the goodies  according to the value
sort_value=sorted(dict1.values())
sort_dict={}

for i in sort_value:
    for k in dict1.keys():
        if dict1[k]==i:
            sort_dict[k]=dict1[k]
            break
#print(sort_dict)
l=[]
values=sort_dict.values()
vallist=list(values)
#print(vallist)
user=int(input("enter the no of employees :"))
man=int(user/2)
n=len(dict1)
print("Here the goodies that are selected for distribution are:")
for z in range(man):
    diff=100000
    
    for j in range(n-1):
        for m in range(j+1,n):
            if abs(vallist[j]-vallist[m])<diff:
                diff=abs(vallist[j]-vallist[m])
                a=vallist[j]
                b=vallist[m]

    for key,value in dict1.items():
        if value==a:
            print(key,":",value)
    for key,value in dict1.items():
        if value==b:
            print(key,":",value)
            l.append(a)
            l.append(b)
    vallist.remove(a)
    vallist.remove(b)
    n=n-2

y=max(l)
c=min(l)
print()
print("And the difference between the chosen goodie with highest price and the lowest price is ",y-c)

    
