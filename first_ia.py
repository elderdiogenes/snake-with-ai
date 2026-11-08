from operator import itemgetter

class Ia:

    def __init__(self):
        self.time = 0
        self.dt = 0
        self.time1 = 0.01

    def ia(self, cobra, apple, game):

        self.cabeca = cobra.corpo[0]
        self.maca = apple.posicao
        caminhos = []
        caminhosGuardados = []

        esquerda, direita, cima, baixo = self.direcao_segura(cobra, game)

        lados = {
            "direita": direita,
            "esquerda": esquerda,
            "cima": cima,
            "baixo": baixo,
        }

        # print("\033[32mcomecou a previsao\033[m")
        self.previsao(3, self.cabeca, game, cobra, caminhos, caminhosGuardados)
        # print("\033[31mterminou a previsao\033[m")
        # print(len(caminhosGuardados))

        self.ordem_movimento(cobra, game, caminhosGuardados)


    def direcao_segura(self, cobra, game):

        self.cabeca = cobra.corpo[0]

        esquerda = (self.cabeca[0] - game.BLOCO < 0 or [self.cabeca[0] - game.BLOCO, self.cabeca[1]] in cobra.corpo)

        direita = (self.cabeca[0] + game.BLOCO > game.RESOLUCAOX - game.BLOCO or [self.cabeca[0] + game.BLOCO, self.cabeca[1]] in cobra.corpo)

        cima = (self.cabeca[1] - game.BLOCO < 0 or [self.cabeca[0], self.cabeca[1] - game.BLOCO] in cobra.corpo)

        baixo = (self.cabeca[1] + game.BLOCO > game.RESOLUCAOY - game.BLOCO or [self.cabeca[0], self.cabeca[1] + game.BLOCO] in cobra.corpo)

        return esquerda, direita, cima, baixo

    def ordem_movimento(self, cobra, game, caminhosGuardados):
        caminhosValidos = self.caminhosSemLoop(caminhosGuardados, game, cobra)

        self.time += self.dt

        for direcao in caminhosValidos:
            if self.time >= self.time1:
                getattr(cobra, direcao)()

            self.time = 0

    def proxMovimento(self, game, posicao, direcao):
        deslocamento = {
            "cima": (0, -game.BLOCO),
            "baixo": (0, game.BLOCO),
            "esquerda": (-game.BLOCO, 0),
            "direita": (game.BLOCO, 0)
        }

        x, y = deslocamento[direcao]
        novaCabeca = [posicao[0] + x, posicao[1] + y]
        return novaCabeca

    def posicao_segura(self, game, posicao, cobra):
        if posicao[0] < 0:
            return False
        if posicao[0] > game.RESOLUCAOX - game.BLOCO:
            return False
        if posicao[1] < 0:
            return False
        if posicao[1] > game.RESOLUCAOY - game.BLOCO:
            return False
        if posicao in cobra.corpo[:-1]:
            return False

        return True

    def previsao(self, passos, posicao, game, cobra, caminhos, caminhosGuardados, direcao_proibida=None):
        if passos == 0:
            caminhosGuardados.append(caminhos.copy())
            self.caminhosSemLoop(caminhosGuardados, game, cobra)
            return caminhosGuardados

        for direcao in ("cima", "baixo", "esquerda", "direita"):
            if direcao == direcao_proibida:
                continue
            novaPosicao = self.proxMovimento(game, posicao, direcao)


            if self.posicao_segura(game, novaPosicao, cobra):
                caminhos.append(direcao)

                if direcao == "cima":
                    prox_direcao_proibida = "baixo"
                elif direcao == "baixo":
                    prox_direcao_proibida = "cima"
                elif direcao == "esquerda":
                    prox_direcao_proibida = "direita"
                else:
                    prox_direcao_proibida = "esquerda"

                # print("Passo:", passos, "| Direção:", direcao, "| Posição:", novaPosicao)
                self.previsao((passos - 1), novaPosicao, game, cobra, caminhos, caminhosGuardados, prox_direcao_proibida)
                # print("\033[33mCaminhos:\033[m", caminhos)
                caminhos.pop()

    def caminhoSemLoop(self, caminho, game, cobra):
        posicao = self.cabeca.copy()
        posicaoVisitada = []

        for lado in caminho:
            novaPosicao = self.proxMovimento(game, posicao, lado)

            if novaPosicao in posicaoVisitada:
                return False, None

            if not self.posicao_segura(game, novaPosicao, cobra):
                return False, None

            posicaoVisitada.append(novaPosicao)

            posicao = novaPosicao

        return True, posicaoVisitada[-1]

    def caminhosSemLoop(self, caminhosGuardados, game, cobra):
        caminhosValidos = []

        for caminho in caminhosGuardados:
            resultado, posicaofinal = self.caminhoSemLoop(caminho, game, cobra)

            if resultado:
                distanciaMaca = (abs(posicaofinal[0] - self.maca[0]) + abs(posicaofinal[1] - self.maca[1])) / game.BLOCO
                caminhosValidos.append([caminho, distanciaMaca])

        caminhosValidos = sorted(caminhosValidos, key=itemgetter(1, 0))


# esta cheio de bugs, boa sorte XD.
        return caminhosValidos[0][0]

    def movimento(self, cobra, lados):
        if self.cabeca[1] > self.maca[1]:
            self.ordem_movimento(cobra, lados, ("cima", "esquerda", "direita", "baixo"))

        elif self.cabeca[1] < self.maca[1]:
            self.ordem_movimento(cobra, lados, ("baixo", "esquerda", "direita", "cima"))

        elif self.cabeca[0] > self.maca[0]:
            self.ordem_movimento(cobra, lados, ("esquerda", "cima", "baixo", "direita"))

        elif self.cabeca[0] < self.maca[0]:
            self.ordem_movimento(cobra, lados, ("direita", "cima", "baixo", "esquerda"))



'''

comece fazendo a IA escolher apenas uma direção por movimento real da cobra
em getattr

'''