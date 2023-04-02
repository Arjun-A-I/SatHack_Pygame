import pygame
import cv2
import numpy as np
from Asl2Text import detect

letter_link = ['./sign-letters/letter-A.png', './sign-letters/letter-B.png',
               './sign-letters/letter-C.png', './sign-letters/letter-D.png', './sign-letters/letter-E.png',
               './sign-letters/letter-F.png', './sign-letters/letter-G.png', './sign-letters/letter-H.png',
               './sign-letters/letter-I.png', './sign-letters/letter-J.png', './sign-letters/letter-K.png',
               './sign-letters/letter-L.png', './sign-letters/letter-M.png', './sign-letters/letter-N.png',
               './sign-letters/letter-O.png', './sign-letters/letter-P.png', './sign-letters/letter-Q.png',
               './sign-letters/letter-R.png', './sign-letters/letter-S.png', './sign-letters/letter-T.png',
               './sign-letters/letter-U.png', './sign-letters/letter-V.png', './sign-letters/letter-W.png',
               './sign-letters/letter-X.png', './sign-letters/letter-Y.png', './sign-letters/letter-Z.png']

letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0

lvl1_letter = pygame.image.load(letter_link[count])
letter = letter_array[count]

home_icn = pygame.image.load('./images/home_icn.png')
home_icn = pygame.transform.scale(home_icn, (50, 50))

next_icn = pygame.image.load('./images/next.png')
next_icn = pygame.transform.scale(next_icn, (50, 50))

retry_icn = pygame.image.load('./images/retry.png')
retry_icn = pygame.transform.scale(retry_icn, (50, 50))

start_img = pygame.image.load('./images/start_btn.png')

apple_img = pygame.image.load('lv2_img/apple.png')
apple_img = pygame.transform.scale(apple_img, (300, 300))

banana_img = pygame.image.load('lv2_img/banana.png')
banana_img = pygame.transform.scale(banana_img, (300, 300))

lvl2_task = {1: banana_img, 2: apple_img, }
lvl2_word = {1: "banana", 2: "apple"}

lvl2_pointer = 1
pop = False
pop_text = ''
pop_bt1_txt = ''
pop_bt2_txt = ''
word = ''
flag = False

