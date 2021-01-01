#This are the inputs to explain, how to perform operations on a mail file...

import threading    # For multi-threading purpose
import main as m    # importing the main file as a library that act as a data-store... 

m.create("execution",25)
m.create("Test",50)
m.create("Demo",70)
m.create("example",100) 
# To create a key with name of the key,value given and with no time-to-live property...


m.create("source",70,3600) 
#to create a key with name of the key,value given and with time-to-live property value given(in number of seconds)


m.read("execution")
# it returns the value of desired key in Jasonobject format 'key_name:value'm

m.read("Demo")
# it returns the value of desired key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


m.create("Test",150)
#it returns an ERROR since the name of the key already exists in the datastore...

# If we want to create this key again with some other value then delete this key using
# delete operation and then recreate it...


m.delete("execution") #it deletes the respective key and its value from the datastore...

#we can access these using multiple threads like

t1=threading.Thread(target=(m.create or m.read or m.delete),args=("Test",50,10)) #as per the operation
t1.start()
t2=threading.Thread(target=(m.create or m.read or m.delete),args=("execution",60,20)) #as per the operation
t2.start()



# Following Errors and Exceptions are also handled by the main code...

# if key_length is greater than 32 or key_name contains any numeric,
# special characters etc... then "Invalid_Key" error will be raised
# if key_name was mis-spelt or deleted then "Key does not exists" error will be raised... 
# if file memory exceeds 1GB then "File memory limit reached" error will be raised...

