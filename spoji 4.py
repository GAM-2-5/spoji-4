import numpy
import pygame
import sys
import random
import time
import math

#OSNOVNE NAREDBE
def napravi_ploču():
    ploča = numpy.zeros((b_red, b_kol))
    numpy.flip(ploča, 0)
    return ploča

def mogući_potez(ploča, kol):
    if ploča[b_red - 1][kol] == 0:
        return True

def sljedeći_red(ploča, kol):
    for red in range (b_red):
        if ploča[red][kol]== 0:
            return red      

def potez(ploča, red, kol, žeton):
    ploča[red][kol] = žeton   

def pobjeda(ploča, žeton):
    for kol in range (b_kol - 3):
        for red in range (b_red):
            if ploča[red][kol] == žeton and ploča[red][kol+1] == žeton and ploča[red][kol+2] == žeton and ploča[red][kol+3] == žeton:
                return True
    for kol in range (b_kol):
        for red in range (b_red - 3):
            if ploča[red][kol] == žeton and ploča[red+1][kol] == žeton and ploča[red+2][kol] == žeton and ploča[red+3][kol] == žeton:
                return True
    for kol in range (b_kol - 3):
        for red in range (b_red - 3):
            if ploča[red][kol] == žeton and ploča[red+1][kol+1] == žeton and ploča[red+2][kol+2] == žeton and ploča[red+3][kol+3] == žeton:
                return True
    for kol in range (2, b_kol):
        for red in range (b_red - 3):
            if ploča[red][kol] == žeton and ploča[red+1][kol-1] == žeton and ploča[red+2][kol-2] == žeton and ploča[red+3][kol-3] == žeton:
                return True

#NAREDBE ZA GRAFIČKI DIO            
def print_ploča(ploča, vel):
    pygame.draw.rect(ekran, ploča_boja , [0, vel, širina, visina_p])
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

def žeton(x,y):
    if runda == 0:
        pygame.draw.circle(ekran, player1boja, [x, y], r)
    if runda == 1:
        pygame.draw.circle(ekran, player2boja, [x, y], r)
        
def grafika():
    if not gam_over:
        ekran.fill(prazno_boja)
        žeton(x,y)
        print_ploča(ploča, vel)
        pygame.display.update()
        
def tekst(poruka, boja, vel_font, y_kordinata, sredina = True, x_kordinata = 50):
    font = pygame.font.SysFont('Arial', vel_font)
    tekst = font.render(poruka, True, boja)
    širina_font = font.size(poruka)[0]
    if sredina == True:
        x_kordinata = (širina - širina_font) //2
    ekran.blit(tekst,[x_kordinata, y_kordinata])
    
def tekst_kraj(poruka, boja):
    vel_font = font2
    y_kordinata = 50 
    ekran.fill(prazno_boja)
    print_ploča(ploča, vel)
    tekst(poruka, boja, vel_font, y_kordinata)
    pygame.display.update()
    time.sleep(4)

def otvori_postavke(lokacija):
    ekran.fill(crna)
    pygame.draw.rect(ekran, siva , [100, 100, 500, 500])
    pygame.draw.rect(ekran, crna , [130, 160, 2, 350])
    pygame.draw.rect(ekran, crna , [130, 160, 440, 2])
    pygame.draw.rect(ekran, crna , [130, 510, 442, 2])
    pygame.draw.rect(ekran, crna , [570, 160, 2, 350])
    tekst('POSTAVKE', crna, font2 - 10, 130, False, 130)
    tekst('NAČIN IGRANJA:', crna, font2 - 10, 200)
    tekst('IZBOR BOJA:', crna, font2 - 10, 310)
    gumb (lokacija, 'spremi', font1)
    gumb (lokacija, 'SINGLEPLAYER', font2, False, 230)
    gumb (lokacija, 'MULTIPLAYER', font2, False, 260)
    gumb (lokacija, 'standardni', font2, False, 340)
    gumb (lokacija, 'nemoguća misija', font2, False, 370)
    gumb (lokacija, 'random', font2, False, 400)

