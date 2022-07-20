# take a string as input and count the number of times a characters in string nd store this data as 

name = input('enter a string')
new=name.lower()
map_={}
for i in new:
    freq=new.count(i)
    map_[i]=freq
print(map_)    

# name = input('enter a string')
# new=name.lower()
# map_={}
# for i in new:
#     if i in map_:
    #     map_[i]+=1
    # else:
    #     map_[i]=1
# print(map_)


# take inputs from user like pop or push for a number in a list and print th list every time any input is taken. and break the operation when user enter stop as input

list_=[]
while True:
    value = input('enter operation and the value')
    value = value.split()
    print(value)
    if(value[0]=='push'):
        list_.append(value[1])
    elif(value[0]=='pop'):
        list_.remove(value[1])   
    elif(value[0]=='stop'):
        break
print(list_)     


##
dic_={}
while True:
    info = input('enter subject and names')
    info = info.split()
    print(info)
    if info[0]=='stop':
        break
    else:
        if info[0] in dic_:
            dic_[info[0]].add(info[1:])
        else:
            dic_[info[0]]={info[1]}
print(dic_)            
                
