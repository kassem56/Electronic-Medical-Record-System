import csv 

#                                                      making Physician class by defining the slots and addding the attributes
class Physician : 
    __slots__ = ['__id','__name','__specialty']         # making the attributes private by adding double _  before the attribute
    def __init__(self,id,name,specialty):
        self.__id = id
        self.__name = name
        self.__specialty = specialty









