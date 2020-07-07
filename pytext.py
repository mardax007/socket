#!/usr/bin/python3
import pygame_textinput
import pygame
pygame.init()
print("hi")

# Create TextInput-object
textinput = pygame_textinput.TextInput()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))
    pygame.draw.rect(pygame.display.set_mode(720,720),(100,100,100),[pygame.display.set_mode(720,720).get_width()/2,pygame.display.set_mode(720,720).get_height()/2,140,40])
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))
    pygame.display.update()
    clock.tick(30)
