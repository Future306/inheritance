#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def sayName(self):
        print(self.name)
        
class Engineer(Person):
    def __init__(self,name):
        super().__init__(name)
        self.profession = "Engineer"
        
    def sayProfession(self):
        print(self.profession)
        
class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.profession= "Doctor"
        
    def sayProfession(self):
        print(self.profession)
        
        
engineer = Engineer("John")
doctor = Doctor("Jane")
engineer.sayName()
engineer.sayProfession()

doctor.sayName()
doctor.sayProfession()


# In[ ]:




