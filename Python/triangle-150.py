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
screen = pygame.display.set_mode((640, 480))

# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 36, True, False)
#orig_surf = font.render('never', True, WEISS)
#txt_surf = orig_surf.copy()
# This surface is used to adjust the alpha of the txt_surf.
#alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
#alpha = 255  # The current alpha value of the surface.
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
    screen.fill(WEISS)
    pygame.display.flip()
    pygame.time.delay(2000)


    # Spielfeld löschen
    screen.fill(SCHWARZ)

    #pygame.draw.polygon(screen, WEISS, [[10,470], [165,200], [320,470]], 2)
    pygame.draw.polygon(screen, WEISS, [[10,290], [105,120], [200,290]], 2)

    # Fenster aktualisieren
    pygame.display.flip()
    pygame.time.delay(1000)

#    font = pygame.font.SysFont('Calibri', 60, True, False)
 
    # Sideways text
    text1 = font.render("never", True, WEISS)
    #text = pygame.transform.rotate(text, 60)
    #screen.blit(text, [100, 410])
    screen.blit(text1, text1_point)
    pygame.display.flip() # if screen is your display
    pygame.time.delay(500)
    
    # Sideways text
    text2 = font.render("odd", True, WEISS)
    text2 = pygame.transform.rotate(text2, 120)
    #screen.blit(text, [160, 280])
    screen.blit(text2, text2_point)
    pygame.display.flip() # if screen is your display
    pygame.time.delay(500)

    # Sideways text
    text3 = font.render("or even", True, WEISS)
    text3 = pygame.transform.rotate(text3, 240)
#    screen.blit(text, [30, 250])
    screen.blit(text3, text3_point)
    pygame.display.flip() # if screen is your display
    pygame.time.delay(1500)

    txt_surf = text1.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    while alpha > 0:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = max(alpha-4, 0)
        txt_surf = text1.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.fill((0, 0, 0))
        screen.blit(txt_surf, text1_point)
        pygame.draw.polygon(screen, WEISS, [[10,290], [105,120], [200,290]], 2)
        screen.blit(text2, text2_point)
        screen.blit(text3, text3_point)
        pygame.display.flip() # if screen is your display
        pygame.time.delay(30)
  
    txt_surf = text2.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    while alpha > 0:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = max(alpha-4, 0)
        txt_surf = text2.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.fill((0, 0, 0))
        screen.blit(txt_surf, text2_point)
        pygame.draw.polygon(screen, WEISS, [[10,290], [105,120], [200,290]], 2)
        screen.blit(text3, text3_point)
        pygame.display.flip() # if screen is your display
        pygame.time.delay(30)

    txt_surf = text3.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    while alpha > 0:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = max(alpha-4, 0)
        txt_surf = text3.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.fill((0, 0, 0))
        screen.blit(txt_surf, text3_point)
        pygame.draw.polygon(screen, WEISS, [[10,290], [105,120], [200,290]], 2)
        pygame.display.flip() # if screen is your display
        pygame.time.delay(30)

    pygame.time.delay(1000)
    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()