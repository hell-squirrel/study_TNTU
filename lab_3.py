__author__ = 'Hulka Yuriy'

import sys
class Student():
    #define initialization
    def __init__(self):
        self.studentName='None'
        self.studentAge=18
        self.studentSchool='None'
    #class methods
    def setSchool(self,school):
        if type(school)!=str:print("Incorreect school value!"),sys.exit()
        self.studentSchool=school
    def setName(self,name):
        if type(name)!=str:print("Incorreect name value!"),sys.exit()
        self.studentName=name
    def setAge(self,age):
        if type(age)!=int:print("Incorreect age value!"),sys.exit()
        self.studentAge=age
    def getAge(self):
        return self.studentAge
    def getAllInfo(self):
        return ("Student name is: %s\nStudent age is: %s \nStudent HighSchool: %s\n" %(self.studentName,self.studentAge,self.studentSchool))

class GoodStudent(Student):
    #define initialization of Student sub-class + new argumet
    def __init__(self):
        Student.__init__(self)
        self.studentMarks=()
    #class methods
    def setMarks(self,*marks):
        self.studentMarks=marks
    def getMarks(self):
        return self.studentMarks
    def getAllInfo(self):
        return ("Student name is: %s\nStudent age is: %s \nStudent High School: %s \nStudent marks: %s\n"
                %(self.studentName,self.studentAge,self.studentSchool,self.studentMarks))

if __name__ == '__main__':
    #test  class functional
    tom=Student()
    tom.setAge(20)
    tom.setName("Tom Hank")
    tom.setSchool("Prague High School")
    print(tom.getAllInfo())

    sue=GoodStudent()
    sue.setName("Sue Jones")
    sue.setAge(19)
    #error-wrong type input
    #sue.setAge('23')
    sue.setSchool("Brno School")
    sue.setMarks(1,45,'dg')
    print(sue.getAllInfo())
