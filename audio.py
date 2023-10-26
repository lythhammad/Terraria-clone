import sys
sys.path.append("venv/lib/python3.11/site-packages")
import pygame

musicPath = "Assets/Audio/Music/"
soundPath = "Assets/Audio/Sounds/"
pygame.mixer.init()

class Audio:
    def __init__(self, filename):
        pygame.mixer.init()
        pygame.mixer.music.load(musicPath + filename)
        self.attackSound = pygame.mixer.Sound(soundPath + "Abigail_attack.wav")
        self.crySound = pygame.mixer.Sound(soundPath + "Abigail_cry_0.wav")
        self.summonSound = pygame.mixer.Sound(soundPath + "Abigail_summon.wav")
        self.achievementSound = pygame.mixer.Sound(soundPath + "Achievement_complete.wav")

    def __del__(self):
        pygame.mixer.music.unload()

    def play(self):
        pygame.mixer.music.play()

    def attack(self):
        pygame.mixer.Sound.play(self.attackSound)

    def cry(self):
        pygame.mixer.Sound.play(self.crySound)

    def summon(self):
        pygame.mixer.Sound.play(self.summonSound)

    def achievement(self):
        pygame.mixer.Sound.play(self.achievementSound)

# Test
audio_manager = Audio("28_RainAmbience.wav")

cond = 0
while (True):
    input()
    if cond == 0:
        audio_manager.play()
        cond = 2
    elif cond == 1:
        audio_manager.attack()
        cond = 2
    elif cond == 2:
        audio_manager.cry()
        cond = 3
    elif cond == 3:
        audio_manager.summon()
        cond = 4
    elif cond == 4:
        audio_manager.achievement()
        cond = 1

del audio_manager