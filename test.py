from pip import main


class person:
   
        def __init__(self,name ,surname,email,yob) -> None:
            self._name=name
            self.__surname=surname
            self.email=email
            self.yob=yob
        def age(self,cury):
            return cury-self.yob
        if __name__=="__main__":
            ck=person("chirag","kapoor","kapoor@gmail.com",2001)
            print(ck._name+' '+ck._person__surname)
            print(ck.age(2022))
