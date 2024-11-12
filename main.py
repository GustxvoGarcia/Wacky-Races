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
carro3 = pygame.image.load("assets/carro3.png")

movXCar1, movXCar2, movXCar3 = 25, 25, 25
posYCar1, posYCar2, posYCar3 = 50, 180, 110

vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1) #looping 3 vezes
acabou = False
somDaVitoria = False

while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
            
    posicao_inicial(branco, tela, fundo, carro1, carro2, carro3, movXCar1, movXCar2, movXCar3, posYCar1, posYCar2, posYCar3)
    
   
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,10)
        movXCar3 = movXCar3 + random.randint(0,10)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
          
    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 350
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 480
        
    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 400
        
     # Contador de distância
    distanciaPixel = 0
    if movXCar1 >= movXCar2 and movXCar1 >= movXCar3:
        firstPlace = 'Vermelho'
        if movXCar2 >= movXCar3:  # se o carro amarelo é o segundo colado
            distanciaPixel = abs(movXCar1 - movXCar2)
            secondPlace = 'Amarelo'
            thirdPlace = 'Azul'
            distancia_segundo_terceiro = abs(movXCar2 - movXCar3)
        else:  #o carro azul é o segundo colocado
            distanciaPixel = abs(movXCar1 - movXCar3)
            secondPlace = 'Azul'
            thirdPlace = 'Amarelo'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar2)

    elif movXCar2 >= movXCar1 and movXCar2 >= movXCar3:
        firstPlace = 'Amarelo'
        if movXCar1 >= movXCar3:  #se o carro vermelho é o segundo colocado
            distanciaPixel = abs(movXCar2 - movXCar1)
            secondPlace = 'Vermelho'
            thirdPlace = 'Azul'
            distancia_segundo_terceiro = abs(movXCar1 - movXCar3)
        else:  #o carro azul é o segundo colocado
            distanciaPixel = abs(movXCar2 - movXCar3)
            secondPlace = 'Azul'
            thirdPlace = 'Vermelho'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar1)

    else:  #o carro azul é o vencedor
        firstPlace = 'Azul'
        if movXCar1 > movXCar2:  #o carro vermelho é o segundo colocado
            distanciaPixel = abs(movXCar3 - movXCar1)
            secondPlace = 'Vermelho'
            thirdPlace = 'Amarelo'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar1)
        else:  #o carro amarelo é o segundo colocado
            distanciaPixel = abs(movXCar1 - movXCar2)
            secondPlace = 'Amarelo'
            thirdPlace = 'Vermelho'
            distancia_segundo_terceiro = abs(movXCar2 - movXCar1)

    #textos winners função
    cronometro_texto(tela, firstPlace, secondPlace, thirdPlace, distanciaPixel, distancia_segundo_terceiro, branco)
    #funcao que atualiza os carros para as posicoes da segunda pista
    movXCar1, movXCar2, movXCar3, posYCar1, posYCar2, posYCar3 = carros_pista(movXCar1, movXCar2, movXCar3, posYCar1, posYCar2, posYCar3)
        
    fonte = pygame.font.Font('freesansbold.ttf',60)#ttf é o arquivo da font
    textoVermelho = fonte.render('Vermelho Ganhou!', True, branco)
    textoAmarelo = fonte.render('Amarelo Ganhou!', True, branco)
    textoAzul = fonte.render('Azul Ganhou!', True, branco)
        
    
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    



