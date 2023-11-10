
import os
import cv2

CROP_TOP = 10
CROP_BOT = 96-15
CROP_L = 5
CROP_R = 96-6

def process_images_in_directory(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)

        if os.path.isdir(file_path):
            # If it's a subdirectory, recursively process its contents
            subdirectory_output = os.path.join(output_directory, filename)
            process_images_in_directory(file_path, subdirectory_output)
        elif filename.endswith(".png"):  # You can adjust the file extension as needed
            # Read the image using OpenCV
            image = cv2.imread(file_path)

            if image is not None:
                # Resize the image to 96x96
                resized_image = cv2.resize(image, (96, 96))

                # Crop the image to [5:95, 5:91]
                cropped_image = resized_image[CROP_TOP:CROP_BOT, CROP_L:CROP_R]
                
                #resized_image = cv2.resize(cropped_image, (96, 96))

                # Save the cropped and resized image to the output directory
                output_path = os.path.join(output_directory, filename)
                cv2.imwrite(output_path, cropped_image)

                print(f"Processed and saved {filename} to {output_path}")
            else:
                print(f"Skipping {filename}: Unable to read the image")

# Example usage:
# Replace "input_root_directory" and "output_root_directory" with your root input and output directory paths
# process_images_in_directory("input_root_directory", "output_root_directory")
