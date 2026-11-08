import pygame

class Snake:

    def __init__(self, bloco):
        self.corpo = [[360, 280]]

        self.vel_x = 0
        self.vel_y = 0

        self.prox_vel_x = 0
        self.prox_vel_y = 0

        self.espessura_cobra = 5
        self.bloco = bloco

    def move(self, comida):

        self.vel_x = self.prox_vel_x
        self.vel_y = self.prox_vel_y

        cabeca = self.corpo[0]

        nova_cabeca = [
            cabeca[0] + self.vel_x,
            cabeca[1] + self.vel_y
        ]


        if self.vel_x != 0 or self.vel_y != 0:
            self.corpo.insert(0, nova_cabeca)

            if self.corpo[0] != comida:
                self.corpo.pop()

    def draw(self, screen, cor):
        for pedaco in self.corpo:
            pygame.draw.rect(screen, cor, (pedaco[0], pedaco[1], self.bloco, self.bloco), self.espessura_cobra)


    def colisao(self):
        if self.corpo[0] in self.corpo[1:]:
            return True

        return False

    def colisao_parede(self, largura, altura):
       if self.corpo[0][0] < 0 or self.corpo[0][0] > largura - self.bloco or self.corpo[0][1] < 0 or self.corpo[0][1] > altura - self.bloco:
           return True

       return False


    def cima(self):
        if self.vel_y == 0:
            self.prox_vel_x = 0
            self.prox_vel_y = -self.bloco

    def baixo(self):
        if self.vel_y == 0:
            self.prox_vel_x = 0
            self.prox_vel_y = self.bloco

    def esquerda(self):
        if self.vel_x == 0:
            self.prox_vel_x = -self.bloco
            self.prox_vel_y = 0

    def direita(self):
        if self.vel_x == 0:
            self.prox_vel_x = self.bloco
            self.prox_vel_y = 0
