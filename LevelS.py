import pygame
import random
from  dic import *
from PushMessage import *
RED = (225, 0, 50)
BLACK=(0,0,0)
class LevelSECOND():
    def __init__(self):
        self.b=True
        self.q=1
        self.p=0
        self.right = 0
        pygame.init()  # вызов библиотеки pygame
        self.sc = pygame.display.set_mode((1191, 634))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
        self.field = pygame.image.load('yrovny.png')  # подгрузка файла для фоновой заливки в переменную fild
        self.background = self.field.get_rect(bottomright=(1191, 634))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
        self.sc.blit(self.field, self.background)
        self.f2 = pygame.font.Font(None, 35)
        self.n = random.randint(0, 80)
        self.question = 'Для начала щелкните мышью'
        self.text = self.f2.render(self.question, 1, (0, 0, 0))
        self.sc.blit(self.text, (70, 75))
        self.nint2 = random.randint(1, 4)
        self.key = {}
        self.key[self.nint2] = correctsubject[objec[self.n]]
        self.k = 0

        pygame.display.update()
        while self.b:# заводим бесконечный цикл
            for self.i in pygame.event.get():
                if self.i.type == pygame.QUIT:  # нажимаем кнопку закрытия экрана
                    pygame.time.delay(20)
                if self.i.type == pygame.MOUSEBUTTONDOWN:  # нажимаем что-нибудь на мыши
                    if self.i.button == 1: # клик ЛКМ
                        self.x = self.i.pos[0]
                        self.y = self.i.pos[1]
                        pygame.init()  # вызов библиотеки pygame
                        self.sc = pygame.display.set_mode((1191,634))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
                        self.field = pygame.image.load('yrovny.png')  # подгрузка файла для фоновой заливки в переменную fild
                        self.background = self.field.get_rect(bottomright=(1191, 634))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
                        self.sc.blit(self.field, self.background)
                        self.f2 = pygame.font.Font(None, 35)
                        self.n=random.randint(0,80)
                        self.question= 'Вопрос номер '+ str(self.q)+ '. Какой административный центр имеет '+objec[self.n]+'?'
                        self.nint2=random.randint(1,4)
                        self.key={}
                        self.key[self.nint2]=correctsubject[objec[self.n]]
                        self.k=0
                        print(correctsubject[objec[self.n]])
                        while self.k<4:
                            self.k+=1
                            if self.k!=self.nint2:
                                while True:
                                    self.nint=random.randint(0,80)
                                    if correctsubject[objec[self.nint]] not in self.key.values():
                                        self.key[self.k]=correctsubject[objec[self.nint]]
                                        break
                        self.text2 = self.f2.render(self.question, 1, (0, 0, 0))
                        self.text3 = self.f2.render(self.key[1], 1, (0, 0, 0))
                        self.text4 = self.f2.render(self.key[2], 1, (0, 0, 0))
                        self.text5 = self.f2.render(self.key[3], 1, (0, 0, 0))
                        self.text6 = self.f2.render(self.key[4], 1, (0, 0, 0))
                        self.sc.blit(self.field, self.background)  # говорим показать
                        self.sc.blit(self.text2, (70, 75))# вопрос
                        self.sc.blit(self.text3, (250, 380))# первая кнопка
                        self.sc.blit(self.text4, (250, 540))# вторая кнопка
                        self.sc.blit(self.text5, (750, 380))# третья кнопка
                        self.sc.blit(self.text6, (750, 540))# четвертая кнопка


                        if self.x > 145 and self.x < 549 and self.y > 356 and self.y < 423: # первая кнопка
                            self.f = 1
                            self.q = self.q + 1
                            if self.key[1] == correctsubject[objec[self.n]]:
                                self.right+=1
                                window1 = YouAreRight()
                            else:
                                window2 = YouAreWrong()
                        if self.x > 144 and self.x < 549 and self.y > 511 and self.y < 578: # вторая кнопка
                            self.f = 2
                            self.q = self.q + 1
                            if self.key[2] == correctsubject[objec[self.n]]:
                                self.right+=1
                                window1 = YouAreRight()
                            else:
                                window3 = YouAreWrong()
                        if self.x > 676 and self.x < 1091 and self.y > 356 and self.y < 422: # третья кнопка
                            self.f = 3
                            self.q = self.q + 1
                            if self.key[3] == correctsubject[objec[self.n]]:
                                self.right+=1
                                window1 = YouAreRight()
                            else:
                                window4 = YouAreWrong()
                        if self.x > 676 and self.x < 1092 and self.y > 512 and self.y < 578: # четвертая кнопка
                            self.f = 4
                            self.q = self.q + 1
                            if self.key[4] == correctsubject[objec[self.n]]:
                                self.right+=1
                                window1 = YouAreRight()

                            else:
                                window5 = YouAreWrong()
                        if self.q == 16:
                            self.b=False
                            window6=Results(self.right)
                        pygame.display.update()
    def RightAnsw(self):
        return self.right
