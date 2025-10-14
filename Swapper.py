import random
import pygame
import numpy as np


pygame.display.init()
pygame.mixer.init()

# WIDTH, HEIGHT = 2560, 1440
WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)) , pygame.RESIZABLE)
pygame.display.set_caption("OTHER SORT")

NumbersInArray = 1000
Sorter = [number for number in range(1, NumbersInArray + 1)]
random.shuffle(Sorter)

Color = (255,105,180)
print(Sorter)


RectWidth = WIDTH // NumbersInArray

FPS = 60
IsSorted = False
Run = True

audio_volume = 0.2  # Adjust this value as needed

# Load base beep sound once
base_sound = pygame.mixer.Sound('Sorting-algorithems/Beep2.wav')
base_sound.set_volume(audio_volume)
base_array = pygame.sndarray.array(base_sound)
sound_sample_rate = base_sound.get_length() / base_array.shape[0]

def play_beep_with_pitch(pitch_factor):
    # Resample array for pitch
    indices = np.round(np.arange(0, len(base_array), pitch_factor))
    indices = indices[indices < len(base_array)].astype(int)
    pitched_array = base_array[indices]
    sound = pygame.sndarray.make_sound(pitched_array)
    sound.set_volume(audio_volume)
    sound.play()

def Redo():
    global Sorter, IsSorted
    Sorter = [number for number in range(1, NumbersInArray + 1)]
    random.shuffle(Sorter)
    IsSorted = False
    print(Sorter)

while Run:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Redo()
            
    if IsSorted == False:
        WIN.fill((0, 0, 0))
        for Sorting in range(len(Sorter)):

            Numb = Sorter[Sorting] - 1
            Sorter[Sorting], Sorter[Numb] = Sorter[Numb], Sorter[Sorting]

            pitch = Sorter[Sorting] / NumbersInArray 
            pitch_factor = 1.0 / pitch
            play_beep_with_pitch(pitch_factor)
            RectHeight = (Sorter[Sorting] / NumbersInArray) * HEIGHT
            pygame.draw.rect(WIN, Color, (Sorting * RectWidth, HEIGHT - RectHeight, RectWidth, RectHeight))
            pygame.display.flip()
            
        if Sorter == sorted(Sorter):
            WIN.fill((0, 0, 0))
            for Sorting in range(len(Sorter)):

                pitch = Sorter[Sorting] / NumbersInArray 
                pitch_factor = 1.0 / pitch  
                play_beep_with_pitch(pitch_factor)

                RectHeight = (Sorter[Sorting] / NumbersInArray) * HEIGHT
                pygame.draw.rect(WIN, Color, (Sorting * RectWidth, HEIGHT - RectHeight, RectWidth, RectHeight))
            pygame.display.flip()
            IsSorted = True
            print("Sorted!")
            print(Sorter)



