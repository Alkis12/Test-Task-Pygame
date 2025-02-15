import pygame


class Button:
    def __init__(self, x, y, width, height, text, n, color, click_color,
                 action=None, font_size=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.n = n
        self.color = color
        self.click_color = click_color
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, font_size)
        self.is_pressed = False
        self.active = True

    def draw(self, screen):
        if self.is_pressed:
            current_color = self.click_color
        else:
            current_color = self.color

        pygame.draw.rect(screen, current_color, self.rect, border_radius=15)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if self.is_mouse_on():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 2:
                    self.is_pressed = True
                else:
                    if self.n == -1:
                        # self.active = False
                        btns.clear()
                        oh_sorry()
                    else:
                        create_new_bro(self)

            elif event.type == pygame.MOUSEBUTTONUP and event.button != 2:
                if self.action:
                    self.action(self)
                self.is_pressed = False

    def is_mouse_on(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

coords = [(50, 50), (50, 250), (50, 450),
       (250, 50), (250, 450),
       (450, 50), (450, 250), (450, 450)]
act = [0, 0, 0, 0, 0, 0, 0, 0]

def create_new_bro(btn):
    for i in range(8):
        if act[i] == 0:
            n = i
            act[i] = 1
            break
    else:
        print("sorry, that's enough")
        return

    x, y = coords[n]
    new_btn = Button(x, y,
                    100, 100, f"Mini-Button-{n+1}",
                    n, (0, 0, 255), (0, 0, 0),
                    i_want_to_leave, 20)
    btns.append(new_btn)

def i_want_to_leave(btn):
    n = btn.n
    act[n] = 0
    btns.remove(btn)

def oh_sorry():
    new_main_btn = Button(50, 50,
                     500, 500, "QUIT (he-he)",
                     -1, (0, 0, 0), (255, 0, 0),
                     quit, 40)
    # конечно, вместо quit лучше функцию thank_you
    btns.append(new_main_btn)

def thank_you():  # quit
    global running
    running = False

    # pygame.quit()
    # exit()


main_btn = Button(200, 200,
                200, 200, "Create Button",
                -1, (0, 255, 0),(255, 0, 0),
                create_new_bro, 35)

btns = [main_btn]


running = True
while running:
    screen.fill((60, 60, 60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for x in btns:
            x.handle_event(event)

    for x in btns:
        if x.active:
            x.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
