import os
from moviepy.editor import VideoFileClip

def split_video_into_segments(input_path, segment_duration):
    """
    Teilt ein Video in Abschnitte einer bestimmten Länge und speichert diese Teile in einem Unterordner,
    der den Namen des Eingabevideos trägt.
    
    :param input_path: Pfad zum Eingabevideo.
    :param segment_duration: Länge der Abschnitte in Sekunden.
    """
    # Extrahiere den Namen des Eingabevideos ohne Erweiterung
    input_filename = os.path.splitext(os.path.basename(input_path))[0]
    
    # Erstelle den Ausgabeordner basierend auf dem Namen des Eingabevideos
    output_folder = input_filename
    os.makedirs(output_folder, exist_ok=True)
    
    # Lade das Video
    video = VideoFileClip(input_path)
    
    # Bestimme die tatsächliche Länge des Videos
    video_duration = video.duration
    
    # Berechne die Anzahl der Segmente
    num_segments = int(video_duration // segment_duration)
    if video_duration % segment_duration != 0:
        num_segments += 1
    
    # Teile das Video in Segmente
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = start_time + segment_duration
        if end_time > video_duration:
            end_time = video_duration
        
        # Schneide das Video
        segment = video.subclip(start_time, end_time)
        
        # Speichere das Segment
        output_path = os.path.join(output_folder, f"{input_filename}_segment_{i+1}.mp4")
        segment.write_videofile(output_path, codec="libx264")
        print(f"Segment {i+1} gespeichert: {output_path}")

# Beispielnutzung
input_video_path = "input_video.mp4"  # Pfad zum Eingabevideo
segment_length = 30  # Länge der Abschnitte in Sekunden

split_video_into_segments(input_video_path, segment_length)
