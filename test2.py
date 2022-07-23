class person:
    _name1 ="chirag"
    __surname1='kapoor'
    yob2=2023
    def _age(self):
        cury=int(input("enter current year"))
        print(cury-person.yob)
    # to access parent variable --use classname.variable
    def __age1(self,cury):
        cury=int(input("enter current year"))
        print(cury-self.yob)
ck=person()
print(ck._person__surname1)   