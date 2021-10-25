from general import general
from patient import*
from doctor import*
from appeal import*

class hospital(general):
    def __init__ (self, id=-1):
        general.__init__(self, id)
        self.__patientList = PatientList()
        self.__doctorList = DoctorList()
        self.__appealList = AppealList()
        self.__categorisList = []
   
    
    def empter(self):
        self.__patientList = PatientList()
        self.__doctorList = DoctorList()
        self.__appealList = AppealList()

    def patient_add(self,val):self.__patientList.append(val)
    def doctor_add(self,val):self.__doctorList.append(val)
    def appeal_add(self,val):self.__appealList.append(val)

    def patient_get(self):return self.__patientList
    def doctor_get(self):return self.__doctorList
    def appeal_get(self):return self.__appealList

    def get_categori(self):return self.__categorisList
    def addCategor(self, val):self.__categorisList.append(val)
        

    
