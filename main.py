from collections import OrderedDict
import time
import threading 


dict1 = OrderedDict()  #dict1 is the dictionary which will act as a datastore...

# for create operation 
# use syntax "create(key_name,value,timeout_value)"
# where timeout is optional you can continue by passing two arguments and can leave timeout...

def create(key,value,timeout=0):
    if key in dict1:
        print("error: Key already exists, please choose another key...") #error msg 1
    else:
        if(key.isalpha()):
            if (len(dict1)<(1024**3) and value<=(16*(1024**2))): 
                #constraints for file size less than 1GB and Jasonobject value less than 16KB... 
                
                if(timeout==0):     temp = [value,timeout]

                else:   temp=[value,time.time()+timeout]

                if(len(key)<=32): 
                    #constraints for input key_name at 32chars
                    dict1[key]= temp

            else:   print("error: Memory limit exceeded...! ") #error msg 2
        else:   print("error: Invalind key_name...! key_name can only contain alphabets and no special characters or numbers") #error msg 3


# for read operation one can use following syntax...
# use syntax read(key_name)
            
def read(key):
    if(key not in dict1):
        print("error: Key doesn't exist in datastore, please enter a valid key") #error message4
    else:
        temp1 = dict1[key]

        if(temp1[1]!=0):
            if(time.time()<temp1[1]): 
                #comparing the present time with expiry time
                obj = str(key)+":"+str(temp1[0]) 
                #to return the value in the format of JasonObject i.e. "key_name:value"
                # Key-Value pair
                return obj
            else:   print("error: time-to-live of",key,"has expired") #error msg 5
        else:
            obj=str(key)+":"+str(temp1[0])
            return obj

# for delete operation one can use following systax
# use syntax "delete(key_name)"

def delete(key):
    if key not in dict1:
        print("error: Key doesn't exist in datastore, please enter a valid key") #error msg 4
    else:
        temp2 = dict1[key]

        if(temp2[1]!=0):

            if(time.time()<temp2[1]): 
                
                #comparing the current time with expiry time
                del dict1[key] # deleting the key
                
                print("Key is successfully deleted...")
            else:
                
                print("error: time-to-live of",key,"has expired") #error msg 5
        else:
            del dict1[key] # deleting the key
            print("Key is successfully deleted...")

