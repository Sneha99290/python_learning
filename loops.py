# # loop in list
lst=[1,2,3,4,5,6,7,8,9,10,23]
for i in lst:
    print(i)
 for i in lst[2:]:
    print(i)   
# # range     
table=range(2,21,2)
print(list(table))   
# # loop in string
for i in 'sneha':
    print(i) 
# # loop in sets
st={1,2,3}
for i in st:
    print(i)

for i in range(len(lst)):
    print(lst[i])
# # nested loops    
for i in [1,2,3]:
    for j in ['a','b','c']:
        print(i,j)
#prime number
# num=input()
# is_Prime=False
# print('enter the number'+num)
# for i in range(2,(num)/2):
#     if(num%i==0):
#        is_Prime=True
# if(is_Prime==True):
#     print('not a prime')
# else:
#     print('prime')

i=0
while i<5:
    print(i) 
    i+=1

