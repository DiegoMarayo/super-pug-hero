import sys
import pygame
from src.const import WIN_WIDTH, MENU_OPTION, C_GOLDEN, WIN_HEIGHT, C_WHITE, C_RED, FONT_NAME
from src.utils.assets import Assets


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = Assets.image("menu.png", WIN_WIDTH, WIN_HEIGHT)
        self.rect = self.surf.get_rect(left = 0 , top = 0)
        self.move_sound = Assets.sound("menu1.mp3",0.5)
        self.info_font = Assets.font(FONT_NAME,26)
        self.menu_font = Assets.font(FONT_NAME,30)
        self.menu_selected_font = Assets.font(FONT_NAME,40)

    def run(self):
        selected_option = 0
        Assets.music("menu.mp3")
        pygame.mixer_music.play(-1)

        while True:
            # Draw Images
            self.window.blit(source=self.surf, dest=self.rect)
            self.draw_text(26,"PRESS SPACE TO FLY", C_RED ,(WIN_WIDTH / 2, 630))

            # MENU
            for index, option in enumerate(MENU_OPTION):

                if index == selected_option:
                    self.draw_text(40,option,C_GOLDEN,(WIN_WIDTH / 2, 700 + 60 * index))
                else:
                    self.draw_text(30,option,C_WHITE,(WIN_WIDTH / 2, 700 + 60 * index))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Event Down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.move_sound.play()
                        if selected_option < len(MENU_OPTION) - 1:
                            selected_option += 1
                        else:
                            selected_option = 0
                    # Event Up
                    elif event.key == pygame.K_UP:
                        self.move_sound.play()
                        if selected_option > 0:
                            selected_option -= 1
                        else:
                            selected_option = len(MENU_OPTION) - 1
                    elif event.key == pygame.K_RETURN: # Enter
                        self.move_sound.play()
                        return MENU_OPTION[selected_option]

    def draw_text(self, size, text, color, center):

        if size == 26:
            font = self.info_font
        elif size == 30:
            font = self.menu_font
        else:
            font = self.menu_selected_font

        surf = font.render(text,True,color).convert_alpha()

        rect = surf.get_rect(center=center)

        self.window.blit(surf,rect)