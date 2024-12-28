import pygame
import sys
from PIL import Image
from bin.settings import *
from bin.game import Game
from bin.game_properties import Properties
from bin.audio import Audio
from bin.ui.button import Button


class MainMenu:
    def __init__(self):  # Конструктор класса
        # Инициализация Pygame
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Lobby")

        # Загрузка GIF и масштабирование его под размеры окна
        self.gif_frames = self.load_gif('resources/main.gif')
        self.num_frames = len(self.gif_frames)

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/main_font.ttf', WIDTH // 40)

        # Загрузка звука
        self.audio = Audio()
        self.hover_sound = self.audio.run("resources/on_button.mp3")
        self.lobby_music = self.audio.run("resources/lobby_music.mp3")

        self.last_hovered_button = None  # Для хранения последней кнопки, на которую наведен курсор

        # Проигрываем фоновую музыку
        self.lobby_music.play(-1)
        print(pygame.RESIZABLE)

    # Загрузка анимации из GIF
    def load_gif(self, filename):
        img = Image.open(filename)
        frames = []
        try:
            while True:
                frame = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
                frame = pygame.transform.scale(frame, (WIDTH, HEIGHT))  # Масштабируем кадр под начальное разрешение
                frames.append(frame)
                img.seek(len(frames))
        except EOFError:
            pass
        return frames

    def run(self):
        # Основной цикл
        clock = pygame.time.Clock()

        button = Button(self.screen)

        last_frame_time = pygame.time.get_ticks()  # Время последнего обновления кадра
        frame_duration = 100  # Длительность одного кадра GIF в миллисекундах
        current_frame = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lobby_music.stop()  # Остановить музыку при выходе
                    exit()

            # Отображение текущего кадра GIF
            scaled_frame = self.gif_frames[current_frame]
            self.screen.blit(scaled_frame, (0, 0))

            # Обновление текущего кадра с оптимизацией под FPS
            current_time = pygame.time.get_ticks()
            if current_time - last_frame_time >= frame_duration:  # Проверяем, прошло ли достаточно времени
                current_frame = (current_frame + 1) % self.num_frames  # Переход к следующему кадру
                last_frame_time = current_time  # Обновляем время последнего кадра

            # Отрисовка кнопок
            button_width = int(WIDTH * 0.25)
            button_height = int(HEIGHT * 0.1)

            if button.draw_button("Играть", (WIDTH - button_width) // 2, HEIGHT * 0.3, button_width, button_height,
                                  (0, 0, 0), (255, 0, 0)):
                self.lobby_music.stop()  # Остановка музыки при заходе в игру
                game = Game()
                game.run()

            if button.draw_button("Настройки", (WIDTH - button_width) // 2, HEIGHT * 0.45, button_width, button_height,
                                  (0, 0, 0), (255, 0, 0)):
                properties = Properties()
                properties.run()

            if button.draw_button("Выйти", (WIDTH - button_width) // 2, HEIGHT * 0.6, button_width, button_height,
                                  (0, 0, 0), (255, 0, 0)):
                self.lobby_music.stop()  # Остановка музыки при выходе
                pygame.quit()
                sys.exit()

            pygame.display.flip()  # Обновляем экран
            clock.tick(FPS)  # Установка FPS
