from general import general

class appeal(general):
    def __init__ (self, id = -1, doctorId = -1, patientId = -1, date = '',diagnosis = '', price = 0):
        general.__init__(self, id)
        self.setDoctor(doctorId)
        self.setPatient(patientId)
        self.setDate(date)
        self.setDiagnos(diagnosis)
        self.setPrice(price)
    
    def getDoctorId(self):return self.__doctorId
    def getPatientId(self):return self.__patientId
    def getDate(self):return self.__date
    def getDiagnos(self):return self.__diagnos
    def getPrice(self):return self.__price 
    
    def setDoctor(self,val):self.__doctorId = val
    def setPatient(self,val):self.__patientId = val
    def setDate(self,val):self.__date = val
    def setDiagnos(self,val):self.__diagnos = val
    def setPrice(self,val):self.__price = val

class AppealList(list):
    def getById(self, id):
        for i in self:
            if i.getId() == id:
                return i 
        else:
            return None
