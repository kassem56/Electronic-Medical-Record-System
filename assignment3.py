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








