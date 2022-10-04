import pyphox
import time
host = ['192.168.1.4:8080','192.168.1.4:8080' ]
# print the HTTP request in the console
for i in host:
    # create a new instance of the class
    phox = pyphox.connect(i)
    # start the experiment
    phox.start()
    # wait for 10 seconds
    time.sleep(10)
    # stop the experiment
    phox.stop()
    # export the data to excel
    phox.export('excel')
    # export the data to csv
 
    phox.clear()
    # close the connection