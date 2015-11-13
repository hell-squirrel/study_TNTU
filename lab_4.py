__author__ = 'Hulka Yuriy'

import sys
class list_observer(list):
    """
    Send all changes to an observer.
    """
    def __init__ (self,value,observer):
        list.__init__(self,value)
        self.set_observer(observer)

    def set_observer (self,observer):
        """
        All changes to this list will trigger calls to observer methods.
        """
        self.observer = observer
    def append (self,value):
        list.append(self,value)
        self.observer.list_append(self)
        return value
class printargs(object):
    """
     prints the name of the method and all arguments.
    """
    def p(self, *args):
        print(self.attr, args)
    def __getattr__(self, attr):
        self.attr = attr
        return self.p


class Student():
    #define initialization
    def __init__(self):
        self.studentName='None'
        self.studentAge=18
        self.studentSchool=None

    #class methods
    def setSchool(self,school):
        if type(school)!=str:print("Incorreect school value!"),sys.exit()
        self.studentSchool=school
    def setName(self,name):
        if type(name)!=str:print("Incorreect name value!"),sys.exit()
        self.studentName=name
        return self.studentName
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
    def setMarks(self,list=[]):
        self.studentMarks=list
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
    observer = printargs()
    data= list_observer([], observer)
    print(sue.setMarks(data.append((2,'d'))))
    print(sue.getAllInfo())


