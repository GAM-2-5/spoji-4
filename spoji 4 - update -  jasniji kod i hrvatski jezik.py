#IGRA SPOJI 4 - PYTHON KOD SA OBJAŠNJENJIMA I HRVATSKIM VARIJABLAMA
import numpy
import pygame
import sys
#napravi listu listi koji predstavljaju redove i kolone - svi su ispunjeni nulama jer su prazni na početku
def napravi_ploču():
    ploča = numpy.zeros((b_red, b_kol))
    return ploča
#okrene tu listu da bi 0-ti red bio zadnja lista
def print_ploča(board):
    print(numpy.flip(ploča, 0))    
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
#provjerava je li prethodni potez bio pobjednički
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
#grafički crta ploču sa trenutnim stanjem
def print_ploča(ploča, vel):
    pygame.draw.rect(ekran, ploča_boja , [0, vel , širina, visina_p])
    pom= vel//2
    for red in range (b_red):
        x= b_red - red
        for kol in range (b_kol):
            if ploča[red][kol] == 0:
                pygame.draw.circle(ekran, prazno, [pom + kol*vel, pom + x*vel], r)
            if ploča[red][kol] == 1:
                pygame.draw.circle(ekran, player1boja, [pom + kol*vel, pom + x*vel], r)
            if ploča[red][kol] == 2:
                pygame.draw.circle(ekran, player2boja, [pom + kol*vel, pom + x*vel], r)
#grafički crta žeton koji se miče - boja ovisna o igraču koji je na redu
def žeton(x,y):
    if runda == 0:
        pygame.draw.circle(ekran, player1boja, [x, y], r)
    else:
        pygame.draw.circle(ekran, player2boja, [x, y], r)
#odredi koja je kolona odabrana               
def kolona(x):
    return int(x // vel)
#mjenja postavke   
def postavke():
    b_red = int(input('Izaberite broj redova vaše ploče:(max 20)'))
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
#zadane boje
prazno = bijela
ploča_boja = plava
player1boja = crvena
player2boja = žuta
##mjenjaj= input('Želite li promjeniti zadane postavke igre spoji 4? (DA/NE)')
##if mjenjaj == 'DA':
##    postavke()
ploča = napravi_ploču()
gam_over = False
runda = 0
pygame.init()  
ekran = pygame.display.set_mode((širina, visina))
pygame.display.set_caption('IGRA SPOJI 4')
x = vel//2
y = vel//2
while not gam_over:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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
                    boja = player1boja
                    kol = kolona(x)
                    if mogući_potez(ploča, kol):
                        red = sljedeći_red(ploča, kol)
                        potez(ploča, red, kol, 1)
                    if pobjeda(ploča, 1):
                        print ('Player1 je pobjedio!')
                        gam_over = True 
                #Player2 input
                if runda == 1:
                    boja = player2boja
                    kol = kolona(x)
                    if mogući_potez(ploča, kol):
                        red = sljedeći_red(ploča, kol)
                        potez(ploča, red, kol, 2)
                    if pobjeda(ploča, 2):
                        print ('Player2 je pobjedio!')
                        gam_over = True 
                            
                runda += 1
                runda = runda % 2
            
            ekran.fill(prazno)
            žeton(x,y)
            print_ploča(ploča, vel)
            pygame.display.update()
        
pygame.quit()
