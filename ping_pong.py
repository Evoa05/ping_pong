from pygame import *
from random import randint
 
'''Необходимые классы'''
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > -90:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 210:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > -90:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 210:
            self.rect.y += self.speed



#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
#display.set_caption()
background = transform.scale(image.load('sky.jpg'), (win_width, win_height))
 

#Персонажи игры:
player = Player('qaz.png', 10, win_height - 280, 20, 300, 4)
player2 = Player2('qaz.png', 670, win_height - 280, 20, 300, 4)

 
finish = False

game = True
time.delay(50)


#музыка
#mixer.init()
#mixer.music.load()
#mixer.music.play()

font.init()
font2 = font.SysFont('Arial', 28)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        player2.update()
        player2.reset()
   
    display.update()
    
    
