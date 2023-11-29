import pygame
import subprocess
import sys

pygame.init()
pygame.display.set_caption("RythmoTouch")


# Pantalla
ancho_pantalla = 1066
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
fondo = pygame.image.load('fondo.jpg')
fondo = pygame.transform.scale(fondo, (ancho_pantalla, alto_pantalla))

# Colores
color_boton = (85, 18, 82)
color_borde = (255, 255, 255)


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_play.collidepoint(evento.pos):
                print("Botón Play presionado!")
                
                subprocess.Popen(["python", "main.py"])

            if boton_exit.collidepoint(evento.pos):
                print("Botón Exit presionado!")
                sys.exit()


    pantalla.blit(fondo, (0, 0))

    # Creacion de botones
    boton_play = pygame.Rect(ancho_pantalla / 2 - 150, alto_pantalla / 1.5 - 40, 300, 80)
    boton_exit = pygame.Rect(ancho_pantalla / 2 - 150, alto_pantalla / 1.5 + 40, 300, 80)

    # Dibujar los botones
    pygame.draw.rect(pantalla, color_borde, boton_play, border_radius=10, width=2)
    pygame.draw.rect(pantalla, color_boton, boton_play.inflate(-4, -4), border_radius=8)

    pygame.draw.rect(pantalla, color_borde, boton_exit, border_radius=10, width=2)
    pygame.draw.rect(pantalla, color_boton, boton_exit.inflate(-4, -4), border_radius=8)


    # Texto
    font = pygame.font.Font('retro.ttf', 36)
    text_play = font.render("Jugar", True, color_borde)
    text_exit = font.render("Salir", True, color_borde)
    pantalla.blit(text_play, (boton_play.x + boton_play.width // 2 - text_play.get_width() // 2,
                              boton_play.y + boton_play.height // 2 - text_play.get_height() // 2))
    pantalla.blit(text_exit, (boton_exit.x + boton_exit.width // 2 - text_exit.get_width() // 2,
                              boton_exit.y + boton_exit.height // 2 - text_exit.get_height() // 2))


    # Título
    font_titulo = pygame.font.Font('retro.ttf', 124)
    text_titulo = font_titulo.render("RythmoTouch", True, color_borde)
    pantalla.blit(text_titulo, (ancho_pantalla / 2 - text_titulo.get_width() // 2, alto_pantalla / 6))

    pygame.display.flip()

pygame.quit()
