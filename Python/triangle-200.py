import pygame

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
BLAU    = ( 0, 0, 255)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Fenster öffnen
screen = pygame.display.set_mode((800, 600))

#startpoint = pygame.math.Vector2(10, 470)
#endpoint = pygame.math.Vector2(630, 470)
#midpoint = pygame.math.Vector2(630, 470)
#angle = 0

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
    screen.fill(WEISS)
    pygame.display.flip()
    pygame.time.delay(1000)


    # Spielfeld löschen
    screen.fill(SCHWARZ)

#    pygame.draw.polygon(screen, WEISS, [[10,470], [315,0], [630,470]], 2)
    pygame.draw.polygon(screen, WEISS, [[10,470], [165,200], [320,470]], 2)
    #pygame.draw.line(screen, WEISS, startpoint, endpoint, 2)
    #angle = 240
    #pygame.draw.line(screen, WEISS, startpoint, endpoint.rotate(angle), 2)
    #angle = 120
    #pygame.draw.line(screen, WEISS, endpoint, startpoint.rotate(angle), 2)

    # Fenster aktualisieren
    pygame.display.flip()
    pygame.time.delay(1000)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 60, True, False)
 
    # Sideways text
    text = font.render("never", True, WEISS)
    #text = pygame.transform.rotate(text, 60)
    screen.blit(text, [100, 410])
    pygame.display.flip() # if screen is your display
    pygame.time.delay(500)
    
    # Sideways text
    text = font.render("odd", True, WEISS)
    text = pygame.transform.rotate(text, 120)
    screen.blit(text, [160, 280])
    pygame.display.flip() # if screen is your display
    pygame.time.delay(500)

    # Sideways text
    text = font.render("or even", True, WEISS)
    text = pygame.transform.rotate(text, 240)
    screen.blit(text, [30, 250])
    pygame.display.flip() # if screen is your display
    pygame.time.delay(1500)


    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()