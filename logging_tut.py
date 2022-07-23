import logging
logging.basicConfig(filename="firstlog.log",level= logging.CRITICAL,format='%(levelname)s%(asctime)s %(name)s %(message)s')
logging.info("this is my first code for logginng kawai uwu")
l=[1,2,3,4,5,6,7]
for i in range(len(l)):
    if i==2:
        logging.info(l)
        logging.warning("2 found ! !")
        
        