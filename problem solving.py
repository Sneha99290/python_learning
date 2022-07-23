# print the data of a file as a set in dictionary

# file = open('random text.txt','r')

# def file_lst(file):
#     data = file.readlines()
#     dic_={}
    
#     for i in data:
        
#         data_=i.split()        
#         print(data_[0])
#         if data_[0] in dic_:
#             dic_[data_[0]].add(data_[1]) #error--> dic_[data_[0]].add(data_[1:]) ---can't add list in a set
#         else:
#             dic_[data_[0]]={data_[1]}
#     return(dic_)

# info=file_lst(file)
# print(info)    

# to get which word has occured most frequently in a file
file = open('article.txt','r')

count_={}
def freq(file):
    data = file.read()
    splitted_data=data.split()
    for i in splitted_data:
        if i in count_:
            count_[i]+=1
        else:
            count_[i] = 1
    return(count_)
dictionary_=freq(file)   
print(dictionary_) 
new_file = open('details.txt','w')
for key,value in dictionary_.items():
    str_ = f'{key} {value}'
    new_file.write(str_+'\n')

# to check whether a table of number is present in given file or not
demo_file = open('table.txt','r')
def table_(demo_file,n):
    num_=demo_file.readlines()
    
    for i in num_:
        if i%n==0:
            return True
        else:
            return False
check_=table_(demo_file,2)  
print(check_)  




