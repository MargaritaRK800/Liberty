import pygame


class YouAreRight():
    def __init__(self):
        self.b=True
        self.q=1
        self.p=0
        self.right = 0
        pygame.init()  # вызов библиотеки pygame
        self.sc = pygame.display.set_mode((1138, 585))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
        self.field = pygame.image.load('gree.png')  # подгрузка файла для фоновой заливки в переменную fild
        self.background = self.field.get_rect(bottomright=(1138, 585))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
        self.sc.blit(self.field, self.background)
        self.f2 = pygame.font.Font(None, 35)
        pygame.display.update()  # первый раз прорисовываем экран
        while self.b:# заводим бесконечный цикл
                for self.i in pygame.event.get():
                    if self.i.type == pygame.QUIT:  # нажимаем кнопку закрытия экрана
                        pygame.time.delay(20)
                    if self.i.type == pygame.MOUSEBUTTONDOWN:  # нажимаем что-нибудь на мыши
                        if self.i.button == 1: # клик ЛКМ
                            self.x = self.i.pos[0]
                            self.y = self.i.pos[1]

                            if self.x > 896 and self.x < 1076 and self.y > 467 and self.y < 537:# это первый уровень субъекты федерации
                                self.b=False
class YouAreWrong():
    def __init__(self):
        self.b=True
        self.q=1
        self.p=0
        self.right = 0
        pygame.init()  # вызов библиотеки pygame
        self.sc = pygame.display.set_mode((1083, 559))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
        self.field = pygame.image.load('fal.png')  # подгрузка файла для фоновой заливки в переменную fild
        self.background = self.field.get_rect(bottomright=(1083, 559))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
        self.sc.blit(self.field, self.background)
        self.f2 = pygame.font.Font(None, 35)
        pygame.display.update()  # первый раз прорисовываем экран
        while self.b:# заводим бесконечный цикл
                for self.i in pygame.event.get():
                    if self.i.type == pygame.QUIT:  # нажимаем кнопку закрытия экрана
                        pygame.time.delay(20)
                    if self.i.type == pygame.MOUSEBUTTONDOWN:  # нажимаем что-нибудь на мыши
                        if self.i.button == 1: # клик ЛКМ
                            self.x = self.i.pos[0]
                            self.y = self.i.pos[1]
                            if self.x > 880 and self.x < 1040 and self.y > 449 and self.y < 517:# это первый уровень субъекты федерации
                                self.b=False
class Results():
    def __init__(self,results):
        self.b=True
        self.q=1
        self.p=0
        self.right = 0
        pygame.init()  # вызов библиотеки pygame
        self.sc = pygame.display.set_mode((1178, 573))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
        self.field = pygame.image.load('res.png')  # подгрузка файла для фоновой заливки в переменную fild
        self.background = self.field.get_rect(bottomright=(1178, 573))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
        self.f2 = pygame.font.Font(None, 35)
        self.question = ' у вас ' + str(results)+ 'правильных ответов'
        self.text = self.f2.render(self.question, 1, (0, 0, 0))
        self.sc.blit(self.field, self.background)
        self.sc.blit(self.text, (70, 375))
        self.f2 = pygame.font.Font(None, 35)
        pygame.display.update()  # первый раз прорисовываем экран
        while self.b:# заводим бесконечный цикл
                for self.i in pygame.event.get():
                    if self.i.type == pygame.QUIT:  # нажимаем кнопку закрытия экрана
                        pygame.time.delay(20)
                    if self.i.type == pygame.MOUSEBUTTONDOWN:  # нажимаем что-нибудь на мыши
                        if self.i.button == 1: # клик ЛКМ
                            self.x = self.i.pos[0]
                            self.y = self.i.pos[1]
                            if self.x > 880 and self.x < 1040 and self.y > 449 and self.y < 517:# это первый уровень субъекты федерации
                                self.b=False
                                pygame.quit()
                                exit()
    