cam = cv2.VideoCapture(0)
# Initialize Pygame
pygame.init()
home = False
start_page = True
lvl1 = False
lvl2 = False
# Set up the window
screen_width = 1540
screen_height = 800
# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
window_size = (screen_width, screen_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Level Selector")
home_bg = pygame.image.load('./images/homee_1.png')
home2_bg = pygame.image.load('./images/homeee_1.png')

start_img = pygame.image.load('./images/start_btn.png')
pop_bg = pygame.image.load('./images/pop.png')

lvl1_bg = pygame.image.load('./images/lvl1_bg.png')
lvl2_bg = pygame.image.load('./images/lvl2_bg.png')


# Select level
select_level = pygame.image.load('./images/Selectlevel.png')
select_level = pygame.transform.scale(select_level, (600, 400))
select_level_rect = select_level.get_rect()
select_level_rect.center = ((screen_width//2), (screen_height//2))

lvlone_img = pygame.image.load('./images/lvl1.png')
lvlone_img = pygame.transform.scale(lvlone_img, (120, 120))
lvltwo_img = pygame.image.load('./images/lvl2.png')
lvltwo_img = pygame.transform.scale(lvltwo_img, (120, 120))


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Set up the font
start_button = Button(720, 550, start_img, 0.7)

font = pygame.font.Font(None, 50)


# Set up the buttons
button1 = pygame.Rect(600, 500, 100, 100)
button2 = pygame.Rect(820, 500, 100, 100)
button_home = pygame.Rect(51, 29, 95, 95)
word_rect = pygame.Rect(466, 706, 457, 70)

pop_btnl = pygame.Rect(250, 600, 200, 100)
pop_btnr = pygame.Rect(500, 600, 200, 100)

pop_rect = pygame.Rect(219, 195, 539, 528)
x = 20
y = 600
x2 = 1100
y2 = 50
move_count = 400

# Game loop
while True:

    # Handle events
    res, img = cam.read()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the Level 1 button is clicked
            if (home):
                if button1.collidepoint(event.pos):
                    print("BT1 CLICKED")
                    level1_screen = pygame.display.set_mode(window_size)
                    level1_screen.fill((255, 255, 255))
                    screen.blit(lvl1_bg, (0, 0))
                    # text = font.render("Level 1", True, (0, 0, 0))
                    # text_rect = text.get_rect(center=(250, 250))
                    # level1_screen.blit(text, text_rect)
                    home = False
                    lvl2 = False
                    lvl1 = True

                    pygame.display.update()
                # Check if the Level 2 button is clicked
                elif button2.collidepoint(event.pos):
                    print("BT2 CLICKED")
                    level2_screen = pygame.display.set_mode(window_size)
                    level2_screen.fill((255, 255, 255))
                    screen.blit(lvl2_bg, (0, 0))
                    # text = font.render("Level 2", True, (0, 0, 0))
                    # text_rect = text.get_rect(center=(250, 250))
                    # level2_screen.blit(text, text_rect)
                    home = False
                    lvl1 = False
                    lvl2 = True
                    pygame.display.update()
            if lvl1:
                if button_home.collidepoint(event.pos):
                    print("BT3 CLICKED")
                    home = True
                    start_page = False
                    lvl1 = False
                    pygame.display.update()

            if lvl2 and not pop:
                if button_home.collidepoint(event.pos):
                    print("HOME BTN CLICKED")
                    home = True
                    start_page = False
                    lvl1 = False
                    lvl2 = False
                    pygame.display.update()

            if pop:
                if pop_btnl.collidepoint(event.pos):
                    print("LEFt btn clicked")
                    lvl1 = False
                    lvl2 = False
                    home = True
                    pop = False

                if pop_btnr.collidepoint(event.pos):
                    print("RIGHT btn clicked")
                    if lvl2:
                        # lvl1=False
                        # lvl2=True
                        # home=False
                        pop = False
                        flag = True
                        if pop_bt2_txt == 'NEXT':
                            level2_screen = pygame.display.set_mode(
                                window_size)
                            level2_screen.fill((255, 255, 255))
                            screen.blit(lvl2_bg, (0, 0))
                            # text = font.render("Level 2", True, (0, 0, 0))
                            # text_rect = text.get_rect(center=(250, 250))
                            # level2_screen.blit(text, text_rect)
                            lvl2_pointer = lvl2_pointer + 1
                        else:
                            level2_screen = pygame.display.set_mode(
                                window_size)
                            level2_screen.fill((255, 255, 255))
                            screen.blit(lvl2_bg, (0, 0))
                            # text = font.render("Level 2", True, (0, 0, 0))
                            # text_rect = text.get_rect(center=(250, 250))
                            # level2_screen.blit(text, text_rect)
                    if lvl1:
                        # lvl1=False
                        # lvl2=True
                        # home=False
                        pop = False
                        flag = True
                        if pop_bt2_txt == 'NEXT':
                            level1_screen = pygame.display.set_mode(
                                window_size)
                            level1_screen.fill((255, 255, 255))
                            screen.blit(lvl1_bg, (0, 0))
                            # text = font.render("Level 1", True, (0, 0, 0))
                            # text_rect = text.get_rect(center=(250, 250))
                            # level1_screen.blit(text, text_rect)
                            count = count+1
                        else:
                            level1_screen = pygame.display.set_mode(
                                window_size)
                            level1_screen.fill((255, 255, 255))
                            screen.blit(lvl1_bg, (0, 0))
                            # text = font.render("Level 1", True, (0, 0, 0))
                            # text_rect = text.get_rect(center=(250, 250))
                            # level1_screen.blit(text, text_rect)
            if start_page:
                if start_button.draw():
                    print("START CLICKED")
                    home = True
                    start_page = False
                    pygame.display.update()
    if (home):
        girl = pygame.image.load('./images/Girl.png')
        girl = pygame.transform.scale(girl, (600, 600))

        screen.blit(home2_bg, (0, 0))
        screen.blit(girl, (70, 70))
        pygame.draw.rect(screen, (0, 0, 0), button1)
        pygame.draw.rect(screen, (255, 0, 0), button2)
        screen.blit(select_level, select_level_rect)
        screen.blit(lvlone_img, (600, 500))
        screen.blit(lvltwo_img, (820, 500))
        pygame.display.update()

    if (lvl1 and not pop):
        lvl1_letter = pygame.image.load(letter_link[count])
        lvl1_letter = pygame.transform.scale(lvl1_letter, (450, 450))
        letter = letter_array[count]
        print(count)
        frame, word = detect(img, flag)
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgRGB = cv2.resize(imgRGB, (539, 528))
        imgRGB = np.rot90(imgRGB)
        imgRGB = pygame.surfarray.make_surface(imgRGB).convert()
        screen.blit(imgRGB, (874, 195))
        # pygame.draw.rect(screen, (255, 255, ), button_home)
        # text1 = font.render("HOME", True, (0,0, 255))
        # text1_rect = text1.get_rect(center=button_home.center)
        print(word)
        if word.lower() == letter:
            print("HURRAY U MADE IT RIGHT :)")
            pop = True
            pop_text = 'HURRAY ! , U MADE IT :)'
            pop_bt1_txt = 'HOME'
            pop_bt2_txt = 'NEXT'
        elif word == '':
            print('continue')
        else:
            print("YOU MADE IT WRONG")
            word = ''
            pop = True
            pop_text = 'WRONG  :)'
            pop_bt1_txt = 'HOME'
            pop_bt2_txt = 'TRY AGAIN '
        # pygame.draw.rect(screen, (255, 0, 0), word_rect)
        # word_text = font.render(word,True, (0,0, 255))
        # word_text_rect = word_text.get_rect(center=word_rect.center)
        # screen.blit(text1,text1_rect)
        screen.blit(home_icn, (51, 29))
        # screen.blit(word_text,word_text_rect)
        screen.blit(lvl1_letter, (269, 245))
        pygame.display.update()

    if (lvl2 and not pop):
        print(pop)
        frame, word = detect(img, flag)
        flag = False
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgRGB = cv2.resize(imgRGB, (539, 528))
        imgRGB = np.rot90(imgRGB)
        imgRGB = pygame.surfarray.make_surface(imgRGB).convert()
        screen.blit(imgRGB, (898, 115))
        # pygame.draw.rect(screen, (255, 0, 0), button_home)
        text1 = font.render(" ", True, (0, 0, 255))
        text1_rect = text1.get_rect(center=button_home.center)
        pygame.draw.rect(screen, (255, 255, 255), word_rect)
        print(word)
        if word.lower() == lvl2_word[lvl2_pointer]:
            print("HURRAY U MADE IT RIGHT :)")
            pop = True
            pop_text = 'HURRAY ! , U MADE IT :)'
            pop_bt1_txt = 'HOME'
            pop_bt2_txt = 'NEXT'

        if word.lower() in lvl2_word[lvl2_pointer]:
            print("continue")
        elif word == '':
            print('continue')
        else:
            print("YOU MADE IT WRONG")
            word = ''
            pop = True
            pop_text = 'WRONG '
            pop_bt1_txt = 'HOME'
            pop_bt2_txt = 'TRY AGAIN '

        screen.blit(home_icn, (51, 29))
        word_text = font.render(word, True, (0, 0, 0))
        word_text_rect = word_text.get_rect(center=word_rect.center)
        screen.blit(text1, text1_rect)
        screen.blit(word_text, word_text_rect)
        obj = lvl2_task[lvl2_pointer]
        obj = pygame.transform.scale(obj, (450, 450))
        screen.blit(obj, (269, 165))
        pygame.display.update()

    if (pop):
        if lvl1:

            screen.blit(pop_bg, (219, 195))
            pop_btnl = pygame.Rect(250, 600, 200, 100)
            pop_btnr = pygame.Rect(500, 600, 200, 100)
            pop_rect = pygame.Rect(219, 195, 539, 528)
        else:
            screen.blit(pop_bg, (219, 115))
            pop_btnl = pygame.Rect(250, 600, 200, 50)
            pop_btnr = pygame.Rect(500, 600, 200, 50)
            pop_rect = pygame.Rect(219, 195, 539, 528)
        display_txt = font.render(pop_text, True, (0, 0, 0))
        dis_txt_rect = display_txt.get_rect(center=pop_rect.center)
        screen.blit(display_txt, dis_txt_rect)

        text1 = font.render(pop_bt1_txt, True, (121, 190, 191))
        text1_rect = text1.get_rect(center=pop_btnl.center)
        screen.blit(text1, text1_rect)
        screen.blit(home_icn, text1_rect)
        if pop_bt2_txt == "NEXT":

            text2 = font.render(pop_bt2_txt, True, (121, 190, 191))
            text2_rect = text2.get_rect(center=pop_btnr.center)
            screen.blit(text2, (600, 633))
            screen.blit(next_icn, (600, 633))
        else:

            text2 = font.render(pop_bt2_txt, True, (121, 190, 191))
            text2_rect = text2.get_rect(center=pop_btnr.center)
            print(text2_rect)
            screen.blit(text2, (600, 633))
            screen.blit(retry_icn, (600, 633))

        pygame.display.update()

    if (start_page):

        # pygame.display.update()
        hand = pygame.image.load('./images/Rectangle.png')
        boy = pygame.image.load('./images/Boy.png')

        if (y > move_count):
            screen.blit(home_bg, (0, 0))
            start_button.draw()
            screen.blit(hand, (x, y))
            screen.blit(boy, (x2, y2))
            y -= 5
            x2 -= 2
            pygame.display.update()
        else:
            screen.blit(home_bg, (0, 0))
            start_button.draw()
            screen.blit(hand, (x, y))
            screen.blit(boy, (x2, y2))
            pygame.display.update()
