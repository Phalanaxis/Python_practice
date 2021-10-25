from hospital import*
import json
import os.path


class datajs:
    def __init__(self, hosp, file_r='', file_w=""):
        self.set_hospital(hosp)
        self.setR(file_r)
        self.setW(file_w)

    def set_hospital(self, val):self.__hospital = val
    def setR(self, val):self.__file_read = val
    def setW(self, val):self.__file_write = val
    def get_hospitel(self, val):return self.__hospital
    def get_fileRead(self, val):return self.__file_read
    def get_fileWrite(self, val):return self.__file_write

    def read(self, file_name=""):
        path = True
        if file_name == "":
            if self.__file_read == "":
                path = False
            else:
                file_name = self.__file_read
        if path:
            with open(file_name) as read_file:
                data = json.load(read_file)
            for el in data["patient"]:
                patien = patient(el["id"], el["surname"], el["name"],
                                 el["patronimic"], el["yearOld"], el["categori"])
                self.__hospital.patient_add(patien)

            for el in data["doctor"]:
                doctorr = doctor(el["id"], el["surname"], el["name"],
                                el["patronimic"], el["spec"], el["categori"])
                self.__hospital.doctor_add(doctorr)
            for el in data["appeal"]:
                appeall = appeal(el["id"], el["doctor"], el["patient"],
                                el["date"], el["diagnos"], el["price"])
                self.__hospital.appeal_add(appeall)

    def write(self, file_name=''):
        path = True
        if file_name == "":
            if self.__file_write == "":
                path = False
            else:
                file_name = self.__file_write
        if path:
            data = {}
            data["patient"] = []
            for el in self.__hospital.patient_get():
                val = {"id": el.getId(),
                       "surname": el.getSurname(),
                       "name": el.getName(),
                       "patronimic": el.getPatronimic(),
                       "yearOld": el.getYearOld(),
                       "categori": el.getCategori()}
                data["patient"].append(val)

            data["doctor"] = []
            for el in self.__hospital.doctor_get():
                val = {"id" : el.getId(),
                       "surname": el.getSurname(),
                       "name": el.getName(),
                       "patronimic": el.getPatronimic(),
                       "spec": el.getSpec(),
                       "categori": el.getCategori()}
                data["doctor"].append(val)

            data["appeal"] = []
            for el in self.__hospital.appeal_get():
                val = {"id": el.getId(),
                       "doctor": el.getDoctorId(),
                       "patient":el.getPatientId(),
                       "date": el.getDate(),
                       "diagnos": el.getDiagnos(),
                       "price": el.getPrice()}
                data["appeal"].append(val)
        with open(file_name, 'w') as write_file:
            json.dump(data, write_file, indent=3)
