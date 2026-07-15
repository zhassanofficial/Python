class Employee:
    company = "Google"
    @classmethod 
    def change_company(cls,name):
        cls.company = name

E1 = Employee()
E1.change_company("youtube")
print(E1.company)

e2 = Employee()
print(e2.company)

#Notice: the company name changed for all objects, because it’s a class variable.
'''Methods that belong to the class itself, not to any specific object.
They can modify class-level data.'''