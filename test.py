
# -*- coding: utf-8 -*-

import sys, random, threading, time
from dic2 import *
from PyQt5.QtWidgets import *
from PyQt5 import uic #преобразование формы qt  в код python3
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
class Results:
    q=0 #количество заданных вопросов
    r=0 #количество правильных ответов
class MainWindow (QMainWindow):#окно приветствия

    def __init__(self):#где написаны init вещи
        super().__init__()#наследование самого себя
        self.initUI()
        MainWindow=uic.loadUi("mainpicture.ui", self)#подключение модуля дизайна
        self.pushButton_2.clicked.connect(self.forward)#вызов процедуры forward по нажатию кнопки pushButton2
    def initUI(self):
        self.resize(250, 150)#размер окна
        self.center()
        self.setWindowTitle('Center')#задают название форме

        self.show()

    def center(self):#задает геометрию окна
        qr = self.frameGeometry()#раздвигать мышкой
        cp = QDesktopWidget().availableGeometry().center()#подключаются библиотеки
        qr.moveCenter(cp)#передвижение мыши по окну
        self.move(qr.topLeft())#отсчет от левого-верхнего угла
    def closeEvent(self, event):#метод закрытия  окна
        reply = QMessageBox.question(self, 'Внимание!', "Действительно хотите закончить тест??", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#окно сообщения с вопросом
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
            event.accept()#если нажимаем NO то остаемся в окне
        else:
            event.ignore()#закрываем форму
    def forward(self,event):# переход на следующую форму
            self.x3=Dialog()#показать форму описанную классом dialog
            self.hide()#спрятать когда показалась форма dialog
class Dialog(QDialog):#окно выбора уровня

    def __init__(self):
         super().__init__()
         uic.loadUi("picture2.ui", self)
         self.initUI()


    def initUI(self):#иницализируем интерфейс

        self.pushButton_2.setEnabled(False)#устанавливаем кнопку изначально недоступной
        self.pushButton.clicked.connect(self.back) # по нажатию кнопки начинаем процедуру back
        self.radioButton.toggled.connect(self.click_on_button1) # если выбрать этот перключатель начнется процедура click_on_button1
        self.radioButton_2.toggled.connect(self.click_on_button2)# если выбрать этот перключатель начнется процедура click_on_button1
        self.radioButton_3.toggled.connect(self.click_on_button3)# если выбрать этот перключатель начнется процедура click_on_button2
        self.show() # показать окно
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):#окно закрытия 2й формы
            reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
                 event.accept()#если нажимаем NO то остаемся в окне
            else:
                 event.ignore()
    def back(self,event):# возвращение назад
                 self.x3=MainWindow()
                 self.hide() # скрываем текущее окно
    def forward (self,event):# продвиждение вперед для 1-го и 2-го уровней тестирования
                 self.x3= Dialog2()
                 self.hide()# скрываем текущее окно
    def forward2 (self,event):# продвиждение вперед для 3-го уровня тестирования
                self.x3= Dialog3()
                self.hide()# скрываем текущее окно
    def forward3 (self,event):# продвиждение вперед для 3-го уровня тестирования
                self.x3= Dialog4()
                self.hide()# скрываем текущее окно
    def click_on_button1(self):# процедура 1-й radioButton
            self.pushButton_2.setEnabled(True)# делаем кнопку доступной
            self.pushButton_2.clicked.connect(self.forward)#по нажатию накнопку происходит переход на следующую форму
    def click_on_button2(self):# процедура 2-й radioButton
        
            self.pushButton_2.setEnabled(True)# делаем кнопку доступной
            self.pushButton_2.clicked.connect(self.forward3)#по нажатию накнопку происходит переход на следующую форму
    def click_on_button3(self):# процедура 2-й radioButton
        
            self.pushButton_2.setEnabled(True)# делаем кнопку доступной
            self.pushButton_2.clicked.connect(self.forward2)#по нажатию накнопку происходит переход на следующую форму
