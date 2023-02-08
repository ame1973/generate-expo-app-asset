# Generate Expo app asset

using the Python Imaging Library (PIL) to generate Expo app asset

https://docs.expo.dev/tutorial/configuration/

1. 1600x1600 icon.png
2. 1284x2778 splash.png, icon place in the upper middle. the logo size is 265x265.
3. 48x48 favicon.png
4. 1600x1600 adaptive-icon.png

## Module

`pip install Pillow`

## How to use

Prepare a Logo image file (1:1 square). The best size is **larger than 1600x1600**.

1. Rename the logo file to `logo.png`, put to project root folder.

2. run the main.py

`python main.py`

3. export to project root folder.

`icon.png`, 
`splash.png`, 
`favicon.png`, 
`adaptive-icon.png`