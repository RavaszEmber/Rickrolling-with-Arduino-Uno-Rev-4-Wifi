import cv2
import os

# Folder containing the bitmaps
folder_path = "RickRoll to Bitmap/bmp"

# Sort the filenames in the folder numerically
bitmap_files = sorted(os.listdir(folder_path), key=lambda x: int(x.split('_')[2].split('.')[0]))

# Create a window to display the bitmaps
cv2.namedWindow('Bitmap Player', cv2.WINDOW_NORMAL)

# Iterate over the bitmap files and display them
for file_name in bitmap_files:
    # Read the bitmap image
    bitmap_path = os.path.join(folder_path, file_name)
    bitmap = cv2.imread(bitmap_path, cv2.IMREAD_GRAYSCALE)
    
    # Display the bitmap in the window
    cv2.imshow('Bitmap Player', bitmap)
    
    # Wait for a key press, with a delay of 100 milliseconds
    key = cv2.waitKey(100)
    
    # Break the loop if the 'q' key is pressed
    if key == ord('q'):
        break

# Close the window
cv2.destroyAllWindows()
