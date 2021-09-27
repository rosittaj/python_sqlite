import sqlite3
connection=sqlite3.connect("hospital_doctor_db")
cursor=connection.cursor()
#cursor.execute("create table Hospital(Hospital_Id INTEGER PRIMARY KEY AUTOINCREMENT,Hospital_Name varchar(50),Bed_Count varchar(30))")
#cursor.execute("create table Doctors(Doctor_Id INTEGER PRIMARY KEY AUTOINCREMENT,Doctor_Name varchar(50),Hospital_Id INTEGER,Joining_Date date,Speciality varchar(50),Salary numeric(0),Experience numeric(0),FOREIGN KEY(Hospital_Id) REFERENCES Hospital(Hospital_Id))")
request=input('Do you want to add new hospital (y/n) ?')
if request=='y'or request=='yes':
    Hospital_Name=input('Hospital name :')
    Bed_Count=input('bed count :')
    cursor.execute("insert into Hospital (Hospital_Name,Bed_Count) values(?,?)",(Hospital_Name,Bed_Count))
    connection.commit()
    print("data enterd successfully. ")
else:
    pass
request=input('Do you want to add new doctor (y/n) ?')
if request=='y'or request=='yes':
    Doctor_Name=input('Doctor_Name :')
    Hospital_Id=input('Hospital_Id :')
    Joining_Date=input('Joining_Date :')
    Speciality=input('Speciality :')
    Salary=input('Salary :')
    Experience=input('Experience :')
    cursor.execute("insert into Doctors (Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) values(?,?,?,?,?,?)",(Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience))
    connection.commit()
    print("data enterd successfully. ")
else:
    pass
print("Doctor details based on Speciality and Salary ")
Speciality=input('Speciality :')
Salary=input('Salary :')
cursor.execute("select *  from Doctors WHERE  Speciality='%s' and Salary>=%s " %(Speciality,Salary))
result=cursor.fetchall()
for i in result:
    print(i)
else:
    print("No doctors avilable in given data! \n")
print("Doctor details and hospital name based on Hospital Id ")
Hospital_Id=int(input('Hospital Id : '))
cursor.execute("select Doctors.Doctor_Name,Hospital.Hospital_Name from Doctors INNER JOIN Hospital ON Doctors.Hospital_Id=Hospital.Hospital_Id WHERE  Doctors.Hospital_Id=%s" %(Hospital_Id))
result=cursor.fetchall()
for i in result:
    print(i)
else:
    print("No Hospital avilable in given data! \n")
connection.close()
