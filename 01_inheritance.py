class employee:
    company = "Google"
    def show(self):
        print(f" Employee is working in {self.company} company")
class programmer:
    Designation = "AI engineer"
    def showdetails(self):
        print(f"programmer designation is  {self.Designation} ")
    @staticmethod
    def stat():
        print("Static method of programmer class")
class cooder(employee,programmer):
    language = "python"
    def showlanguage(self):
        print(f'''person is working in {self.company} , Designation are {self.Designation} and 
            expert in {self.language} language''')
p = cooder()
p.showlanguage()
p.stat()