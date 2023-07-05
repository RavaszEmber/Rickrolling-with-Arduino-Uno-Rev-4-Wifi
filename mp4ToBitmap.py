import cv2
import os

# Create the output folder if it doesn't exist
output_folder = "RickRoll to Bitmap/bmp"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file 
video_path = "C:/Users/benja/Downloads/Rick_Astley_Never_Gonna_Give_You_Up_Official_Music_Video_Cropped.mp4"
cap = cv2.VideoCapture(video_path)

# Initialize the frame counter
frame_count = 0

# Read and process frames
while cap.isOpened():
    # Read the current frame
    ret, frame = cap.read()

    # Check if the frame reading was successful
    if not ret:
        break

    # Resize the frame to 12x8 pixels
    frame = cv2.resize(frame, (12, 8))

    # Convert the frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image to get a binary image
    _, frame_binary = cv2.threshold(frame_gray, 127, 255, cv2.THRESH_BINARY) # Use adaptiveThreshold?
    
    # Save the frame as a bitmap
    output_path = os.path.join(output_folder, "output_frame_{:04d}.bmp".format(frame_count))
    cv2.imwrite(output_path, frame_binary)

    # Increment frame counter
    frame_count += 1

# Release the video object and close any open windows
cap.release()
cv2.destroyAllWindows()