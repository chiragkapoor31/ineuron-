from test2 import person
import test2
#ck=test.person("chirag","kapoor","kapoor@gmail.com",2001)
#print(ck)
#print(ck._name)
#print(ck._person__surname)
class purple:
    _name ="ginle"
    __surname='op'
    yob1=2021
    def _age(self):
        cury=int(input("enter current year"))
        print(cury-purple.yob)
    # to access parent variable --use classname.variable
    def __age1(self,cury):
        cury=int(input("enter current year"))
        print(cury-self.yob)


class leet(purple,test2.person):
    _name="choto"
    __surname="boi"
    yob=2022
    print("uwu")
ginleboi=leet()
print(ginleboi.yob2)
print(ginleboi._name1)
#print(ginleboi._purple__surname1)
#ginleboi._age()
print(ginleboi._person__surname1)

print
# when ever we use same variable first we will get from child class
