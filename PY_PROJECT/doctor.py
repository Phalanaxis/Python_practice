from general import general

class doctor(general):
    def __init__ (self,id = -1, surname="", name='', patron='', spec='', categ=0):
        general.__init__(self, id)
        self.setSurname(surname)
        self.setName(name)
        self.setPatronimic(patron)
        self.setSpec(spec)
        self.setCategoti(categ)
    
    def getSurname(self):return self.__surname
    def getName(self):return self.__name
    def getPatronimic(self):return self.__patronimic
    def getSpec(self):return self.__spec
    def getCategori(self):return self.__categori

    def setSurname(self,val):self.__surname = val
    def setName(self,val):self.__name = val
    def setPatronimic(self,val):self.__patronimic = val
    def setSpec(self,val):self.__spec = val
    def setCategoti(self,val):self.__categori = val

class DoctorList(list):
    def getById(self, id):
        for i in self:
            if i.getId() == id:
                return i
        else:
            return None
    
    