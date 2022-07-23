# syntax for creating class and it's objects
class Webseries:
    show_name = 'Suites'
    show_length = '189'
web_obj = Webseries()
print(web_obj.show_name)    
print(web_obj.show_length)

class series:
    def __init__(self,name,season,episode):
        self.name=name
        self.season=season
        self.episode=episode
        print('i am hit')
    def say_my_name(self):
        return self.name 
    def say_my_season(self):
        return f'{self.name} {self.season} {self.episode}'

s1_ = series("GoT",1,2)
s2_ = series("TVD",4,5)
print(s1_.name,s2_.name) 
episode_name=s1_.say_my_season()   
print(episode_name)
        
# inheritance
class vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color 
    def get_brand(self):
        return f'{self.brand}'   
class Car(vehicle):
    def __init__(self,brand,color,type_):
        super().__init__(brand,color)
        self.type_=type_
    def get_color(self):
        return f'this color is {self.color}' 
    def get_type(self):
        return f'this type is {self.type_}' 
sedan = Car('Toyota','Red','Sedan')
print(sedan.get_brand())
print(sedan.get_color())
print(sedan.get_type())

# write few classes for a school
class School:
    def __init__(self,school_name):
        self.school_name = school_name
    def get_Sname(self):
        return f'School name is {self.school_name}'
class Student(School):
    def __init__(self, school_name,std_name,class_,section_,roll_no):
        super().__init__(school_name)
        self.std_name = std_name
        self.class_ = class_
        self.section_ = section_
        self.roll_no = roll_no
    def std_details(self):
        return f'{self.std_name} is a student of class {self.class_} {self.section_} and has roll_no {self.roll_no}'
class Teacher(School):
    def __init__(self, school_name,t_name,subject):
        super().__init__(school_name)
        self.t_name = t_name
        self.subject = subject
    def t_details(self):
        return f'{self.t_name} teaches {self.subject} subject'


        


        