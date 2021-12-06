import csv 

#                                                      making Physician class by defining the slots and addding the attributes
class Physician : 
    __slots__ = ['__id','__name','__specialty']         # making the attributes private by adding double _  before the attribute
    def __init__(self,id,name,specialty):
        self.__id = id
        self.__name = name
        self.__specialty = specialty


    def set(self,id):                                                            # making function to give the abbility to change the private attribute
         self.__id = id
    def set(self,name):                                                          ## making function to give the abbility to change the private attribute
         self.__name = name 
    def set(self,specialty):                                                      # # making function to give the abbility to change the private attribute
        self.__specialty = specialty




    
    def get(self):                                                                # making a function to get the value of the private attribute
        return self.__id
    def get(self):                                                                  # making a function to get the value of the private attribute
        return self.__name
    def get(self):                                                                   # making a function to get the value of the private attribute
       return self.__specialty


    

    def __str__(self):                                                                  # making special method (str) to set the sentence that will be zed when you print the object
        return self.__name + ' is a '+  self.__specialty+ ' Physician with ID number ' +  self.__id  

    def __repr__(self):                                                         # making special method (repr) to set the sentence that will be printed when you print the object if the (str) method doesn't exist
        return 'Physician(id=' +self.__id + 'name=' + self.__name + '  specialty=' +  self.__specialty




                                    #making Patient class by defining the slots and addding the attributes  
class Patient :
    __slots__ = ['__emr_id','__name','__gender','__phone_number']               # making the attributes private by adding double _  before the attribute
    def __init__(self,emr_id,name,gender,phone_number):
        self.__emr_id = emr_id
        self.__name = name
        self.__gender = gender 
        self.__phone_number = phone_number
    
    def set(self,emr_id):                                    # making function to give the abbility to change the private attribute
         self.__emr_id= emr_id
    def set(self,name):                                      # making function to give the abbility to change the private attribute
         self.__name = name
    def set(self,gender):                                        # making function to give the abbility to change the private attribute
        self.__gender = gender
    def set(self,phone_number):
        self.__phone_number = phone_number

    







    def get(self):
        return self.__emr_id
    def get(self):
        return self.__name
    def get(self):
       return self.__gender
    def get(self):
        return self.__phone_number


    
