class Product:
    def __init__(self,name="",code=0):
        self.name=name
        self.code=code
    def pro_print(self):
        print(f'product {self.code} is {self.name}')
    
product1= Product()
product2=Product()
product1.name="codetree"
product1.code=50

name,code = input().split()
product2.name=name
product2.code = int(code)

product1.pro_print()
product2.pro_print()