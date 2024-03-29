import pygame

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
BLAU    = ( 0, 0, 255)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

def fadeIn(pg, scrn, txt, txt_pt, txt2, txt2_pt, txt3, txt3_pt, dly):
    txt_surf = txt.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
    print(txt_surf.get_width())
    alpha = 0  # The current alpha value of the surface.
    while alpha < 255:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = min(alpha+4, 255)
        txt_surf = txt.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        scrn.fill((0, 0, 0))
        scrn.blit(txt_surf, txt_pt)
        pg.draw.polygon(scrn, WEISS, [[10,290], [105,120], [200,290]], 2)
        if (txt2 != None):
            scrn.blit(txt2, txt2_pt)
        if (txt3 != None):
            scrn.blit(txt3, txt3_pt)
        pg.display.flip() # if screen is your display
        pg.time.delay(dly)

def fadeOut(pg, scrn, txt, txt_pt, txt2, txt2_pt, txt3, txt3_pt, dly):
    txt_surf = txt.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    while alpha > 0:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = max(alpha-4, 0)
        txt_surf = txt.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        scrn.fill((0, 0, 0))
        scrn.blit(txt_surf, txt_pt)
        pg.draw.polygon(scrn, WEISS, [[10,290], [105,120], [200,290]], 2)
        if (txt2 != None):
            scrn.blit(txt2, txt2_pt)
        if (txt3 != None):
            scrn.blit(txt3, txt3_pt)
        pg.display.flip() # if screen is your display
        pg.time.delay(dly)

def main(txt1, txt2, txt3):
    # initialisieren von pygame
    pygame.init()

    # Fenster oeffnen
    screen = pygame.display.set_mode((640, 480))

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 36, True, False)
    text1 = font.render(txt1, True, WEISS)
    print(text1.get_size())
    text2 = font.render(txt2, True, WEISS)
    print(text2.get_size())
    text2 = pygame.transform.rotate(text2, 120)
    text3 = font.render(txt3, True, WEISS)
    print(text3.get_size())
    text3 = pygame.transform.rotate(text3, 240)

    text1_point = pygame.math.Vector2( 70, 255)
    text2_point = pygame.math.Vector2(105, 170)
    text3_point = pygame.math.Vector2( 30, 165)

    # Bildschirm Aktualisierungen einstellen
    clock = pygame.time.Clock()

    # Ueberpruefen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Spieler hat Quit-Button angeklickt")

    # Spielfeld loeschen
    screen.fill(WEISS)
    pygame.display.flip()
    pygame.time.delay(2000)


    # Spielfeld loeschen
    screen.fill(SCHWARZ)

    #pygame.draw.polygon(screen, WEISS, [[10,470], [165,200], [320,470]], 2)
    pygame.draw.polygon(screen, WEISS, [[10,290], [105,120], [200,290]], 2)

    # Fenster aktualisieren
    pygame.display.flip()
    pygame.time.delay(1000)

    fadeIn(pygame, screen, text1, text1_point, None, None, None, None, 60)
    pygame.time.delay(500)
    fadeIn(pygame, screen, text2, text2_point, text1, text1_point, None, None, 60)
    pygame.time.delay(500)
    fadeIn(pygame, screen, text3, text3_point, text1, text1_point, text2, text2_point, 60)
    pygame.time.delay(1500)

    fadeOut(pygame, screen, text1, text1_point, text2, text2_point, text3, text3_point, 60)
    pygame.time.delay(500)
    fadeOut(pygame, screen, text2, text2_point, text3, text3_point, None, None, 60)
    pygame.time.delay(500)
    fadeOut(pygame, screen, text3, text3_point, None, None, None, None, 60)
    pygame.time.delay(1000)
    # Refresh-Zeiten festlegen
    clock.tick(60)

    pygame.quit()

#main("hallo", "ballo", "knallo")
#main("never", "odd", "or even")
main("or even", "or even", "or even")