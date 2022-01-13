
import moviepy.editor as mp

smile_path = 'smile/smile face.png'
music_path = 'audio/Freemasonry music.mp3'
video_path = 'video/Math equations blackboard.mp4'


audio = mp.AudioFileClip(music_path).subclip(0, 15)
video = mp.VideoFileClip(video_path).subclip(0, 15)
smile = mp.ImageClip(smile_path).set_position('center').set_duration(audio.duration).set_opacity(0.50)

final_video = mp.CompositeVideoClip([video.set_start('0:0:2'), smile])
final_video.audio = audio
final_video.write_videofile('output.mp4', fps = 30)
