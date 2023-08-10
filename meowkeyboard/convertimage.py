from PIL import Image

# Open the PNG image
image = Image.open('meowkeyboard\catpawIcon.png')

# Convert to ICO format
image.save('meowkeyboard\catpawIcon.ico', format='ICO')
