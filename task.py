import logging

from pyrsistent import l
logging.basicConfig(filename="task.log",level=logging.INFO)
class tasks:
    l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    
    def reverse(self):
        a=[]
        try:
            logging.info("we are going to reverse list")
            a=self.l[::-1]
            print(a)
            logging.info("reverse list")
        except Exception as e:
            logging.info("oops",e)
    
    def access(self):
        try:
            c=[]
            logging.info("we are going to access 234")
            print(self.l[7][0])
            a=str(l)
            for i in range(len(a)):
                if a[i]==234:
                    logging.info(i,"found",a[i])
            
            logging.info("found 234")
        except Exception as e:
            logging.info("not able to find",e)
    def exlist(self):
        try:
            b=[]
            logging.info("we are going to get lists from l")
            for  i in self.l:
                if type(i)==list:
                    b.append(i)
            print(b)
            logging.info("list from l found")
        except Exception as e:
            logging.info("lists not found",e)
                   
            
    

t=tasks()
print(t.reverse())
print(t.access())        
print(t.exlist())    
        