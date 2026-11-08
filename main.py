import pygame
from snake import Snake
from apple import Apple
from game import Game
from first_ia import Ia
# from operator import itemgetter

pygame.init()

game = Game()
cobra = Snake(game.BLOCO)
apple = Apple(game.BLOCO)
ia = Ia()

apple.posicao = game.gerar_comida(cobra.corpo)

while game.running:

#Movimento da cobra
    game.movimento(cobra)

# Cor do fundo
    game.screen.fill((9, 11, 25))

# Grade
    game.desenhar_grade(game.screen, game.screen.get_width(), game.screen.get_height(), game.BLOCO)

# Cobra
    cobra.draw(game.screen, game.CYAN)

# Maça
    apple.draw(game.screen)

# "tickrate" do jogo, e grow da cobra
    game.tickrate(cobra, apple)

#Ia
    game.ia_main(cobra, ia, apple, game)
    ia.direcao_segura(cobra, game)
# Colisao com parede
    game.colisao_parede(cobra)

# Gera a maça, checando se o numero escolhido para spawnar a maça esta no meio da cobra.
    game.gerar_posicao_comida(cobra, apple)

    pygame.display.flip()

    game.dt = game.clock.tick(60) / 1000
    ia.dt += game.dt
pygame.quit()

print(f"Você comeu {game.comidas_comida}/{game.comidastotal} maçãs")