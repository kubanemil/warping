# Spacetime Curvature Visualization

This project visualizes the curvature of spacetime around a massive object using a Schwarzschild metric approximation. The program generates a series of plots that depict how spacetime is warped by varying Schwarzschild radii, then combines these images into a GIF to illustrate the dynamic effect of increasing mass on spacetime curvature.

## Project Structure

- `spacetime_curvature.py`: Main Python script that generates the plots.
- `to_gif.py`: Auxiliary Python script that converts the series of images into a GIF.
- `output/`: Directory containing the generated images and final GIF.


## Usage

To run the project, simply execute the script `main.py`. This will generate a series of images in the `output/` directory and compile these images into a GIF named `spacetime_curvature.gif`:



## How It Works

1. **Transformation Function**: The script defines a function `transform_coordinates` that models the bending of spacetime. It takes Cartesian coordinates and a Schwarzschild radius as input and outputs transformed coordinates based on the spacetime curvature effect.

2. **Image Generation**: For each frame, the script calculates the transformed grid for a given Schwarzschild radius and saves the resulting plot as an image.

3. **GIF Creation**: After all images are generated, they are compiled into a GIF using the `to_gif` function, which sequences the images based on the order of the Schwarzschild radius.

## Customization

- **Schwarzschild Radius Range**: You can adjust the `max_radius` and `frames` variables to change the range of the Schwarzschild radius and the number of frames in the GIF, respectively.

- **Grid Resolution**: Modify the `width` variable to change the resolution of the grid.

## Output

The final output is a GIF animation that shows how spacetime curvature intensifies as the Schwarzschild radius increases, representing an increasing mass of the central object.

## Contributions

Contributions to this project are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.


