import pygame
import pygame_gui


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((1366, 768))
#users = ['profileDefault','blank']
#imgs = []
f = pygame.image.load("imagenes/med.jpg")
fondo = pygame.transform.scale(f,(1366, 768))
manager = pygame_gui.UIManager((1366, 768))

pic1 = pygame.image.load("imagenes/profileDefault.png")
prof1 = pygame.transform.scale(pic1, (100, 100))
pic2 = pygame.image.load("imagenes/blank.png")
prof2 = pygame.transform.scale(pic2, (100, 100))
#for user in users:
#    pic = pygame.image.load("imagenes/"+user+".jpg")
#    prof = pygame.transform.scale(f, (100,100))
#    imgs.append(prof)

#hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),text='Say Hello',manager=manager)
#hii = pygame_gui.elements.ui_text_entry_line(relative_rect=pygame.Rect((350, 275), (100, 50)),manager=manager)
#parts = 1366/len(imgs)
#for i in imgs:
#    window_surface.blit(i, (0, 0))
status=True
userInput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((623, 275), (120, 50)),manager=manager)
loginButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((623, 395), (120, 30)),text='->',manager=manager)
clock = pygame.time.Clock()

while True:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            status = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == loginButton:
                    print('Welcome')
        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(fondo, (0, 0))
    if status:
        window_surface.blit(prof1, (573, 279))
        window_surface.blit(prof2, (793, 279))
    else:
        pass
    manager.draw_ui(window_surface)

    pygame.display.update()