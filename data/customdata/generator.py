import os

from PIL import Image


def generate_file_list_and_shapes(image_folder, output_file, shapes_file):
    with open(output_file, "w") as f, open(shapes_file, "w") as sf:
        for root, _, files in os.walk(image_folder):
            for file in files:
                if file.endswith(
                    (".jpg", ".png", ".jpeg")
                ):  # Add other formats if necessary
                    image_path = os.path.join(root, file)
                    f.write(image_path + "\n")

                    # Get image dimensions
                    with Image.open(image_path) as img:
                        width, height = img.size
                        sf.write(f"{width} {height}\n")


original_path = "/app/yolo-midas-master/data/customdata"
# Paths to your folders
train_folder = original_path + "/train"
test_folder = original_path + "/test"

# Generate train.txt, test.txt, and their respective .shapes files
generate_file_list_and_shapes(
    train_folder, original_path + "/train.txt", original_path + "/train.shapes"
)
generate_file_list_and_shapes(
    test_folder, original_path + "/test.txt", original_path + "/test.shapes"
)

# Create custom.data
classes = 3  # Change this to your number of classes
custom_data_content = f"""\
classes = {classes}
train = {original_path}/train.txt
valid = {original_path}/test.txt
names = {original_path}/custom.names
"""
with open(original_path + "/custom.data", "w") as f:
    f.write(custom_data_content)

# Create custom.names
class_names = [
    "Boots",
    "Ear-protection",
    "Glass",
    "Glove",
    "Helmet",
    "Mask",
    "Person",
    "Vest",
]  # Replace with your actual class names
with open(original_path + "/custom.names", "w") as f:
    f.write("\n".join(class_names) + "\n")
