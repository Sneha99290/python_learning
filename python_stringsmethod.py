f_name = 'sneha'
# print(f_name.upper())
updated_name = f_name.upper()
print(updated_name,f_name)
# string functions
print(f_name.capitalize())
print(f_name.islower())
print(f_name.endswith("h"))
print(f_name.isascii())
print(f_name.count('a'))
print(f_name.find('a'))
# f string
sentence = f'{f_name} is a coder'
print(sentence)
len(sentence)
# creating and printing list elements
lst = [1,2,3,4,5,'sneha',['a','b','c']]
print(lst[0])
print(lst[-1])
print(lst[-2][0])
# updating list elements
lst[0]=20
print(lst)
# sorting
numbers=[20,100,3,98,50]
numbers.sort()
print(numbers)
# reverse sorting
num=[5,67,23,1]
num.sort(reverse=True)
print(num)
# appending
numbers.append('hii')
print(numbers)
# adding list
a=[5,6,7]
b=[1,2,3]
print(a+b)
# appending two lists
a.append(b)
print(a)
# extending two lists
a.extend(b)
print(a)
# slicing of list
random_lst=[23,1,56,89,0,27,89]
print(random_lst[1:6:2])
# poping particular element
random_lst.pop(2)
print(random_lst)
# tuples
tup = (1,2,3,4,'hii')
print(tup)
# converting list to tuple
lst = [1,2,3,4]
tupl=tuple(lst)
print(tupl)
# sets
st={11,22,33,22}
print(st)
# operatins on set
bt = {24,56,78}
new=st.union(bt)
print(new)
intersect=st.intersection(bt)
print(intersect)
# u can't access elements of set through index . u have to convert it into list to access through index


# dictionaries
map_={
    'first_name':'sneha',
    'last_name':'gupta',
    'sem':'3rd'
}
print(map_['first_name'])
# if we access elements which are not present in dictionary then it will give errors so to avoid that we use .get function
print(map_.get('company','not found'))
print(map_.get('college'))
print(map_.get('sem','not found'))
# poping elements from dict
sem=map_.pop('sem')
print(sem)
print(map_)