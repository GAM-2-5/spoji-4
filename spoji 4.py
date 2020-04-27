import numpy
import pygame
import sys
import random
import time
import math

#OSNOVNE FUNKCIJE
#napravi listu listi koji predstavljaju redove i kolone - svi su ispunjeni nulama jer su prazni na početku
def napravi_ploču():
    ploča = numpy.zeros((b_red, b_kol))
    numpy.flip(ploča, 0)
    return ploča
#provjeri je li kolona u koju želimo ubaciti već puna
def mogući_potez(ploča, kol):
    if ploča[b_red - 1][kol] == 0:
        return True
#odredi koji red je sljedeći s obzirom koja je kolona odabrana
def sljedeći_red(ploča, kol):
    for red in range (b_red):
        if ploča[red][kol]== 0:
            return red      
#stavlja '1' ili '2' koji predstavljaju žetone u dvije boje umjesto '0' na odabranoj poziciji
def potez(ploča, red, kol, žeton):
    ploča[red][kol] = žeton   
#provjerava postoji li spojenih 4 na ploči
def pobjeda(ploča, žeton):
    #provjeri horizontalne kombinacije
    for kol in range (b_kol - 3):
        for red in range (b_red):
            if ploča[red][kol] == žeton and ploča[red][kol+1] == žeton and ploča[red][kol+2] == žeton and ploča[red][kol+3] == žeton:
                return True
    #provjeri vertikalne kombinacije
    for kol in range (b_kol):
        for red in range (b_red - 3):
            if ploča[red][kol] == žeton and ploča[red+1][kol] == žeton and ploča[red+2][kol] == žeton and ploča[red+3][kol] == žeton:
                return True
    #provjeri dijagonalne kombinacije - nagnute na desno
    for kol in range (b_kol - 3):
        for red in range (b_red - 3):
            if ploča[red][kol] == žeton and ploča[red+1][kol+1] == žeton and ploča[red+2][kol+2] == žeton and ploča[red+3][kol+3] == žeton:
                return True
    #provjeri dijagonalne kombinacije - nagnute na lijevo
    for kol in range (2, b_kol):
        for red in range (b_red - 3):
            if ploča[red][kol] == žeton and ploča[red+1][kol-1] == žeton and ploča[red+2][kol-2] == žeton and ploča[red+3][kol-3] == žeton:
                return True
            
#GRAFIČKI DIO
#crta ploču sa trenutnim stanjem
def print_ploča(ploča, vel):
    pygame.draw.rect(ekran, ploča_boja , [0, vel , širina, visina_p])
    pom= vel//2
    for red in range (b_red):
        x= b_red - red
        for kol in range (b_kol):
            if ploča[red][kol] == prazno:
                pygame.draw.circle(ekran, prazno_boja, [pom + kol*vel, pom + x*vel], r)
            if ploča[red][kol] == žeton1:
                pygame.draw.circle(ekran, player1boja, [pom + kol*vel, pom + x*vel], r)
            if ploča[red][kol] == žeton2:
                pygame.draw.circle(ekran, player2boja, [pom + kol*vel, pom + x*vel], r)
#žeton na vrhu koji se miče
def žeton(x,y):
    if runda == 0:
        pygame.draw.circle(ekran, player1boja, [x, y], r)
    if runda == 1:
        pygame.draw.circle(ekran, player2boja, [x, y], r)
def grafika(): #naredbe za grafiku
    if not gam_over:
        ekran.fill(prazno_boja)
        žeton(x,y)
        print_ploča(ploča, vel)
        pygame.display.update()    
def kraj(): #kraj igre - napiše tko je pobjedio
    ekran.fill(prazno_boja)
    print_ploča(ploča, vel)
    if runda == 0:
        tekst('{} je pobjedi{}!'.format(player1, spol1), player1boja, None, 50, 50)
    elif runda == 1 and mode == 'MULTIPLAYER':
        tekst('{} je pobjedi{}!'.format(player2, spol2), player2boja, None, 50, 50)
    elif runda == 1 and mode == 'SINGLEPLAYER':
        tekst('Izgubi{} si! Više sreće drugi put. ;)'.format(spol1), player2boja, None, 50, 50)
    pygame.display.update()
    time.sleep(3)
