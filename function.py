


def greet():
    print('hello world')
    # return 'hi  mars'
greet()
var=greet()
print(var)

# factorial using function
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
fact_of_5 = factorial(5)
fact_of_10 = factorial(10)
print(fact_of_5)
print(fact_of_10)  

# print table using function
def table(n):
    for i in range(1,11):
        print(n*i)
table(5)        

# return a list of 3 elements
info=[]
def list3():
    for i in range(0,3):
        element = input('enter an element')
        info.append(element)
    return info 
data = list3()
print(data)

# create a function which takes string as parameter and return true if all characters of string are capitals and otherwise false
def capital():
    el = input('enter a value')
    if el.isupper():
        return True
    else:
        return False
cap = capital()
print(cap) 
# easy way           
# def is_string_upper(string):
#     return string.isupper()


# return the sum of ascii value of caracters of string
def sum_of_ascii(string):
    total=0
    for i in string:
        total=total+ord(i)
    return total
c = sum_of_ascii('mananya')
print(c)        
# using map function
# def sum_ascii(string):
#     return sum(map(ord,string))

# map function takes a function and an iterator which will result  in a list whose elements are function acting on iterators


# create a function taking  username and password a sinput and return first 4 char of username + last 4 char of password
def sum_of_uname_pass(username,password):
    val = username[0:4]+password[-4:]
    return val
sum_ = sum_of_uname_pass('snehagupta','12acb4')
print(sum_)    


def count_consequent(string):
    string = string.lower()
    count_=0
    for i in range(len(string)-1):
       
        
        if ord(string[i]) == ord(string[i+1])-1:
            count_+=1
    return count_
result = count_consequent('abcfde') 
print(result)   



lst_=[20,35,68,98,21]
def even_(lst_):
    for i in lst_[0:]:
        if i%2==0:
            print(i)
print(even_(lst_))

        