def na_njemu (lokacija, poruka):
    (xg, yg, širinag, duljinag) = gumbovi[poruka]
    if xg <lokacija[0]< xg+širinag and yg <lokacija[1]< yg+duljinag:
        return True
    
def gumb (lokacija, poruka, vel_font, bijela_tipka = True , y = 0):
    font = pygame.font.SysFont('Arial', vel_font)
    veličina = font.size(poruka)
    if bijela_tipka == True:
        (xg, yg, širinag, duljinag) = gumbovi[poruka]
        pygame.draw.rect(ekran, siva , [xg - 4, yg - 4 , širinag +8, duljinag+8])
        if na_njemu(lokacija, poruka):
            pygame.draw.rect(ekran, bijela2 , [xg, yg, širinag, duljinag])
            pygame.draw.rect(ekran, crna , [xg, yg, 2, duljinag])
            pygame.draw.rect(ekran, crna , [xg, yg, širinag, 2])
        else:
            pygame.draw.rect(ekran, bijela , [xg, yg, širinag, duljinag])
        x = xg +((širinag - veličina[0])//2)
        y = yg +((duljinag - veličina[1])//2)
        tekst(poruka, crna, vel_font, y, False, x)
    else:
        x = (širina - veličina[0]) //2
        gumbovi[poruka] = (x, y, veličina[0], veličina[1])
        if poruka == mode or poruka == colorpack:
            boja = crvena
        elif na_njemu(lokacija, poruka):
            boja = crvena2
        else:
            boja = bijela
        tekst(poruka, boja, vel_font, y)
        return gumbovi[poruka]


def početni_zaslon(lokacija):
    vel_font = font1
    if na_njemu (lokacija,'pehar'):
        if mode == 'SINGLEPLAYER':
            tekst('pobjede: {}'.format(win1), player1boja, vel_font, 170, False)
            tekst('porazi: {}'.format(win2), player2boja, vel_font, 200, False)
        else:
            tekst('IGRAČ 1: {}'.format(win1), player1boja, vel_font, 170, False)
            tekst('IGRAČ 2: {}'.format(win2), player2boja, vel_font, 200, False)
    elif na_njemu (lokacija, 'upitnik'):
        tekst('strelicama lijevo i desno upravljate žetonom', bijela, vel_font, 170, False)
        tekst('strelica dolje će ubaciti žeton', bijela, vel_font, 200, False)
    elif na_njemu(lokacija, 'postavke'):
        tekst('kliknite na postavke ako ih želite promjeniti', bijela, vel_font, 170, False)
        tekst('to će resetirati trenutni rezultat', player2boja, vel_font - 5, 200, False)
    else:
        ekran.fill(crna)
        tekst('SPOJI 4', bijela, vel_font + 30, 100)
        tekst('prijeđite preko ikona', siva, vel_font - 10, 400)
        ekran.blit(pehar_ikona,(gumbovi['pehar'][0],gumbovi['pehar'][1]))
        ekran.blit(upitnik_ikona,(gumbovi['upitnik'][0],gumbovi['upitnik'][1]))
        ekran.blit(postavke_ikona,(gumbovi['postavke'][0],gumbovi['postavke'][1]))
        gumb (lokacija, 'IGRAJ', font1)
    
#NAREDBE ZA SINGLEPLAYER MODE 
def bodovanje(dio, žeton):
    vr_dio = 0
    protivnik = žeton1
    if žeton == žeton1:
        protivnik = žeton2
    if dio.count(žeton) == 4:
        vr_dio += 1000
    if dio.count(žeton) == 3 and dio.count(prazno) == 1:
        vr_dio += 15
    if dio.count(žeton) == 2 and dio.count(prazno) == 2:
        vr_dio += 2
    if dio.count(protivnik) == 3 and dio.count(prazno) == 1:
        vr_dio -= 70
    elif dio.count(protivnik) == 2 and dio.count(prazno) == 2:
        vr_dio -= 10
    return vr_dio

def vrijednost_ploče(ploča, žeton):
    vr = 0
    centar = [int(i) for i in list(ploča[:, b_kol//2])]
    u_centru = centar.count(žeton)
    vr += 3*u_centru
    for r in range (b_red):
        jedan_red = [int(i) for i in list(ploča[r, :])]
        for k in range (b_kol - 3):
            dio = jedan_red[k:k+4]
            vr += bodovanje (dio, žeton)
    for k in range (b_kol):
        jedna_kol = [int(i) for i in list(ploča[:, k])]
        for r in range (b_red - 3):
            dio = jedna_kol[r: r+4]
            vr += bodovanje(dio, žeton)
    for r in range (b_red -3):
        for k in range (b_kol -3):
            dio = [int(ploča[r+i][k+i]) for i in range (4)]
            vr += bodovanje(dio, žeton)
    for r in range (b_red -3):
        for k in range (2, b_kol):
            dio = [int(ploča[r+i][k-i]) for i in range (4)]
            vr += bodovanje(dio, žeton)
    return vr

def moguće_kolone(ploča):
    m_kolone = []
    for kol in range (b_kol):
        if mogući_potez(ploča, kol):
            m_kolone.append(kol)
    return m_kolone

#MINIMAX ALGORITAM
def kraj_mogućnosti(ploča):
    if len(moguće_kolone(ploča)) == 0 or pobjeda(ploča, žeton1) or pobjeda(ploča,žeton2):
        return True
    
def minimax(ploča, dubina,alpha, beta, maksimiziranje):
    m_kolone= moguće_kolone(ploča)
    if kraj_mogućnosti or dubina == 0:
        if kraj_mogućnosti(ploča):
            if pobjeda(ploča, žeton2):
                return (None, 1000000000)
            if pobjeda (ploča, žeton1):
                return (None, -1000000000)
            else: return (None, 0)
        if dubina == 0:
            return (None, vrijednost_ploče(ploča, žeton2))
    if maksimiziranje:  
        vrijednost = - math.inf
        naj_kol= random.choice(m_kolone)
        for kol in m_kolone:
            red = sljedeći_red(ploča, kol)
            ploča_kopija = ploča.copy()
            potez(ploča_kopija, red, kol, žeton2)
            nova_vr = minimax(ploča_kopija, dubina -1,alpha, beta, False)[1]
            alpha = max(alpha, vrijednost)
            if beta <= alpha:
                break
            if nova_vr > vrijednost:
                vrijednost = nova_vr
                naj_kol = kol
        return naj_kol, nova_vr
    if not maksimiziranje:
        vrijednost = math.inf
        naj_kol= random.choice(m_kolone)
        for kol in m_kolone:
            red = sljedeći_red(ploča, kol)
            ploča_kopija = ploča.copy()
            potez(ploča_kopija, red, kol, žeton1)
            nova_vr = minimax(ploča_kopija, dubina - 1, alpha, beta, True)[1]
            beta = min(beta, vrijednost)
            if beta >= alpha:
                break
            if nova_vr < vrijednost:
                vrijednost = nova_vr
                naj_kol = kol
        return naj_kol, nova_vr
        
bijela = (255, 255, 255)
bijela2 = (230, 230, 230)
crna = (0,0,0)
siva = (139, 145, 148)
crvena = (255, 0, 0)
žuta = (255, 255, 0)
plava = (20, 20, 240)
aqua = (0, 255, 255)
crvena2 = (255, 150, 70)
gumbovi = {'pehar' : (158, 300, 64, 64),
           'upitnik' : (318, 300, 64, 64),
           'postavke' : (478, 300, 64, 64),
           'IGRAJ' :(300, 500, 100, 40),
           'spremi' : (470, 540, 100, 30)}
b_red = 6
b_kol = b_red + 1
širina = 700
visina = širina
vel = int(širina/b_kol)
visina_p = širina - vel
r = vel//2 - 4
x = vel//2
y = x
gam_over = True
game_exit = False
postavke = False
žeton1 = 1
žeton2 = 2
prazno = 0
win1 = 0
win2 = 0
font1= 25
font2= 30
ploča = napravi_ploču()

mode = 'SINGLEPLAYER'
prazno_boja = crna
ploča_boja = plava
player1boja = žuta
player2boja = crvena
colorpack = 'standardni'

pygame.init()  
ekran = pygame.display.set_mode((širina, visina))
ikona = pygame.image.load('ikona.png')
postavke_ikona = pygame.image.load('postavke.png')
pehar_ikona = pygame.image.load('pehar.png')
upitnik_ikona = pygame.image.load('upitnik.png')
pygame.display.set_caption('IGRA SPOJI 4')
pygame.display.set_icon(ikona)

while  not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if na_njemu(lokacija, 'postavke'):
                postavke = True
            if na_njemu(lokacija,'IGRAJ'):
                gam_over = False
                
            if postavke == True:
                win1 = 0
                win2 = 0
                sve_boje =[crvena, žuta, plava, aqua, bijela, siva]
                if na_njemu(lokacija, 'spremi'):
                    postavke = False
                if 230<lokacija[1]< 230+font2:
                    mode = 'SINGLEPLAYER'
                if 260<lokacija[1]<260+font2:
                    mode = 'MULTIPLAYER'
                if 340<lokacija[1]<340+font2:
                    colorpack = 'standardni'
                    ploča_boja = plava
                    player1boja = žuta
                    player2boja = crvena
                if 370<lokacija[1]<370+font2:
                    colorpack = 'nemoguća misija'
                    ploča_boja = siva
                    player1boja = crvena
                    player2boja = crvena
                if 400<lokacija[1]<400+font2:
                    colorpack = 'random'
                    ploča_boja = sve_boje.pop(random.randint(0,len(sve_boje)-1))
                    player1boja = sve_boje.pop(random.randint(0,len(sve_boje)-1))
                    player2boja = sve_boje.pop(random.randint(0,len(sve_boje)-1))
                    
        lokacija = pygame.mouse.get_pos()
        if not postavke and gam_over:
            početni_zaslon(lokacija)
        if postavke and gam_over:
            otvori_postavke(lokacija)    
        pygame.display.update()
    runda = random.randint(0,1)
    ploča = napravi_ploču()
    grafika()
    
    while not gam_over:       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gam_over = True
                win1 = 0
                win2 = 0
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
                            grafika()
                            if pobjeda(ploča, žeton1) and mode == 'MULTIPLAYER':
                                tekst_kraj('IGRAČ 1 je pobjedio!', player1boja)
                                gam_over = True
                                win1 += 1
                            elif pobjeda(ploča, žeton1) and mode == 'SINGLEPLAYER':
                                tekst_kraj('Pobijedio si - bravo kralju!', player1boja)
                                gam_over = True
                                win1 += 1
                        else: runda -= 1
                    #Player2 input
                    if runda == 1 and mode == 'MULTIPLAYER':
                        kol = x // vel
                        if mogući_potez(ploča, kol):
                            red = sljedeći_red(ploča, kol)
                            potez(ploča, red, kol, žeton2)
                            grafika()
                            if pobjeda(ploča, žeton2):
                                tekst_kraj('IGRAČ 2 je pobjedio!', player2boja)
                                gam_over = True
                                win2 += 1
                        else: runda -= 1
                    if len (moguće_kolone(ploča))== 0:
                        tekst_kraj('Izjednačeno!', bijela)
                        gam_over = True
                    runda += 1
                    runda = runda % 2
                grafika()
            #Player program        
            if runda == 1 and mode == 'SINGLEPLAYER' and gam_over == False:
                kol, vr = minimax(ploča, 2, -math.inf, math.inf, True) 
                red = sljedeći_red(ploča, kol)      
                novix = kol*vel + vel//2
                grafika()
                while not x == novix:
                    if novix > x:
                        x += vel
                    if novix < x:
                        x -= vel
                    grafika()
                    time.sleep(0.3)    
                potez(ploča, red, kol, žeton2)
                if pobjeda(ploča, žeton2):
                    tekst_kraj('Izgubio si! Više sreće drugi put. ;)', player2boja)
                    gam_over = True
                    win2 += 1
                if len (moguće_kolone(ploča))== 0:
                    tekst_kraj('Izjednačeno!', bijela)
                    gam_over = True
                vr = 0
                runda += 1
                runda = runda % 2
                grafika()
                
pygame.quit()
