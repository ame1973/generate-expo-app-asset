from PIL import Image
from pathlib import Path

def resize_and_crop_icon(image, size):
    # Resize the image while preserving aspect ratio
    aspect_ratio = image.size[0] / image.size[1]
    new_width = int(aspect_ratio * size[1])
    resized_image = image.resize((new_width, size[1]), Image.ANTIALIAS)

    # Crop the image to the desired size
    left = (resized_image.size[0] - size[0]) / 2
    right = left + size[0]
    top = 0
    bottom = size[1]
    cropped_image = resized_image.crop((left, top, right, bottom))

    return cropped_image

def resize_and_center_logo(image, size):
    # Resize the image while preserving aspect ratio
    aspect_ratio = image.size[0] / image.size[1]
    new_height = int(size[0] / aspect_ratio)
    resized_image = image.resize((size[0], new_height), Image.ANTIALIAS)

    # Center the image
    background = Image.new("RGBA", size, (255, 255, 255, 0))
    offset = ((size[0] - resized_image.size[0]) // 2, (size[1] - resized_image.size[1]) // 2)
    background.paste(resized_image, offset)

    return background

Path("./asset").mkdir(parents=True, exist_ok=True)

# Load the original icon image
icon = Image.open("logo.png")

# Generate the 1600x1600 icon
icon_1600 = icon.resize((1600, 1600), Image.ANTIALIAS)
icon_1600.save("asset/icon.png")

# Generate the 1284x2778 splash
splash = Image.new("RGBA", (1284, 2778), (255, 255, 255, 0))
logo = resize_and_center_logo(icon, (265, 265))
offset = ((1284 - logo.size[0]) // 2, (2778 - logo.size[1]) // 3)
splash.paste(logo, offset)
splash.save("asset/splash.png")

# Generate the 48x48 favicon
favicon = resize_and_crop_icon(icon, (48, 48))
favicon.save("asset/favicon.png")

# Generate the 1600x1600 adaptive-icon
adaptive_icon = Image.new("RGBA", (1600, 1600), (255, 255, 255, 0))
icon_mask = resize_and_crop_icon(icon, (1600, 1600))
adaptive_icon.paste(icon_mask, (0, 0), icon_mask)
adaptive_icon.save("asset/adaptive-icon.png")