def tekst(poruka, boja, font, vel_font, y_kordinata): 
    font = pygame.font.SysFont(font, vel_font)
    tekst = font.render(poruka, True, boja)
    širina_font = font.size(poruka)[0]
    ekran.blit(tekst,[(širina - širina_font) //2, y_kordinata])
 
#FUNKCIJE ZA SINGLEPLAYER MODE
#odredi kolko 'vrijedi' dio ploče od 4 prazna ili puna mjesta 
def bodovanje(ploča, dio, žeton, r=100, k=100):
    vr_dio = 0
    protivnik = žeton1
    if žeton == žeton1:
        protivnik = žeton2
    if dio.count(žeton) == 4:
        vr_dio += 100
    elif dio.count(žeton) == 3 and dio.count(prazno) == 1:
        vr_dio += 15
    elif dio.count(žeton) == 2 and dio.count(prazno) == 2:
        vr_dio += 2
    elif dio.count(protivnik) == 3 and dio.count(prazno) == 1:
        vr_dio -= 80
    elif dio.count(protivnik) == 2 and dio.count(prazno) == 2 and r==0:
        vr_dio -= 10
    elif len(dio)== 5:
        if dio.count(žeton1) == 0 and ploča[r-1][k] == prazno and  ploča [r-1][k+1] == prazno:
                broj = dio.count(žeton)
                vr_dio+= broj*5
    return vr_dio

#ploču dijeli na djelove i zbroji njihove vrijednosti
def vrijednost_ploče(ploča, žeton):
    vr = 0
    #bolje je odabrati središnju kolonu
    centar = [ int(i) for i in list(ploča[:, b_kol//2])]
    u_centru = centar.count(žeton)
    vr += 4*u_centru
    #horizontalne mogućnosti
    for r in range (b_red):
        jedan_red = [ int(i) for i in list(ploča[r, :])]
        for k in range (b_kol - 3):
            dio = jedan_red[k:k+4]
            vr += bodovanje (ploča, dio, žeton, r)
    #vertikalne mogućnosti
    for k in range (b_kol):
        jedna_kol = [ int(i) for i in list(ploča[:, k])]
        for r in range (b_red - 3):
            dio = jedna_kol[r:r+4]
            vr += bodovanje(ploča, dio, žeton)
    #dijagonalne mogućnosti - desno
    for r in range (b_red -3):
        for k in range (b_kol -3):
            dio = [int(ploča[r+i][k+i]) for i in range (4)]
            vr += bodovanje(ploča, dio, žeton)
    #dijagonalne mogućnosti - lijevo
    for r in range (b_red -3):
        for k in range (2, b_kol):
            dio = [int(ploča[r+i][k-i]) for i in range (4)]
            vr += bodovanje(ploča, dio, žeton)
##    #taktika 'sedmica'- naopako okrenuta 7
##    for r in range (2, b_red-1):
##        for k in range (1, b_kol-1):
##            dio = [ploča[r][k],ploča[r][k+1],ploča[r][k+2],ploča[r-1][k+1],ploča[r-2][k+2]]
##            vr+= bodovanje (ploča, dio, žeton, r, k)
    return vr
#lista kolona koje nisu popunjene do kraja
def moguće_kolone(ploča):
    m_kolone = []
    for kol in range (b_kol):
        if mogući_potez(ploča, kol):
            m_kolone.append(kol)
    return m_kolone

# --- MINIMAX ALGORITAM - pravilo odlučivanja koje se koristi u umjetnoj inteligenciji,teoriji igara, statistici i filozofiji
# za minimiziranje mogućeg gubitka za najgori slučaj (maksimalni gubitak) scenarija. Kad se radi o dobitku, naziva se "maksimin" - za maksimiziranje minimalnog dobitka.
def kraj_mogućnosti(ploča):
    if len(moguće_kolone(ploča)) == 0 or pobjeda(ploča, žeton1) or pobjeda(ploča,žeton2):
        return True
def minimax(ploča, dubina, maksimiziranje):
    m_kolone= moguće_kolone(ploča)
    if kraj_mogućnosti(ploča):
        if pobjeda(ploča, žeton2):
            return (None, 1000000)
        if pobjeda (ploča, žeton1):
            return (None, -1000000)
        else: return (None, 0)
    if dubina == 0: #došao je do dubine 0 tj. predvidio određeni broj poteza
        return (None, vrijednost_ploče(ploča, žeton2))
    if maksimiziranje: #program
#maksimiziranje je 'True' kada program predviđa svoj potez, a 'False' kada igra igrač jer će igrač igrati najbolju opciju za sebe - ona ima minimalnu vrijednost 
        vrijednost = - math.inf #stavljena je negativna beskonačnost jer ona nikada neće biti maksimum
        naj_kol= random.choice(m_kolone)
        for kol in m_kolone:
            red = sljedeći_red(ploča, kol)
            ploča_kopija = ploča.copy()
            potez(ploča_kopija, red, kol, žeton2)
            nova_vr = minimax(ploča_kopija, dubina -1, False)[1]
            if nova_vr > vrijednost:
                vrijednost = nova_vr
                naj_kol = kol
        return naj_kol, nova_vr
    if not maksimiziranje: #igrač
        vrijednost = math.inf #stavljena je beskonačnost jer ona nikada neće biti minimum
        naj_kol= random.choice(m_kolone)
        for kol in m_kolone:
            red = sljedeći_red(ploča, kol)
            ploča_kopija = ploča.copy()
            potez(ploča_kopija, red, kol, žeton1)
            nova_vr = minimax(ploča_kopija, dubina -1, True)[1]
            if nova_vr < vrijednost:
                vrijednost = nova_vr
                naj_kol = kol
        return naj_kol, nova_vr
        
#klonira ploču te napravi sve moguće poteze - odabere onaj kojim postiže najveću vrijednost ploče
def odaberi(ploča, žeton):
    m_kolone = moguće_kolone(ploča)
    naj_vr = 0
    naj_kol = random.choice(m_kolone)
    for kol in m_kolone:
        red = sljedeći_red(ploča, kol)
        ploča2 = ploča.copy()
        potez(ploča2, red, kol, žeton)
        vr = vrijednost_ploče(ploča2, žeton)
        if vr > naj_vr:
            naj_vr = vr
            naj_kol = kol
    return naj_kol

         
#boje sa RGB vrijednostima
bijela = (255, 255, 255)
crna = (0,0,0)
crvena = (255, 0, 0)
žuta = (255, 255, 0)
plava = (0, 0, 255)
magenta = (255, 255, 0)
aqua = (0, 255, 255)
narančasta = (255, 165, 0)
#zadane postavke
b_red = 6
b_kol = b_red + 1
širina = 700
visina = širina
vel = int(širina/b_kol)
visina_p = širina - vel
r = vel//2 - 2
x = vel//2
y = x
gam_over = True
game_exit = False
žeton1 = 1
žeton2 = 2
prazno = 0
ploča = napravi_ploču()
#promjenjive postavke
mode = 'SINGLEPLAYER'
spol1 = 'o'
player1 = 'IGRAČ 1'
spol2 = 'o'
player2 = 'IGRAČ 2'
prazno_boja = bijela
ploča_boja = plava
player1boja = crvena
player2boja = žuta

pygame.init()  
ekran = pygame.display.set_mode((širina, visina))
pygame.display.set_caption('IGRA SPOJI 4')

while  not game_exit:
    ekran.fill(crna)
    tekst('IGRA SPOJI 4', bijela, None, 50, 100)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            gam_over = False
    runda = random.randint(0,1)
    ploča = napravi_ploču()
    grafika()
    
    while not gam_over:       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gam_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x == vel//2: pass
                    else: x -= vel
                if event.key == pygame.K_RIGHT:
                    if x > širina - vel : pass
                    else: x += vel
                if event.key == pygame.K_DOWN:
                    #Player1 input
                    if runda == 0:
                        kol = x // vel
                        if mogući_potez(ploča, kol):
                            red = sljedeći_red(ploča, kol)
                            potez(ploča, red, kol, žeton1)
                            if pobjeda(ploča, žeton1):
                                gam_over = True
                                kraj()
                        else: runda -= 1
                    #Player2 input
                    if runda == 1 and mode == 'MULTIPLAYER':
                        kol = x // vel
                        if mogući_potez(ploča, kol):
                            red = sljedeći_red(ploča, kol)
                            potez(ploča, red, kol, žeton2)
                            if pobjeda(ploča, žeton2):
                                gam_over = True
                                kraj()
                        else: runda -= 1
                    runda += 1
                    runda = runda % 2
                if not gam_over: grafika()

            #PlayerP input - program igra         
            if runda == 1 and mode == 'SINGLEPLAYER' and gam_over == False:
                kol, vr = minimax(ploča, 3, True)
                red = sljedeći_red(ploča, kol)      
                novix = kol*vel + vel//2
                grafika()
                #pomicanje do odabrane kolone
                while not x == novix:
                    if novix > x:
                        x += vel
                    if novix < x:
                        x -= vel
                    grafika()
                    time.sleep(0.3)    
                potez(ploča, red, kol, žeton2)
                grafika()
                if pobjeda(ploča, žeton2):
                    gam_over = True
                    kraj()            
                runda += 1
                runda = runda % 2
                if not gam_over: grafika()
pygame.quit()
