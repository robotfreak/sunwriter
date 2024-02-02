import pygame

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Fenster öffnen
screen = pygame.display.set_mode((640, 480))

startpoint = pygame.math.Vector2(10, 470)
endpoint = pygame.math.Vector2(630, 470)
#midpoint = pygame.math.Vector2(630, 470)
angle = 0

text1_point = pygame.math.Vector2( 70, 255)
text2_point = pygame.math.Vector2(105, 180)
text3_point = pygame.math.Vector2( 20, 165)

# solange die Variable True ist, soll das Spiel laufen
active = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while active:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            print("Spieler hat Quit-Button angeklickt")

    # Spielfeld löschen
    screen.fill(SCHWARZ)

    pygame.draw.polygon(screen, WEISS, [[10,290], [105,120], [200,290]], 2)
    #pygame.draw.polygon(screen, WEISS, [[10,470], [315,0], [630,470]], 2)
    #pygame.draw.line(screen, WEISS, startpoint, endpoint, 2)
    #angle = 240
    #pygame.draw.line(screen, WEISS, startpoint, endpoint(angle), 2)
    #angle = 120
    #pygame.draw.line(screen, WEISS, endpoint, startpoint.rotate(angle), 2)

    # Fenster aktualisieren
    pygame.display.flip()
    pygame.time.delay(500)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 36, True, False)
 
    # Sideways text
    text1 = font.render("never", True, WEISS)
    #text = pygame.transform.rotate(text, 60)
    screen.blit(text1, text1_point)
    pygame.display.flip() # if screen is your display
    pygame.time.delay(500)
    
    # Sideways text
    text2 = font.render("odd", True, WEISS)
    text2 = pygame.transform.rotate(text2, 120)
    screen.blit(text2, text2_point)
    pygame.display.flip() # if screen is your display
    pygame.time.delay(500)

    # Sideways text
    text3 = font.render("or even", True, WEISS)
    text3 = pygame.transform.rotate(text3, 240)
    screen.blit(text3, text3_point)
    pygame.display.flip() # if screen is your display
    pygame.time.delay(1500)


    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()