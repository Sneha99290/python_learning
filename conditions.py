f_name='darsh'
l_name='gupta'

if f_name=='sneha':
    print('yes')
else:
    print('no')    

if f_name=='darsh' and l_name=='gupta':
    print('name is darsh gupta')
else:
    print('name is not darsh gupta')    

if f_name=='darsh' and  not l_name=='sharma':
    print('name is darsh gupta')
else:
    print('name is not darsh gupta')     

if 'sneha' in ['a','b','c']:
    print('sneha is in list')
elif 'p'in 'sneha':
    print('sneha has p in spelling')
elif 'k' in 'aakash':
    print('aakash has k in spelling')
else:
    print('false')         


name=input('enter the string')
for i in name:
    if ord(i)%2==0:
        print('even')
    else:
        print('odd')    
# take an integer input from user nd take n more more inputs and append these inputs into a list
num = input('enter a number')
a_list=[]
a=int(num)
for i in range(0,a):
    n = input()
    a_list.append(n)
print(a_list)    

# take an integer as input
num=input('enter a number')
num=int(num)
info={
    'str': [],
    'int': []
}

for i in range(0,num):
    datatype=input('enter datatype')
    values=input('enter value')
    if datatype=='str':
        info['str'].append(values) 
    elif datatype=='int':
        info['int'].append(values)     
    # else:
    #     print('please initialise an empty list for{datatype}'.format(datatype=datatype))
    else:
        info.update(datatype=[])
        info[datatype].append(values)
print(info)