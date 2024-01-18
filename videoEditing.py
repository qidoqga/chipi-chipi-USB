from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

video_clip = VideoFileClip("Chipi_chipi_chapa_chapa_cat.mp4")
audio_clip = AudioFileClip("chipichipi.mp3")

final_clip = video_clip.set_audio(audio_clip)

final_clip.write_videofile("final.mp4")
