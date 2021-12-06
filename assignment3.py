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


                                        # making special method (str) to set the sentence that will be printed when you print the object
    def __str__(self):
        return ' patient name: ' + self.__name + ' with EMR ID: ' + self.__emr_id + ' gender of patient: ' + self.__gender + ' phone number :' + self.__phone_number 



                            # making special method (repr) to set the sentence that will be printed when you print the object if the (str) method doesn't exist
    def __repr__(self):
            return 'Patient(id= '+ self.__emr_id+ ' name= '+ self.__name + ' gender= ' + self.__gender + ' phone_number= ' + self.__phone_number



 #making Encounter class by defining the slots and addding the attributes  
class Encounter:
    __slots__ = ['physician' , 'patient' ,'date', 'disease', 'medication']                      # adding the attributes to the slots

    def __init__(self,physician, patient, date, disease, medication):
        self.physician = physician
        self.patient = patient
        self.date = date
        self.disease = disease
        self.medication = medication

    def __str__(self):
        return '' + str(self.physician) + '  ' + str(self.patient) + '  ' +  str(self.date) + '  ' + str(self.disease) + '  ' + str(self.medication) + ''

    def __repr__(self):
                return self.physician , self.patient ,  self.date, self.disease , self.medication


def main():
                                                    # opening and reading the csv file that contains the info of the patients and put each patient in a list
            with open("professor_work\patients.csv") as pp: 
                    reader = csv.reader(pp)
                    row = list(reader)

                    patient1         = row[1]
                    patient2         = row[2]
                    patient3         = row[3]
                    patient4         = row[4]
                    patient5         = row[5]
                    patient6         = row[6]
                    patient7         = row[7]
                    patient8         = row[8]
                    patient9         = row[9]
                    patient10        = row[10]

                                        #making a list to add all the patients to the list then print them

                    patientss= []
                    for rows in row:
                        patientss.append(rows)
                    
                    


                        # defining an object of class Pateint for each pateint from csv file by the list 
                    
                    Patient1_  = Patient(patient1[0],patient1[1],patient1[2],patient1[3])
                    Patient2_  = Patient(patient2[0],patient2[1],patient2[2],patient2[3])
                    Patient3_  = Patient(patient3[0],patient3[1],patient3[2],patient3[3])
                    Patient4_  = Patient(patient4[0],patient4[1],patient4[2],patient4[3])
                    Patient5_  = Patient(patient5[0],patient5[1],patient5[2],patient5[3])
                    Patient6_  = Patient(patient6[0],patient6[1],patient6[2],patient6[3])
                    Patient7_  = Patient(patient7[0],patient7[1],patient7[2],patient7[3])
                    Patient8_  = Patient(patient8[0],patient8[1],patient8[2],patient8[3])
                    Patient9_  = Patient(patient9[0],patient9[1],patient9[2],patient9[3])
                    Patient10_ = Patient(patient10[0],patient10[1],patient10[2],patient10[3])

  
    
