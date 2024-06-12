from moviepy.editor import VideoFileClip

def cut_video(input_path, output_path, target_duration):
    """
    Schneidet ein Video auf eine angegebene Länge.
    
    :param input_path: Pfad zum Eingabevideo.
    :param output_path: Pfad zum Ausgabevideo.
    :param target_duration: Gewünschte Länge des Ausgabevideos in Sekunden.
    """
    # Lade das Video
    video = VideoFileClip(input_path)
    
    # Bestimme die tatsächliche Länge des Videos
    video_duration = video.duration
    
    # Schneide das Video nur, wenn die Länge des Videos größer ist als die gewünschte Länge
    if video_duration > target_duration:
        # Schneide das Video
        cut_video = video.subclip(0, target_duration)
    else:
        # Verwende das Originalvideo, falls es kürzer oder gleich lang wie die Zielzeit ist
        cut_video = video
    
    # Speichere das geschnittene Video
    cut_video.write_videofile(output_path, codec="libx264")

# Beispielnutzung
input_video_path = "input_video.mp4"  # Pfad zum Eingabevideo
output_video_path = "output_video.mp4"  # Pfad zum Ausgabevideo
desired_length = 30  # Gewünschte Länge in Sekunden

cut_video(input_video_path, output_video_path, desired_length)