class Dialog2(QDialog): # форма тестирования 1-го и 2-го уровней

    def __init__(self):
        super().__init__()
        uic.loadUi("picture3.ui", self)
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Номер вопроса-'+str(Results.q), self)#первая надпись
        lbl1.move(85, 10) #размещение надписи
        self.a=''
        key={}
        n=random.randint(0,199)
        question= countries[n]+' какую имеет столицу?'
        self.label.setText(question)
        self.answer=CorrectDir[countries[n]]
        nint2=random.randint(1,4)
        key[nint2]=CorrectDir[countries[n]]
        k=0
        while k<4:
            k+=1
            if k!=nint2:
                while True:
                    nint=random.randint(0,9)
                    if CorrectDir[countries[nint]] not in key.values():
                        key[k]=CorrectDir[countries[nint]]#использовали словарь
                        break
        self.y1=key[1]
        self.pushButton.setText(key[1])#даем название этой кнопке
        self.pushButton.clicked.connect(self.On_Click1)#что происходит по ее нажатию


        self.y2=key[2]
        self.pushButton_2.setText(key[2])
        self.pushButton_2.clicked.connect(self.On_Click2)

        self.y3=key[3]
        self.pushButton_3.setText(key[3])
        self.pushButton_3.clicked.connect(self.On_Click3)

        self.y4=key[4]
        self.pushButton_4.setText(key[4])
        self.pushButton_4.clicked.connect(self.On_Click4)


        self.show() # показать окно

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):#окно закрытия 2й формы
        reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
            event.accept()#если нажимаем NO то остаемся в окне
        else:
            event.ignore()
    def On_Click1(self):
        if Results.q!=10:#если не десятый вопрос то далее
            Results.q+=1#увеличиваем вопрос
            self.hide()
            self.y1==self.a
            if self.y1 == self.answer:#проверяем введеный ответ с правильным
                Results.r+=1#увеличиваем кол-во правильных ответов
                self.x4= Picture4()#вы правы
            else:
                self.x4=Picture5()#вы ошиблись
            self.hide()
            self.x3= Dialog2()#вызываем окно с вопросом заново
        else:#тестирование прекращается переходим к результатам
            self.hide()
            self.x7=Picture()#показать окно результатов
    def On_Click2(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            self.y2==self.a
            if self.y2 == self.answer:
                Results.r+=1
                self.x4= Picture4()
            else:
                self.x4=Picture5()
            self.hide()
            self.x3= Dialog2()
        else:
            self.hide()
            self.x7=Picture()
    def On_Click3(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            self.y2==self.a
            if self.y3 == self.answer:
                Results.r+=1
                self.x4= Picture4()
            else:
                self.x4=Picture5()
            self.hide()
            self.x3= Dialog2()
        else:
            self.hide()
            self.x7=Picture()
    def On_Click4(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            self.y2==self.a
            if self.y4 == self.answer:
                Results.r+=1
                self.x4= Picture4()
            else:
                self.x4=Picture5()
            self.hide()
            self.x3= Dialog2()
        else:
            self.hide()
            self.x7=Picture()
class Dialog3(QDialog): # форма тестирования 3-го уровня

    def __init__(self):
        super().__init__()
        uic.loadUi("picture6.ui", self)
        self.initUI()

    def initUI(self):
        self.a=''
        lbl1 = QLabel('Номер вопроса-'+str(Results.q), self)#первая надпись
        lbl1.move(85, 10) #размещение надписи
        n=random.randint(0,59)
        question= country[n]+' какую имеет столицу?'

        self.label.setText(question)
        self.answer=correct[country[n]]#присваивание правильного ответа
        

        self.lbl3 = QLabel()#первая надпись
        self.lbl3.move(85, 20) #размещение надписи
        self.lbl3 = QLabel()#первая надпись
        self.lbl3.move(85, 30) #размещение надписи
        self.pushButton.clicked.connect(self.On_Click1)
        self.pushButton_2.clicked.connect(self.On_Click2)


        self.show() # показать окно

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):#окно закрытия 2й формы
        reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
            event.accept()#если нажимаем NO то остаемся в окне
        else:
            event.ignore()
    def On_Click2(self):
        self.a=self.textEdit.toPlainText()
        self.a=self.a.strip()
        self.a=self.a.capitalize()
    def On_Click1(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            if self.a == self.answer:
                Results.r+=1
                self.x4= Picture4()
                self.x3= Dialog3()
            else:
                self.x4= Picture5()
                self.hide()
                self.x3= Dialog3()
        else:
                self.hide()
                self.x7=Picture()
class Picture4(QDialog): # форма оповещения о неправильном ответе
    def __init__(self):
        super().__init__()
        uic.loadUi("picture4.ui", self)
        self.initUI()

    def initUI(self):
        self.qbtn2 = QPushButton('Далее', self)#заводим кнопку
        self.qbtn2.clicked.connect(self.forward)#по нажатию накнопку происходит переход на следующую форму
        self.qbtn2.resize(self.qbtn2.sizeHint())
        self.qbtn2.move(250, 300)#устанавливаем положение кнопки
        self.qbtn2.setStyleSheet("background-color: Blue")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)#устанавливаем появление окна поверх другого окна
        self.show() # показать окно
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):#окно закрытия 2й формы
        reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
            event.accept()#если нажимаем NO то остаемся в окне
        else: event.ignore()
    def forward (self,event):self.hide()# продвиждение вперед для 1-го и 2-го уровней тестирования
class Picture5(QDialog): # форма оповещения о неправильном ответе
        def __init__(self):
            super().__init__()
            uic.loadUi("picture5.ui", self)
            self.initUI()

        def initUI(self):
            self.qbtn2 = QPushButton('Далее', self)#заводим кнопку
            self.qbtn2.clicked.connect(self.forward)#по нажатию накнопку происходит переход на следующую форму
            self.qbtn2.resize(self.qbtn2.sizeHint())#установление размера кнопки
            self.qbtn2.move(250, 300)#устанавливаем положение кнопки
            self.qbtn2.setStyleSheet("background-color: Blue")
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            self.show() # показать окно
        def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        def closeEvent(self, event):#окно закрытия 2й формы
            reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
               event.accept()#если нажимаем NO то остаемся в окне
            else: event.ignore()
        def forward (self,event):self.hide()# продвиждение вперед для 1-го и 2-го уровней тестирования

class Dialog4(QDialog): # форма тестирования 2-го уровней

    def __init__(self):
        super().__init__()
        uic.loadUi("picture3.ui", self)
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Номер вопроса-'+str(Results.q), self)#первая надпись
        lbl1.move(85, 10) #размещение надписи
        self.a=''
        key={}
        n=random.randint(0,81)
        question= objec[n]+' какой административный центр?'
        self.label.setText(question)
        self.answer=correctsubject[objec[n]]
        nint2=random.randint(1,4)
        key[nint2]=correctsubject[objec[n]]
        k=0
        while k<4:
            k+=1
            if k!=nint2:
                while True:
                    nint=random.randint(0,9)
                    if correctsubject[objec[nint]] not in key.values():
                        key[k]=correctsubject[objec[nint]]
                        break
        self.y1=key[1]
        self.pushButton.setText(key[1])
        self.pushButton.clicked.connect(self.On_Click1)


        self.y2=key[2]
        self.pushButton_2.setText(key[2])
        self.pushButton_2.clicked.connect(self.On_Click2)

        self.y3=key[3]
        self.pushButton_3.setText(key[3])
        self.pushButton_3.clicked.connect(self.On_Click3)

        self.y4=key[4]
        self.pushButton_4.setText(key[4])
        self.pushButton_4.clicked.connect(self.On_Click4)


        self.show() # показать окно

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):#окно закрытия 2й формы
        reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
            event.accept()#если нажимаем NO то остаемся в окне
        else:
            event.ignore()
    def On_Click1(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            self.y1==self.a
            if self.y1 == self.answer:
                Results.r+=1
                self.x4= Picture4()
            else:
                self.x4=Picture5()
            self.hide()
            self.x3= Dialog4()
        else:
            self.hide()
            self.x7=Picture()
    def On_Click2(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            self.y2==self.a
            if self.y2 == self.answer:
                Results.r+=1
                self.x4= Picture4()
            else:
                self.x4=Picture5()
            self.hide()
            self.x3= Dialog4()
        else:
            self.hide()
            self.x7=Picture()
    def On_Click3(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            self.y2==self.a
            if self.y3 == self.answer:
                Results.r+=1
                self.x4= Picture4()
            else:
                self.x4=Picture5()
            self.hide()
            self.x3= Dialog4()
        else:
            self.hide()
            self.x7=Picture()
    def On_Click4(self):
        if Results.q!=10:
            Results.q+=1
            self.hide()
            self.y2==self.a
            if self.y4 == self.answer:
                Results.r+=1
                self.x4= Picture4()
            else:
                self.x4=Picture5()
            self.hide()
            self.x3= Dialog4()
        else:
            self.hide()
            self.x7=Picture()
class Picture(QDialog): # форма оповещения о результатах теста
        def __init__(self):
            super().__init__()
            uic.loadUi("picture.ui", self)
            self.initUI()

        def initUI(self):
            if Results.r<=4: self.label.setText('Вы набрали всего-'+str(Results.r)+' правильных ответов')
            elif Results.r>4 and Results.r<10: self.label.setText('Вы набрали целых-'+str(Results.r)+' правильных ответов')
            self.show() # показать окно
        def center(self):
                qr = self.frameGeometry()
                cp = QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
        def closeEvent(self, event):#окно закрытия 2й формы
                reply = QMessageBox.question(self, 'Внимание', "Форма закроется. Вы правда этого хотите?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes: #если нажимаем Yes, то выходим из окна
                    event.accept()#если нажимаем NO то остаемся в окне
                else: event.ignore()
        def forward (self,event):self.hide()# продвиждение вперед для 1-го и 2-го уровней тестирования
if __name__ == '__main__':#технические строчки, указывающие какое окно появляется первым
    app = QApplication(sys.argv)#подключение базовой библиотеки qt, все сигналы и слоты содержатся вней
    ex = MainWindow()#задается название окна которе появляется первым
    sys.exit(app.exec_())#стандартная процедура выхода 
