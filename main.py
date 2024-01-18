"""chipi chipi chapa chapa"""

from os import startfile
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os


class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        startfile(self.path)


class MovieMP4(Video):
    type = "MP4"


class MusicMP3(Video):
    type = "MP3"


final = MovieMP4("final.mp4")
final.play()


# video_clip = VideoFileClip("Chipi_chipi_chapa_chapa_cat.mp4")
# audio_clip = AudioFileClip("chipichipi.mp3")
#
# final_clip = video_clip.set_audio(audio_clip)
#
# final_clip.write_videofile("final.mp4")

