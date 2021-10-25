from hospital import*
import sqlite3 as db
import os.path
import os

emptydb = """
PRAGMA foreign_keys = ON;

create table doctor
    (id integer primary key,
    surname text,
    name text,
    patronimic text,
    spec text,
    categori integer);

create table patient
    (id integer primary key,
    surname text,
    name text,
    patronimic text,
    yearOld integer,
    categori text);


create table appeal
    (id integer primary key,
    doctor integer,
    patient integer,
    date text,
    diagnos text,
    price integer);

 """


class dataSQL:
    def __init__ (self, hosp, file_r='', file_w=""):
        self.set_hospital(hosp)
        self.setR(file_r)
        self.setW(file_w)
    def set_hospital(self,val):
        self.__hospital = val
    def setR(self,val):
        self.__file_read = val
    def setW(self,val):
        self.__file_write = val
    

    def get_hospitel(self):
        return self.__hospital
    def get_fileRead(self):
        return self.__file_read
    def get_fileWrite(self):
        return self.__file_write
    
    def read(self,file_name = ""):
        if file_name == "":
            file_name = self.get_fileRead()
        conn = db.connect(file_name)
        curs = conn.cursor()
        #doctor
        curs.execute('select id,surname,name,patronimic,spec,categori from doctor')
        data=curs.fetchall()
        for el in data:
            self.__hospital.doctor_add(doctor(el[0],el[1],el[2],
            el[3],el[4],el[5]))

        #client
        curs.execute('select id,surname, name, patronimic, yearOld, categori from patient')
        data = curs.fetchall()
        for el in data:
            self.__hospital.patient_add(patient(el[0],el[1],el[2],
            el[3],el[4],el[5]))
        
        #appeal
        curs.execute('select id,doctor,patient,date,diagnos,price from appeal')
        data = curs.fetchall()
        for el in data:
            self.__hospital.appeal_add(appeal(el[0],el[1],el[2],
            el[3],el[4],el[5]))
        conn.close()

    def write(self,file_name=""):
        if file_name == '':
            file_name = self.get_fileWrite()
        if os.path.isfile(file_name):os.remove(file_name)
        conn = db.connect(file_name)
        curs = conn.cursor()

        curs.executescript(emptydb)

        for el in self.__hospital.doctor_get():
            curs.execute("insert into doctor(id,surname,name,patronimic,spec,categori) values('%s','%s','%s','%s','%s','%s')"%(
            el.getId(),
            el.getSurname(),
            el.getName(), 
            el.getPatronimic(),
            el.getSpec(),
            el.getCategori()))
        for el in self.__hospital.patient_get():
            curs.execute("insert into patient(id,surname,name,patronimic,yearOld, categori) values('%s','%s','%s','%s','%s','%s')"%(
                el.getId(),
                el.getSurname(),
                el.getName(),
                el.getPatronimic(),
                el.getYearOld(),
                el.getCategori()))
        for el in self.__hospital.appeal_get():
            curs.execute("insert into appeal(id, doctor, patient, date, diagnos, price) values('%s','%s','%s','%s','%s','%s')"%(
                el.getId(),
                el.getDoctorId(),
                el.getPatientId(),
                el.getDate(),
                el.getDiagnos(),
                el.getPrice()))
        conn.commit()
        conn.close()