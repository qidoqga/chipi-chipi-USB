"""chipi chipi chapa chapa"""

import pygame
from moviepy.editor import VideoFileClip
import sys


def play_fullscreen(video_path, audio_path):
    # Initialize Pygame
    pygame.init()

    # Get the dimensions of the primary display
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

    # Set the display mode for the primary monitor
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.HWSURFACE)

    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Pygame movie surface
    movie_screen = pygame.Surface((screen_width, screen_height)).convert()

    clock = pygame.time.Clock()

    # Create a Pygame sound mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

    running = True

    # Play the video and audio on a loop until 'x' is pressed
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                running = False

        for frame in video_clip.iter_frames(fps=30, dtype="uint8"):
            resized_frame = pygame.transform.scale(pygame.surfarray.make_surface(frame.swapaxes(0, 1)),
                                                   (screen_width, screen_height))

            # Blit the frame to the screen
            movie_screen.blit(resized_frame, (0, 0))
            screen.blit(movie_screen, (0, 0))

            pygame.display.flip()
            clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    video_path = r"C:\Users\AMD\Desktop\final\Chipi_chipi_chapa_chapa_cat.mp4"
    audio_path = r"C:\Users\AMD\Desktop\final\chipi-chipi-chapa-chapa.mp3"
    play_fullscreen(video_path, audio_path)
