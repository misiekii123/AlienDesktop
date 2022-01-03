import sys
from random import *
from time import *

try:
    import pygame
    from pygame.locals import*
except ModuleNotFoundError:
    import pip
    pip.main(['install','pygame'])
    import pygame
    from pygame.locals import*


pygame.init()

# deklaracja zmiennych

SZEROKOSC = 1000
WYSOKOSC = 700
obcy_szer = 160
obcy_wys = 250
count = 0
FPS = 75
clock = pygame.time.Clock()
x = 120
y = 200
celx = 0
cely = 0
obcy_xpoz = 800
x_move = 10
HP = 100
upgrade = 1
counter = 3

obcyimg = pygame.image.load("obcy.png")
apteczkaimg = pygame.image.load("apteczka2.png")

icon = pygame.image.load("ikona.png")
oknogry = pygame.display.set_mode((SZEROKOSC,WYSOKOSC),0,32)
# oknogry = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
# pygame.RESIZABLE()
pygame.display.set_caption("ALIEN")
pygame.display.set_icon(icon)

#podstawowe funkcje


def odliczanie():
    global counter
    global gra
    while counter > 0:
        counter -= 1
        oknogry.fill((0, 0, 0))
        fontObj = pygame.font.Font("DS-DIGIT.ttf", 50)
        tekst = fontObj.render(str(counter), True, (255, 255, 255))
        oknogry.blit(tekst, (SZEROKOSC / 2 - 100, WYSOKOSC / 2 - 25))
        print(str(counter))
        sleep(1)
    if counter == 0:
        gra = True

def tlo():
    bg = pygame.image.load("mapa-deszcz_meteorytow.png")
    oknogry.blit(bg, (0, 0))


def postac():
    img = pygame.image.load("postać_trzymajaca_bron.png")
    oknogry.blit(img, (25, 100))


def bron():
    img = pygame.image.load("pistolet.png")
    oknogry.blit(img, (100, 195))


def naboj(x,y):
    img = pygame.image.load("naboj.png")
    oknogry.blit(img, (x, y))


def punkty():
    fontObj = pygame.font.Font("DS-DIGIT.ttf", 50)
    tekst = fontObj.render("Score: " + str(count), True, (255, 255, 255))
    oknogry.blit(tekst, (SZEROKOSC/2-80, 10))


def hp():
    global HP
    fontObj = pygame.font.Font("DS-DIGIT.ttf", 50)
    if HP > 20:
        tekst = fontObj.render("HP: " + str(HP), True, (255, 255, 255))
    else:
        tekst = fontObj.render("HP: " + str(HP), True, (255, 0, 0))
    oknogry.blit(tekst,(25,10))


def wspolrzedne_klikniecia(x,y):
    fontObj = pygame.font.Font("DS-DIGIT.ttf",25)
    tekst = fontObj.render("X: " + str(x) + " " + "Y:" + str(y), True, (255,255,255))
    oknogry.blit(tekst, (SZEROKOSC-150, 10))


def celownik(x,y):
    img = pygame.image.load("celownik.png")
    oknogry.blit(img,(x-60,y-50))


def obcy():
    global obcy_xpoz
    global x_move
    global HP
    global przegrana
    global gra
    oknogry.blit(obcyimg, (obcy_xpoz, 250))
    obcy_xpoz -= x_move
    if obcy_xpoz < 125:
        obcy_xpoz = 800
        HP -= 10
        if HP == 0:
            przegrana = True
            gra = False


def apteczka():
    global HP
    oknogry.blit(apteczkaimg, (SZEROKOSC/2-50,WYSOKOSC-90))


def leczenie():
    global HP
    HP += 10

def upgrade_button():
    img = pygame.image.load("upgrade.png")
    oknogry.blit(img, (800,WYSOKOSC-110))

def upgrade_func():
    global count
    global upgrade
    if count >= 50:
        count -= 50
        upgrade += 2

# główna pętla programu


przegrana = False
gra = False
start = True

while start:
    odliczanie()
    gra = True

while gra:
    tlo()
    postac()
    punkty()
    hp()
    naboj(x, y)
    bron()
    apteczka()
    upgrade_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            myszaX, myszaY = event.pos
            celx = myszaX
            cely = myszaY
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseX, mouseY = event.pos
                x = mouseX
                y = mouseY
                if x > obcy_xpoz and x < obcy_xpoz + obcy_szer and y > 275 and y < 275 + obcy_wys:
                    obcy_xpoz = 800
                    count += upgrade
                if x > 450 and x < 550 and y > WYSOKOSC - 90 and y < WYSOKOSC and HP != 100:
                    leczenie()
                if x > 800 and x < 996 and y > 590 and y < 590+140:
                    upgrade_func()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x = 120
                y = 200

    obcy()

    celownik(celx, cely)

    wspolrzedne_klikniecia(x,y)
    pygame.display.update()
    clock.tick(FPS)

while przegrana:
    oknogry.fill((0,0,0))
    fontObj = pygame.font.Font("DS-DIGIT.ttf", 50)
    tekst = fontObj.render("GAME OVER", True, (255, 255, 255))
    oknogry.blit(tekst, (SZEROKOSC/2-100, WYSOKOSC/2-25))

    smallerfontObj = pygame.font.Font("DS-DIGIT.ttf", 25)
    tekst2 = smallerfontObj.render("Score: " + str(count), True, (255,255,255))
    oknogry.blit(tekst2, (SZEROKOSC/2-50, WYSOKOSC/2+25))

    instructionsfontObj = pygame.font.Font("DS-DIGIT.ttf", 25)
    instructions = instructionsfontObj.render("Click to play again", True, (100,100,100))
    oknogry.blit(instructions, (SZEROKOSC/2-100, WYSOKOSC/2+100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                HP = 100
                count = 0
                upgrade = 1
                gra = True
                przegrana = False
                while gra:
                    tlo()
                    postac()
                    punkty()
                    hp()
                    naboj(x, y)
                    bron()
                    apteczka()
                    upgrade_button()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEMOTION:
                            myszaX, myszaY = event.pos
                            celx = myszaX
                            cely = myszaY
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mouseX, mouseY = event.pos
                                x = mouseX
                                y = mouseY
                                if x > obcy_xpoz and x < obcy_xpoz + obcy_szer and y > 275 and y < 275 + obcy_wys:
                                    obcy_xpoz = 800
                                    count += upgrade
                                if x > 450 and x < 550 and y > WYSOKOSC - 90 and y < WYSOKOSC and HP != 100:
                                    leczenie()
                                if x > 800 and x < 996 and y > 590 and y < 590 + 140:
                                    upgrade_func()

                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                x = 120
                                y = 200

                    obcy()

                    celownik(celx, cely)

                    wspolrzedne_klikniecia(x, y)
                    pygame.display.update()
                    clock.tick(FPS)

    pygame.display.update()
    clock.tick(FPS)