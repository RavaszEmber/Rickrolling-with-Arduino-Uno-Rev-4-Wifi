import subprocess

# Input video file path
input_video = "C:/Users/benja/Downloads/Rick_Astley_Never_Gonna_Give_You_Up_Official_Music_Video.mp4"

# Output video file path
output_video = "C:/Users/benja/Downloads/Rick_Astley_Never_Gonna_Give_You_Up_Official_Music_Video_Cropped.mp4"

# Set the crop range to remove the black vertical bars
crop_range = "crop=in_w-2*90:in_h" # Adjust the crop range as needed. Here 90 pixels are removed from each side

# FFmpeg command to perform cropping and save as a new video
ffmpeg_cmd = f'ffmpeg -i {input_video} -vf "{crop_range}" -c:a copy {output_video}'

# Execute the FFmpeg command using subprocess
subprocess.call(ffmpeg_cmd, shell = True)