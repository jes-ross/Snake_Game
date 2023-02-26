''' 
Jesús Rosales Santana.
11/02/2023.
Crear una interfaz de usuario para validar usuario para jugar al snake. '''

#librerias
import pygame #esta libreria es de las mas usadas para hacer juegos en python.
import random #con esta libreria se posicionaran de manera aleatoria las manzanas.
#import interfaz

#Zona funciones
class cuerpo:
    def __init__(self, screen):#con esta clase definiremos posición y direcciones que tomará la serpiente
        self.x = 0
        self.y = 0
        self.screen = screen
        self.dir = 0
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, 10, 10))#con esto dibujamos el cuerpo
    def movement(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10

class manzanas:
    def __init__(self, screen):#con esta clase definiremos posición de las manzanas
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.screen = screen
    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0 ), (self.x, self.y, 10, 10))#con esto dibujamos el cuerpo
    def new_manzana(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10


def refresh(screen):
    screen.fill((0, 0, 0))
    food.draw()
    for i in range(len(snake)):
        snake[i].draw()

def snake_ubication():
    if(len(snake)) > 1:
        for i in range(len(snake) -1):
            snake[len(snake) - i - 1].x = snake[len(snake) - i - 2].x 
            snake[len(snake) - i - 1].y = snake[len(snake) - i - 2].y

def Colision():
    hit = False
    if len(snake) > 1:
        for i in range(len(snake) - 1):
            if snake[0].x == snake[i + 1].x and snake[0].y == snake[i + 1].y:
                hit = True
    return hit
def main():
    global snake, food
    screen = pygame.display.set_mode((400, 400))#con este comando se crea las proporciones de la pantalla
    screen.fill((0, 0, 0))#con este colores de la pantalla
    pygame.display.set_caption("Snake")
    snake = [cuerpo(screen)]
    snake[0].draw()
    food = manzanas(screen)
    refresh(screen)
  

    run = True
    velocidad = 100
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake[0].dir = 2
                if event.key == pygame.K_LEFT:
                    snake[0].dir = 1
                if event.key == pygame.K_RIGHT:
                    snake[0].dir = 0
                if event.key == pygame.K_UP:
                    snake[0].dir = 3
        snake_ubication()
        snake[0].movement()
        refresh(screen)
        pygame.display.update()
        pygame.time.delay(velocidad)

        if snake[0].x >= 400:
            snake[0].x = 0
        elif snake[0].x < 0:
            snake[0].x = 390
        if snake[0].y >= 400:
            snake[0].y = 0
        elif snake[0].y < 0:
            snake[0].y = 390

        if Colision():
            snake = [cuerpo(screen)]
            food.new_manzana()
            velocidad = 100
        
        if snake[0].x == food.x and snake[0].y == food.y:
            if velocidad > 35:
                velocidad -= 5
            food.new_manzana()
            snake.append(cuerpo(screen))
            snake_ubication()


main()
pygame.quit()