import pygame
from random import *
from cristall import Cristall
pygame.init()

W, H = 900,500
window = pygame.display.set_mode((W,H))
pygame.display.set_caption("Game")
pygame.time.set_timer(pygame.USEREVENT, 2000)

clock = pygame.time.Clock()

bg_load = pygame.image.load('images/фон.png')
bg_image = pygame.transform.scale(bg_load,(bg_load.get_width()//2, bg_load.get_height()//2))

telega = pygame.image.load("images/telega.png")
telega_img = pygame.transform.scale(telega, (telega.get_width()//10, telega.get_height()//10))
telega_rect = telega_img.get_rect(centerx=W//2, bottom=H-15)
speed_t = 13

cristall_img = ["001.png", "002.png", "003.png"]
cristall_surf = [pygame.image.load("images/"+path) for path in cristall_img]

def create_cristall(group):
    indx = randint(0, len(cristall_img)-1)  #индекс последнего через код len(list)-1 -длина списка- print(len(list))
    x = randint(20, W-20)
    speed = randint(3, 8)

    return Cristall(x, speed, cristall_surf[indx], group)

cristalls = pygame.sprite.Group()
"""cristalls.add(Cristall(W//2, 1, 'imges/001.png'),#delete
              Cristall(W//2-250, 3, 'imges/002.png'),
              Cristall(W//2+250, 5, 'imges/003.png'))
"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            create_cristall(cristalls)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        telega_rect.x = telega_rect.x - speed_t
        if telega_rect.x < 0:
            telega_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        telega_rect.x = telega_rect.x + speed_t
        if telega_rect.x > W - telega_rect.width:
            telega_rect.x = W - telega_rect.width

    window.blit(bg_image, (0,0))
    cristalls.draw(window)

    window.blit(telega_img, telega_rect)

    pygame.display.update()
    clock.tick(60)

    cristalls.update(H)

# imges -> images in file