num=input()
is_Prime=False
print('enter the number'+num)
for i in range(2,(num)/2):
    if(num%i==0):
        is_Prime=True
if(is_Prime==True):
    print('not a prime')
else:
    print('prime')