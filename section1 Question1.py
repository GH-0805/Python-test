class salary():
    __salary=50000
    def increment(self):
        self.__salary+=5000
        print("salary increased")
    def deduct(self):
        self.__salary-=5000
        print("salary reduced")
    def get_salary(self):
        print(f"your salary is : {self.__salary}")

s=salary()
s.deduct()
s.get_salary()
