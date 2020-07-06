from interface.loadWindow import loadWindow
from interface.loginWindow import loginWindow
import pygame
from pygame.locals import *
import time
import threading
import pygame_gui

def loading():
    pygame.init()

    load = pygame.display.set_mode((1366, 768))
    logo = pygame.image.load("imagenes/LOGO.png")
    pygame.display.flip()
    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
        load.fill((255, 255, 255))
        load.blit(logo, (0, 0))
        pygame.display.update()
        time.sleep(3)
        break

def logining():
    pygame.init()

    pygame.display.set_caption('LOGIN')
    window_surface = pygame.display.set_mode((1366, 768))
    f = pygame.image.load("imagenes/med.jpg")
    fondo = pygame.transform.scale(f, (1366, 768))
    manager = pygame_gui.UIManager((1366, 768))
    pic1 = pygame.image.load("imagenes/profileDefault.png")
    prof1 = pygame.transform.scale(pic1, (100, 100))

    userInput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((623, 275), (120, 50)), manager=manager)
    passwordInput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((623, 335), (120, 50)), manager=manager)
    loginButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((623, 395), (120, 30)), text='->', manager=manager)
    clock = pygame.time.Clock()

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == loginButton:
                        validateUser(userInput.get_text(),passwordInput.get_text())
            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(fondo, (0, 0))
        window_surface.blit(prof1, (633, 165))
        manager.draw_ui(window_surface)
        pygame.display.update()

def validateUser(name,password):
    if name=='samuel' and password=='12345':
        quit()
def desktop():
    pass
if __name__ == '__main__':
    loading()
    logining()
    desktop()