import pygame
import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# Initialize Pygame
pygame.init()
home = True
lvl1 = False
# Set up the window
window_size = (1500, 700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Level Selector")


# Set up the font
font = pygame.font.Font(None, 50)


# Set up the buttons
button1 = pygame.Rect(150, 200, 200, 50)
button2 = pygame.Rect(150, 300, 200, 50)


# Game loop
while True:
    res,frame= cam.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    imgRGB = pygame.surfarray.make_surface(imgRGB).convert()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the Level 1 button is clicked
            if (home):
                if button1.collidepoint(event.pos):
                    if(home):
                        lvl1=True
                        home=False
                    else:
                        home = True
                        lvl1=False
                    # level1_screen = pygame.display.set_mode(window_size)
                    # level1_screen.fill((255, 255, 255))
                    # text = font.render("Level 1", True, (0, 0, 0))
                    # text_rect = text.get_rect(center=(250, 250))
                    # level1_screen.blit(text, text_rect)
                    # home = False
                    pygame.display.update()
                # Check if the Level 2 button is clicked
                elif button2.collidepoint(event.pos):
                    home = True
                    lvl1 = False
                    # level2_screen = pygame.display.set_mode(window_size)
                    # level2_screen.fill((255, 255, 255))
                    # text = font.render("Level 2", True, (0, 0, 0))
                    # text_rect = text.get_rect(center=(250, 250))
                    # level2_screen.blit(text, text_rect)
                    # home = False
                    pygame.display.update()

            if (lvl1):
                # if button1.collidepoint(event.pos):
                #     home = False
                #     lvl1 = True
                #     level1_screen = pygame.display.set_mode(window_size)
                #     level1_screen.fill((255, 255, 255))
                #     text = font.render("Level 1", True, (0, 0, 0))
                #     text_rect = text.get_rect(center=(250, 250))
                #     level1_screen.blit(text, text_rect)
                #     home = False
                #     pygame.display.update()
                # Check if the Level 2 button is clicked
                if button2.collidepoint(event.pos):
                    home = True
                    lvl1 = False
                    # level2_screen = pygame.display.set_mode(window_size)
                    # level2_screen.fill((255, 255, 255))
                    # text = font.render("HOME", True, (0, 0, 0))
                    # text_rect = text.get_rect(center=(250, 250))
                    # level2_screen.blit(text, text_rect)
                    # home = False
                    pygame.display.update()

    # Draw the buttons
    
    # Draw the button text
    if (home):
        pygame.draw.rect(screen, (255, 0, 0), button1)
        pygame.draw.rect(screen, (0, 255, 0), button2)
        text1 = font.render("Level 1", True, (255, 255, 255))
        text1_rect = text1.get_rect(center=button1.center)
        screen.blit(text1, text1_rect)
        text2 = font.render("Level 2", True, (255, 255, 255))
        text2_rect = text2.get_rect(center=button2.center)
        screen.blit(text2, text2_rect)
        pygame.display.update()
    
    if(lvl1):
        screen.blit(imgRGB, (800, 100))
        pygame.draw.rect(screen, (0, 255, 0), button2)
        text2 = font.render("HOME", True, (255, 255, 255))
        text2_rect = text2.get_rect(center=button2.center)
        screen.blit(text2, text2_rect)
        pygame.display.update()

    # Update the display
    #pygame.display.update()


