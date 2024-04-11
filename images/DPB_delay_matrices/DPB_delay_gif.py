from PIL import Image
import glob

# Use the absolute path for the directory
plot_directory = "/home/Marc/Marc_network_sims/imgs/Results_Feb16/DPB_delay_matrices/"

# Updated glob pattern to match the new file naming convention
plot_files = sorted(
    glob.glob(plot_directory + "DPB_delay_noise_*.png"),
    key=lambda x: float(x.split("noise_")[-1].split(".png")[0]),
)

# Ensure that plot_files is not empty
if not plot_files:
    raise ValueError(
        f"No plot files found in directory {plot_directory}. Check your path and filename pattern."
    )

# Create an image list for the GIF
images = [Image.open(plot_file) for plot_file in plot_files]

# Ensure there are images to avoid IndexError
if images:
    # Save the images as an animated GIF
    images[0].save(
        plot_directory + "DPB_delay_animation.gif",
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=1000,
        loop=0,
    )
else:
    raise ValueError("No images loaded. Unable to create GIF.")
