import os
from PIL import Image


def to_gif(output_dir="output", duration=100):
    """
    Convert a series of PNG images in a specified directory into a GIF.
    """

    png_files = [os.path.join(output_dir, fn) for fn in sorted(os.listdir(output_dir)) if fn.endswith('.png')]
    if not png_files:
        raise FileNotFoundError("No PNG files found in the directory.")

    images = []
    for png_file in png_files:
        with Image.open(png_file) as img:
            images.append(img.convert('P'))

    images[0].save(
        "spacetime_curvature.gif",
        save_all=True,
        append_images=images[1:],
        loop=0,
        duration=duration
    )


if __name__ == "__main__":
    to_gif()
