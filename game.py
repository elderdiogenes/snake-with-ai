import pygame
import random

class Game:

    def __init__(self):

        self.RESOLUCAOX = 760
        self.RESOLUCAOY = 600

        self.screen = pygame.display.set_mode((self.RESOLUCAOX, self.RESOLUCAOY))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.time = 0
        self.tempo_acumulado = 0
        self.INTERVALO_DE_PASSO = 0.15
        self.comidas_comida = 0

        # self.dt_para_ia = self.dt
        self.tempo_acumulado_para_ia = 0
        self.INTERVALO_DE_PASSO_para_ia = 0.01

        self.BLOCO = 40
        self.ESPESSURA = 5
        self.comidastotal =  (self.RESOLUCAOX//self.BLOCO) * (self.RESOLUCAOY//self.BLOCO) - 1

        self.PURPLE = (89, 33, 208)
        self.CYAN = (8, 213, 248)
        self.GREEN = (111, 219, 73)
        self.YELLOW = (250, 209, 18)

    def desenhar_grade(self, janela, largura_tela, altura_tela, tamanho_BLOCO):
        for x in range(0, largura_tela, tamanho_BLOCO):
            pygame.draw.line(janela, (9, 5, 18), (x, 0), (x, altura_tela), self.ESPESSURA)

        for y in range(0, altura_tela, tamanho_BLOCO):
            pygame.draw.line(janela, (9, 5, 18), (0, y), (largura_tela, y), self.ESPESSURA)


    def gerar_comida(self, corpo):
        while True:
            x = random.randrange(0, self.RESOLUCAOX, self.BLOCO)
            y = random.randrange(0, self.RESOLUCAOY, self.BLOCO)

            if [x, y] not in corpo:
                return [x, y]

    def movimento(self, cobra):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cobra.cima()

                elif event.key == pygame.K_s:
                    cobra.baixo()

                elif event.key == pygame.K_a:
                    cobra.esquerda()

                elif event.key == pygame.K_d:
                    cobra.direita()

    def tickrate(self, cobra, apple):
        self.tempo_acumulado += self.dt

        if self.tempo_acumulado >= self.INTERVALO_DE_PASSO:
            cobra.move(apple.posicao)

            self.tempo_acumulado = 0

            if cobra.colisao():
                self.running = False

    def gerar_posicao_comida(self, cobra, apple):
        if cobra.corpo[0] == apple.posicao:
            apple.posicao = self.gerar_comida(cobra.corpo)
            self.comidas_comida += 1

    def colisao_parede(self, cobra):
        if cobra.colisao_parede(self.RESOLUCAOX, self.RESOLUCAOY):
                self.running = False

    def ia_main(self, cobra, ia, apple, game):

        self.tempo_acumulado_para_ia += self.dt

        if self.tempo_acumulado_para_ia >= self.INTERVALO_DE_PASSO_para_ia:
            ia.ia(cobra, apple, game)

            self.tempo_acumulado_para_ia = 0
