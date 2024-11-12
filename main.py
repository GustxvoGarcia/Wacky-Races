import pygame, random, time 
from funcoes import mover_carros, cronometro_texto, carros_pista, posicao_inicial

pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("assets/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preta = (0,0,0)
fundo = pygame.image.load("assets/fundo.png")

carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")

movXCar1, movXCar2, = 25, 25
posYCar1, posYCar2, = 50, 180

while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXCar1,posYCar1))
    tela.blit(carro2, (movXCar2,posYCar2))
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    



