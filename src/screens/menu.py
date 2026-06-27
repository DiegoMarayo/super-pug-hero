import pygame
from src.const import WIN_WIDTH, MENU_OPTION, C_GOLDEN, WIN_HEIGHT, C_WHITE, C_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/menu.png')
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left = 0 , top = 0)

        self.move_sound = pygame.mixer.Sound('./assets/sounds/menu1.mp3')
        self.move_sound.set_volume(0.5)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./assets/sounds/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # Draw Images
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(26,"PRESS SPACE TO FLY", C_RED ,(WIN_WIDTH / 2, 630))

            # MENU
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], C_GOLDEN, ((WIN_WIDTH / 2), 700 + 60 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 700 + 60 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Event Down
                if event.type == pygame.KEYDOWN:
                    self.move_sound.play()
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    # Event Up
                    if event.key == pygame.K_UP:
                        self.move_sound.play()
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # Enter
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)