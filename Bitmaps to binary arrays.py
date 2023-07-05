import os
from PIL import Image

# Input folder containing BMP images
input_folder = "RickRoll to Bitmap/bmp"

# Output text file path
output_file = "RickRoll to Bitmap/output.txt"


# Initialize the frames list
frames = []

# Get the list of BMP files in the input folder
bmp_files = [f for f in os.listdir(input_folder) if f.endswith('.bmp')]

# Process each BMP file
for bmp_file in bmp_files:
    # Open the BMP image
    bmp_path = os.path.join(input_folder, bmp_file)
    image = Image.open(bmp_path)

    # Convert the image to grayscale
    image = image.convert('L')

    # Resize the image to match the desired frame size
    frame_size = (12, 8)
    image = image.resize(frame_size, Image.ANTIALIAS)

    # Convert the image to a list of uint32_t hexadecimal values
    frame_values = []
    pixels = image.getdata()
    number = 0
    for i, pixel in enumerate(pixels):
        value = 1 if pixel < 128 else 0
        number |= (value << (31 - (i % 32)))
        if i % 32 == 31:
            frame_values.append(hex(number))
            number = 0

    # Add the frame values to the frames list
    #frame_values.append(hex(0)) #Trailing 0
    frames.append(frame_values)

# Save the frames to the output text file
with open(output_file, 'w') as file:
    file.write("uint32_t frames[][3] = {\n")
    for frame in frames:
        file.write("    {")
        file.write(", ".join(frame))
        file.write("},\n")
    file.write("};\n")

print("Output saved to", output_file)