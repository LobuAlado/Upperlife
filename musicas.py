import pygame
import pygame.mixer_music

"""Musica"""

def tocar_musica_menu():
    menu_song = pygame.mixer.music.load('BMG/menu_song.mp3')
    pygame.mixer.music.play(5, 0.0)

def tocar_musica_jogo():
    tema1 = pygame.mixer.music.load('BMG/tema1.mp3')
    pygame.mixer.music.play(5, 0.0)

def ligar():
    pygame.mixer.music.play(5, 0.0)
    Switch_BMG = True

def desligar():
    pygame.mixer.music.pause()
    Switch_BMG = False