import cv2

# Input video file path
input_video = "C:/Users/benja/Downloads/Rick_Astley_Never_Gonna_Give_You_Up_Official_Music_Video_Cropped.mp4"

# Output PNG file path
output_image = 'output_frame.png'

# Desired frame number to save
desired_frame_number = 100

# Open the video file
video_capture = cv2.VideoCapture(input_video)

# Check if the video file opened successfully
if not video_capture.isOpened():
    print("Error opening video file")
    exit()

# Initialize a frame counter
frame_count = 0

# Read frames from the video until the desired frame number is reached
while frame_count < desired_frame_number:
    ret, frame = video_capture.read()
    if not ret:
        print("Error reading video frame")
        exit()
    frame_count += 1

# Save the desired frame as a PNG image
cv2.imwrite(output_image, frame)

# Release the video capture object
video_capture.release()

print(f"Frame {desired_frame_number} saved as", output_image)
