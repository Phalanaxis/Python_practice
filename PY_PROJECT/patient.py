from general import general

class patient(general):
    def __init__(self,id =-1, surname='', name='', patron='', yearOld = -1, categoris = ''):
        general.__init__(self, id)
        self.setSurname(surname)
        self.setName(name)
        self.setPatronimic(patron)
        self.setYearOld(yearOld)
        self.setCategoti(categoris)

    def setSurname(self, value):self.__surname = value
    def setName(self, value):self.__name = value
    def setPatronimic(self, value):self.__patronimic = value
    def setYearOld(self, value):self.__yearOld = value
    def setCategoti(self, value):self.__categori = value
    
    def getSurname(self):return self.__surname
    def getName(self):return self.__name
    def getPatronimic(self):return self.__patronimic
    def getYearOld(self):return self.__yearOld
    def getCategori(self):return self.__categori
    
class PatientList(list):
    def getById(self, id):
        for i in self:
            if i.getId() == id:
                return i
        else:
            return None