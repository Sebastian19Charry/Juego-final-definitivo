import pygame
import sys
import random

pygame.init()

# Musica
pygame.mixer.music.load('Bourgueoise.mp3')
pygame.mixer.music.play(-1)


# Ventana
width, height = 1066, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RythmoTouch")
fondo = pygame.image.load('fondo_juego.jpg')


# Colores
black = (25, 30, 40)
white = (228, 227, 230)
red = (254, 4, 129)
green = (52, 210, 40)
blue = (13, 227, 231)
yellow = (253, 194, 26)


# Configuración del reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()


# Generacion de circulos 
circle_radius = 20
circle_speed = 3.6  
spawn_rate = 8  


# Aparicion de notas
note_timings = {
    0: [],
    1: [],
    2: [],
    3: [],
}

last_note_time = pygame.time.get_ticks()
next_note_time = 0  # Tiempo aparicion


# Circulos aleatorios
def generate_circle(x, color):
    return {'x': x, 'y': 0, 'color': color}

circles = []


# Botones
button_radius = 30
button_spacing = 150
buttons = [
    {'x': width // 5, 'y': height - 50, 'color': red, 'arrow': pygame.image.load('f_izquierda.png')},
    {'x': 2 * width // 5, 'y': height - 50, 'color': green, 'arrow': pygame.image.load('f_derecha.png')},
    {'x': 3 * width // 5, 'y': height - 50, 'color': blue, 'arrow': pygame.image.load('f_arriba.png')},
    {'x': 4 * width // 5, 'y': height - 50, 'color': yellow, 'arrow': pygame.image.load('f_abajo.png')},
]

for button in buttons:
    button['arrow'] = pygame.transform.scale(button['arrow'], (60, 60))  # Ajuste del tamaño de las flechas


# Fuente_Puntaje
retro = pygame.font.Font("retro.ttf", 30)

score = 0


#Puntaje
def update_score():
    score_text = retro.render(f"Puntaje: {score}", True, white)
    screen.blit(score_text, (20, 20))


#Fondo_pantalla    
background = pygame.image.load('fondo_juego.jpg')
background = pygame.transform.scale(background, (width, height))


#Pausa
paused = False 


# Bucle principal del juego
def main():
    global last_note_time
    global next_note_time
    global score
    global paused 

    while True:
        current_time = pygame.time.get_ticks()
        time_passed = current_time - last_note_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    
                    paused = not paused 
                         
        if not paused: 

            keys = pygame.key.get_pressed()

            # Movimiento de las flechas
            for i, button in enumerate(buttons):
                if keys[pygame.K_LEFT] and i == 0:
                    if note_timings[i] and current_time - note_timings[i][-1] < 500:  
                        for circle in circles[::-1]:
                            if circle['x'] == button['x'] and circle['y'] > height - 70:
                                score += 10
                                circles.remove(circle)
                                break
                elif keys[pygame.K_RIGHT] and i == 1:
                    if note_timings[i] and current_time - note_timings[i][-1] < 500:
                        for circle in circles[::-1]:
                            if circle['x'] == button['x'] and circle['y'] > height - 70:
                                score += 10
                                circles.remove(circle)
                                break
                elif keys[pygame.K_UP] and i == 2:
                    if note_timings[i] and current_time - note_timings[i][-1] < 500:
                        for circle in circles[::-1]:
                            if circle['x'] == button['x'] and circle['y'] > height - 70:
                                score += 10
                                circles.remove(circle)
                                break
                elif keys[pygame.K_DOWN] and i == 3:
                    if note_timings[i] and current_time - note_timings[i][-1] < 500:
                        for circle in circles[::-1]:
                            if circle['x'] == button['x'] and circle['y'] > height - 70:
                                score += 10
                                circles.remove(circle)
                                break
            
            
            screen.blit(background, (0, 0))
        

            # Lineas verticales
            line_width = 5
            num_lines = 4
            line_spacing = width // (num_lines + 1)

            for i in range(1, num_lines + 1):
                x = i * line_spacing
                pygame.draw.line(screen, white, (x, 0), (x, height), line_width)
                

                # Tiempo aleatorio
                if time_passed > next_note_time and len(note_timings[i - 1]) < 5:
                    if not note_timings[i - 1] or current_time - note_timings[i - 1][-1] > 3000:
                        note_timings[i - 1].append(current_time + random.randint(3000, 5000))
                        last_note_time = current_time
                        next_note_time = random.randint(1500, 3000)

        
            # Notas
            for i, notes in enumerate(note_timings.values()):
                for note_time in notes[:]:
                    if current_time > note_time:
                        note_timings[i].remove(note_time)
                        circles.append(generate_circle((i + 1) * line_spacing, buttons[i]['color']))
                        break 


            # Circulos
            for circle in circles[:]:
                pygame.draw.circle(screen, circle['color'], (circle['x'], circle['y']), circle_radius)
                circle['y'] += circle_speed


                # Eliminar circulos
                if circle['y'] > height:
                    circles.remove(circle)


            # Botones
            for button in buttons:
                pygame.draw.circle(screen, button['color'], (button['x'], button['y']), button_radius)
                screen.blit(button['arrow'], (button['x'] - button['arrow'].get_width() // 2, button['y'] - 30))


            # Actualizar puntaje
            update_score()
            
            
            
            pygame.display.flip()

            clock.tick(60)
        

if __name__ == "__main__":
    main()