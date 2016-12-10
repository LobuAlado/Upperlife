""" Pacotes """
import pygame
from pygame.locals import *
from sys import exit
import cores
import musicas
import resolucoes
import objetos

""" Inicializacao """
pygame.init()
menu_principal = pygame.display.set_mode(resolucoes.G1,0,32)
pygame.display.set_caption('Upperlife')

"""Imagens"""
logo = objetos.icone('Imagens/logo.png',170,220,400,40)
volume = objetos.icone('Imagens/volume_img.jpg',50,50,580,420)

"""Fontes  --- Corrigir"""
fonte = pygame.font.SysFont("comicsansms", 35)
titulo = fonte.render("Upperlife ", True, cores.verde)
iniciar = fonte.render("Play ", True, cores.branco)
fechar = fonte.render("Sair ", True, cores.branco)

""" Menu Principal"""
Switch_MENU = True
Switch_JOGO = False
Switch_BMG = True

if Switch_BMG:
    musicas.tocar_musica_menu()

while Switch_MENU:
    """Fecha o jogo ao clicar no X"""
    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()

        """Passa para a tela principal do jogo"""
        if pygame.mouse.get_pressed()[0]:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 0 and mouseX < 350:
                if mouseY < 250 and mouseY > 150:
                    Switch_MENU = False
                    Switch_JOGO = True

        """Fecha o jogo ao clicar no Sair"""
        if pygame.mouse.get_pressed()[0]:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 140 and mouseX < 640:
                if mouseY < 400 and mouseY > 300:
                    exit()

        """Liga/Desliga a musica"""
        if pygame.mouse.get_pressed()[0]:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 580 and mouseY > 420:
                if Switch_BMG:
                    musicas.desligar()
                else:
                    musicas.ligar()

    """Exibicao do menu"""
    menu_principal.fill(cores.branco)
    pygame.draw.rect(menu_principal, cores.verde, [0,150,300,100], 0)
    pygame.draw.rect(menu_principal,  cores.roxo, [140, 300, 500, 100], 0)
    menu_principal.blit(titulo,(20,20))
    menu_principal.blit(iniciar, (60, 200))
    menu_principal.blit(fechar, (180, 350))
    menu_principal.blit(logo.image,(logo.posx,logo.posy))
    menu_principal.blit(volume.image,(volume.posx, volume.posy))
    pygame.display.flip()

""" Tela do Jogo"""
tela = pygame.display.set_mode(resolucoes.G2,0,32)
pygame.display.set_caption('Upperlife :)')

"""Musica """
BMG_ON = True
if BMG_ON:
    musicas.tocar_musica_jogo()

"""Fontes"""
fonte = pygame.font.SysFont("comicsansms", 25)
fonte2 = pygame.font.SysFont("comicsansms", 45)
fonte3 = pygame.font.SysFont("comicsansms", 20)
textoa = fonte.render("Namorada ", True, cores.roxo)
textob = fonte.render("Amigos ", True, cores.roxo)
textoc = fonte.render("Familia ", True, cores.roxo)
textod = fonte.render("Escola ", True, cores.roxo)
textoe = fonte2.render("Minha energia ", True, cores.roxo)
textof = fonte3.render("Moral ", True, cores.roxo)

""" """
botao = pygame.font.SysFont("verdana", 14)
botao1 = botao.render("Mandar Mensagem", True, cores.branco)
botao2 = botao.render("Ligar", True, cores.branco)
botao3 = botao.render("Encontro", True, cores.branco)
botao4 = botao.render("Cumprimentar", True, cores.branco)
botao5 = botao.render("Jogar bola", True, cores.branco)
botao6 = botao.render("Cervejada", True, cores.branco)
botao7 = botao.render("Dar bom dia", True, cores.branco)
botao8 = botao.render("Limpar a casa", True, cores.branco)
botao9 = botao.render("Reuniao Familiar", True, cores.branco)
botao10 = botao.render("Colar", True, cores.branco)
botao11 = botao.render("Revisar materia", True, cores.branco)
botao12 = botao.render("10 na prova", True, cores.branco)
botao_energia = botao.render("Dormir", True,cores.branco)

