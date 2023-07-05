# Rickrolling-with-Arduino-Uno-Rev-4-Wifi
Used the Arduino Uno Rev 4 Wifi's LED matrix to play a portion of Rick Astley's "Never Gonna Give you Up." It's not perfect but works well enough for the Rickroll.

[![Rickroll](https://github.com/RavaszEmber/Rickrolling-with-Arduino-Uno-Rev-4-Wifi/blob/main/output_frame.png)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

There are a few python scripts as well as the Arduino .ini file to upload to the board. Here's an outline
1. mp4ToBitmap.py takes an MP4 file and converts it into a 12 x 8 bitmap to be used on the Arduino Uno Rev 4 Wifi's LED matrix (since this is 12 x 8 LEDs). The bits here are determined by a threshold value for the 0's and 1's. I'd encourage you to look at cv2.adaptiveThreshold() as it will probably give clearer results than an arbitrary threshold value for all frames. Each frame from the video is save as a 12 x 8 bitmap in a /bmp folder.
2. Save frame as png.py *Optional* Used to save a frame from an mp4 as a png. This was just to check things on specific frames
3. Crop Black Bars.py *Optional* I had to use this because the original music video had black bars on the sides, which I wanted to remove. This python script uses ffmpeg to remove them. You don't need to use this unless you have the same black bar problem.
4. playBitmaps.py allows you to point to the /bmp folder and play the bitmaps back as a video. This is useful to see what your bitmaps will look like before porting it to the Arduino.
5. Bitmaps to binary arrays.py takes in your bmp folder and creates an output text file with all your frames in an array variable that you can copy straight into your Arduino code.
6. RickRoll.ino is the arduino code that you upload to your board. You need the Arduino_LED_Matrix library to drive the display. There isn't much to this file, just paste your frame array at the top and call it later in the loop. Note that I could only get ~1700 frames loaded before I ran out of RAM on the board, so you can likely only play part of your video, unless you reduce the framerate or come up with some cool compression to save on memory.

Feel free to use and alter this code for your own projects. If you do, please credit this repo.
