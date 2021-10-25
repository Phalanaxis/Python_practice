from hospital import *
from dataJson import*
from dataSql import* 
hos = hospital()
jorj = patient(1,"Smirnov","Artyom","Vsevolodovich",19,"student")
hos.patient_add(jorj)
doc = doctor(2,"Gromova","Daryia","Olegovna","therapist",3)
hos.doctor_add(doc)
ap = appeal(1,1,1,"22.02.2019","covid-19",100)
hos.appeal_add(ap)

js = datajs(hos,"","")
js.write("js.json")

hos.empter()

js = datajs(hos,"","")
js.write("js.json")

js.read("js.json")
js.write("js1.json")

sql1 = dataSQL(hos,"","")
sql1.write("dd.sqlite")
hos.empter()
sql1.read("dd.sqlite")
js.write("js2.json")

