import pygame

class Apple:

    def __init__(self, bloco):
        self.posicao = [0, 0]
        self.bloco = bloco

    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.posicao[0], self.posicao[1], self.bloco, self.bloco), 5, 5)