points = 0
progress = 150
progress1 = 150
progress2 = 150
progress3 = 150
progress4 = 150
energy_progress = 740

Gameover = False

while Switch_JOGO:
    """Fecha o jogo ao clicar no X"""
    for evento in pygame.event.get():

        """ Detectar o clique do mouse botao 1"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 40 and mouseX < 180:
                if mouseY > 140 and mouseY < 220:
                        if progress1 <= 150:
                            if energy_progress > 0:
                                progress1 += 10
                                energy_progress -= 50
                                points += 25

        """ Detectar o clique do mouse botao 2"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 40 and mouseX < 180:
                if mouseY > 240 and mouseY < 320:
                    if progress1 <= 150:
                        if energy_progress > 0:
                            progress1 += 25
                            energy_progress -= 25
                            points += 50

        """ Detectar o clique do mouse botao 3"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 40 and mouseX < 180:
                if mouseY > 340 and mouseY < 420:
                    if progress1 <= 150:
                        if energy_progress > 0:
                            progress1 += 50
                            energy_progress -= 10
                            points += 100

        """ Detectar o clique do mouse botao 4"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 220 and mouseX < 370:
                if mouseY > 140 and mouseY < 220:
                    if progress2 <= 150:
                        if energy_progress > 0:
                            progress2 += 10
                            energy_progress -= 50
                            points += 25

        """ Detectar o clique do mouse botao 5"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 220 and mouseX < 370:
                if mouseY > 240 and mouseY < 320:
                    if progress2 <= 150:
                        if energy_progress > 0:
                            progress2 += 25
                            energy_progress -= 25
                            points += 50

        """ Detectar o clique do mouse botao 6"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 220 and mouseX < 370:
                if mouseY > 340 and mouseY < 420:
                    if progress2 <= 150:
                        if energy_progress > 0:
                            progress2 += 50
                            energy_progress -= 10
                            points += 100

        """ Detectar o clique do mouse botao 7"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 410 and mouseX < 560:
                if mouseY > 140 and mouseY < 220:
                    if progress3 <= 150:
                        if energy_progress > 0:
                            progress3 += 10
                            energy_progress -= 50
                            points += 25

        """ Detectar o clique do mouse botao 8"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 410 and mouseX < 560:
                if mouseY > 240 and mouseY < 320:
                    if progress3 <= 150:
                        if energy_progress > 0:
                            progress3 += 25
                            energy_progress -= 25
                            points += 50

        """ Detectar o clique do mouse botao 9"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 410 and mouseX < 560:
                if mouseY > 340 and mouseY < 420:
                    if progress3 <= 150:
                        if energy_progress > 0:
                            progress3 += 50
                            energy_progress -= 10
                            points += 100

        """ Detectar o clique do mouse botao 10"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 600 and mouseX < 750:
                if mouseY > 140 and mouseY < 220:
                    if progress4 <= 150:
                        if energy_progress > 0:
                            progress4 += 10
                            energy_progress -= 50
                            points += 25

        """ Detectar o clique do mouse botao 11"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 600 and mouseX < 750:
                if mouseY > 240 and mouseY < 320:
                    if progress4 <= 150:
                        if energy_progress > 0:
                            progress4 += 25
                            energy_progress -= 25
                            points += 50

        """ Detectar o clique do mouse botao 12"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 600 and mouseX < 750:
                if mouseY > 340 and mouseY < 420:
                    if progress4 <= 150:
                        if energy_progress > 0:
                            progress4 += 50
                            energy_progress -= 10
                            points += 100

        """Recarrega energia"""
        if evento.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if mouseX > 540 and mouseX < 750:
                if mouseY > 440 and mouseY < 500:
                        if energy_progress < 740:
                            energy_progress = 740

        """ Fechar o jogo"""
        if evento.type == QUIT:
            exit()

    """ Diminuir barras de status """
    if points <= 1000:
        if progress1 > 0:
            progress1 -= 0.005
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 1000 and points <= 5000:
        if progress1 > 0:
            progress1 -= 0.008
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 5000 and points <= 10000:
        if progress1 > 0:
            progress1 -= 0.01
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 10000 and points <= 20000:
        if progress1 > 0:
            progress1 -= 0.03
        else:
            Switch_JOGO = False
            Gameover = True
    else:
        if progress1 > 0:
            progress1 -= 0.05
        else:
            Switch_JOGO = False
            Gameover = True

    if points <= 1000:
        if progress2 > 0:
            progress2 -= 0.005
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 1000 and points <= 5000:
        if progress2 > 0:
            progress2 -= 0.008
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 5000 and points <= 10000:
        if progress2 > 0:
            progress2 -= 0.01
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 10000 and points <= 20000:
        if progress2 > 0:
            progress2 -= 0.03
        else:
            Switch_JOGO = False
            Gameover = True
    else:
        if progress2 > 0:
            progress2 -= 0.05
        else:
            Switch_JOGO = False
            Gameover = True

    if points <= 1000:
        if progress3 > 0:
            progress3 -= 0.005
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 1000 and points <= 5000:
        if progress3 > 0:
            progress3 -= 0.008
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 5000 and points <= 10000:
        if progress3 > 0:
            progress3 -= 0.01
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 10000 and points <= 20000:
        if progress3 > 0:
            progress3 -= 0.03
        else:
            Switch_JOGO = False
            Gameover = True
    else:
        if progress3 > 0:
            progress3 -= 0.05
        else:
            Switch_JOGO = False
            Gameover = True

    if points <= 1000:
        if progress4 >= 0:
            progress4 -= 0.005
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 1000 and points <= 5000:
        if progress4 >= 0:
            progress4 -= 0.008
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 5000 and points <= 10000:
        if progress4 >= 0:
            progress4 -= 0.01
        else:
            Switch_JOGO = False
            Gameover = True
    elif points > 10000 and points <= 20000:
        if progress4 >= 0:
            progress4 -= 0.03
        else:
            Switch_JOGO = False
            Gameover = True
    else:
        if progress4 >= 0:
            progress4 -= 0.05
        else:
            Switch_JOGO = False
            Gameover = True

    """Exibicao do Jogo"""
    tela.fill(cores.verde)
    pygame.draw.rect(tela,cores.branco,[20,20,760,560],0)
    """Primeira barra"""
    pygame.draw.rect(tela, cores.azul_claro, pygame.Rect(40, 80, 150, 15), 0)
    pygame.draw.rect(tela, cores.azul, pygame.Rect(40, 80, progress1,15))
    """Segunda barra"""
    pygame.draw.rect(tela, cores.azul_claro, pygame.Rect(220, 80, 150, 15), 0)
    pygame.draw.rect(tela, cores.azul, pygame.Rect(220, 80, progress2, 15))
    """Terceira barra"""
    pygame.draw.rect(tela, cores.azul_claro, pygame.Rect(420, 80, 150, 15), 0)
    pygame.draw.rect(tela, cores.azul, pygame.Rect(420, 80, progress3, 15))
    """Quarta barra"""
    pygame.draw.rect(tela, cores.azul_claro, pygame.Rect(620, 80, 150, 15), 0)
    pygame.draw.rect(tela, cores.azul, pygame.Rect(620, 80, progress4, 15))
    """Barra principal"""
    pygame.draw.rect(tela, cores.azul_claro, pygame.Rect(30, 520, 740, 45), 0)
    pygame.draw.rect(tela, cores.azul, pygame.Rect(30, 520, energy_progress, 45))

    if points <= 1000:
        """Botao 1"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(40, 140, 150, 80), 0)
        tela.blit(botao1, (50, 170))
        """Botao 4"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(220, 140, 150, 80), 0)
        tela.blit(botao4, (240, 170))
        """Botao 7"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(410, 140, 150, 80), 0)
        tela.blit(botao7, (420, 170))
        """Botao 10"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(600, 140, 150, 80), 0)
        tela.blit(botao10, (620, 170))

    if points > 1000 and points <= 5000:
        """Botao 1"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(40, 140, 150, 80), 0)
        tela.blit(botao1, (50, 170))
        """Botao 4"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(220, 140, 150, 80), 0)
        tela.blit(botao4, (240, 170))
        """Botao 7"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(410, 140, 150, 80), 0)
        tela.blit(botao7, (420, 170))
        """Botao 10"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(600, 140, 150, 80), 0)
        tela.blit(botao10, (620, 170))
        """Botao 2"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(40, 240, 150, 80), 0)
        tela.blit(botao2, (50, 270))
        """Botao 5"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(220, 240, 150, 80), 0)
        tela.blit(botao5, (240, 270))
        """Botao 8"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(410, 240, 150, 80), 0)
        tela.blit(botao8, (420, 270))
        """Botao 11"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(600, 240, 150, 80), 0)
        tela.blit(botao11, (620, 270))

    if points > 5000:
        """Botao 1"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(40, 140, 150, 80), 0)
        tela.blit(botao1, (50, 170))
        """Botao 4"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(220, 140, 150, 80), 0)
        tela.blit(botao4, (240, 170))
        """Botao 7"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(410, 140, 150, 80), 0)
        tela.blit(botao7, (420, 170))
        """Botao 10"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(600, 140, 150, 80), 0)
        tela.blit(botao10, (620, 170))
        """Botao 2"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(40, 240, 150, 80), 0)
        tela.blit(botao2, (50, 270))
        """Botao 5"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(220, 240, 150, 80), 0)
        tela.blit(botao5, (240, 270))
        """Botao 8"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(410, 240, 150, 80), 0)
        tela.blit(botao8, (420, 270))
        """Botao 11"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(600, 240, 150, 80), 0)
        tela.blit(botao11, (620, 270))
        """Botao 3"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(40, 340, 150, 80), 0)
        tela.blit(botao3, (50, 370))
        """Botao 6"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(220, 340, 150, 80), 0)
        tela.blit(botao6, (240, 370))
        """Botao 9"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(410, 340, 150, 80), 0)
        tela.blit(botao9, (420, 370))
        """Botao 12"""
        pygame.draw.rect(tela, cores.roxo, pygame.Rect(600, 340, 150, 80), 0)
        tela.blit(botao12, (620, 370))

    """Botao dormir"""
    pygame.draw.rect(tela, cores.verde, pygame.Rect(540, 440, 220, 60), 0)
    tela.blit(botao_energia, (560, 460))

    """ Labels"""
    tela.blit(textoa, (30, 20))
    tela.blit(textob, (210, 20))
    tela.blit(textoc, (410, 20))
    tela.blit(textod, (610, 20))
    tela.blit(textoe, (30, 450))
    tela.blit(textof, (30, 95))
    tela.blit(textof, (210, 95))
    tela.blit(textof, (410, 95))
    tela.blit(textof, (610, 95))

    pygame.display.flip()

""" Tela de Game Over"""
fonte = pygame.font.SysFont("comicsansms", 35)
mensagem = fonte.render(" GAME OVER ", True, cores.roxo)
fimgame = pygame.display.set_mode(resolucoes.G1,0,32)
pygame.display.set_caption("Game Over")
fonte = pygame.font.SysFont("comicsansms", 25)
pontuacao = fonte.render("Seus Pontos >> " + str(points),True,cores.roxo)

while Gameover:
    for evento in pygame.event.get():
        """ Fechar o jogo"""
        if evento.type == QUIT:
            exit()

    fimgame.fill(cores.branco)
    fimgame.blit(mensagem,(200,200))
    fimgame.blit(pontuacao,(200,250))
    pygame.display.flip()