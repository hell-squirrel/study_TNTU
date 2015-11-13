#coding: utf8
import sys
from Labs import lab_4

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QMessageBox
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('TNTY')
form_class, base_class = loadUiType('form_pop.ui')
form_class2,base_class2 =loadUiType('form5.ui')
#-----------------------------------------------------#

#Creation MainWindow frame(choose class build)
class MainWindow(QMainWindow, form_class):

    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)

    def WithMarks(self):
        global student
        student=lab_4.GoodStudent()
        self.mainFrame=QDialog(self)
        self.mainFrame.ui=MainForm(self)
        self.mainFrame.ui.setWindowTitle('StdS v0.04')
        self.mainFrame.ui.show()

    def WithoutMarks(self):
        global student
        student=lab_4.Student()

        self.mainFrame=QDialog(self)
        self.mainFrame.ui=MainForm(self)
        self.mainFrame.ui.setWindowTitle('StdS v0.04')
        self.mainFrame.ui.show()




#Creation MainFrame with all content(+all buttons methons)
class MainForm(QDialog, form_class2):

    def __init__(self, *args):
        super(MainForm, self).__init__(*args)
        self.setupUi(self)

    def setName(self):
        if self.lineName.text()=='':
            box=QMessageBox().information(self,'INFO','No name value')
        else:
            student.setName(self.lineName.text())
            return self.lineName.text()

    def setAge(self):
        if self.lineAge.text()=='':
            box=QMessageBox().information(self,'INFO','No age value')
        else:
            try:
                student.setAge(int(self.lineAge.text()))
            except:

                box=QMessageBox().information(self,'INFO','Only numbers')
            return self.lineAge.text()

    def setSchool(self):
        if self.lineSchool.text()=='':
            box=QMessageBox().information(self,'INFO','No school name value')
        else:
            student.setSchool(self.lineSchool.text())
            return self.lineSchool.text()

    def getAge(self):
            print(student.getAge())
            return student.getAge()

    def getAllInfo(self):
        print(student.getAllInfo())
        return student.getAllInfo()




    def setMarks(self):
        if type(student).__name__=='Student':
            box=QMessageBox().warning(self,'INFO','Not avalible')
        else:
            if self.lineMarks.text()=='':
                box=QMessageBox().information(self,'INFO','No marks value')
            else:
                student.setMarks(list(self.lineMarks.text()))
                return self.lineMarks.text()

    def getMarks(self):
        if type(student).__name__=='Student':
            box=QMessageBox().warning(self,'INFO','Not avalible')
        else:
            print(list(student.getMarks()))
            return list(student.getMarks())
    global student
    def setAllInfo(self):
        if type(student).__name__=='Student':
            if self.lineSchool.text()=='' or  self.lineAge.text()=='' or self.lineName.text()=='':
                box=QMessageBox().information(self,'INFO','Some value(s) missing')
            else:
                student.setName(self.lineName.text())
                try:
                    student.setAge(int(self.lineAge.text()))
                except:
                    box=QMessageBox().information(self,'INFO','Only numbers')
                student.setSchool(self.lineSchool.text())
        else:
            if self.lineMarks.text()=='' or self.lineSchool.text()=='' or  self.lineAge.text()=='' or self.lineName.text()=='':
                box=QMessageBox().information(self,'INFO','Some value(s) missing')
            else:
                student.setName(self.lineName.text())
                try:
                    student.setAge(int(self.lineAge.text()))
                except:
                    box=QMessageBox().information(self,'INFO','Wrong Age')
                student.setSchool(self.lineSchool.text())
                student.setMarks(list(self.lineMarks.text()))

#-----------------------------------------------------#

if __name__ == '__main__':
    form = MainWindow()
    form.setWindowTitle('StdS v0.04')
    form.show()
    sys.exit(app.exec_())