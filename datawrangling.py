import cv2
import os

def blur_with_level(img, level, max_level=40):
    # just return if 0
    if level <= 0:
        return img.copy()

    max_sigma = 50

    sigma = (level / max_level) * max_sigma

    k = int(6 * sigma + 1)
    if k % 2 == 0:
        k += 1

    return cv2.GaussianBlur(img, (k, k), sigmaX=sigma, sigmaY=sigma)


def main():

    directory_path = "TestingData"
    blur_levels = [0, 10, 20, 30, 40]

    # filter images
    images = [
        f for f in os.listdir(directory_path)
        if f.lower().endswith((".jpeg", ".jpg"))
    ]

    # make folders
    for level in blur_levels:
        output_directory = f"BlurLevel_{level}"
        os.makedirs(output_directory, exist_ok=True)

    # load images
    for image in images:
        input_path = os.path.join(directory_path, image)
        img = cv2.imread(input_path)

        base_name, _ = os.path.splitext(image)

        for level in blur_levels:
            output_directory = f"BlurLevel_{level}"

            # blur (or copy if level=0)
            image_blurred = blur_with_level(img, level)

            # output path
            file_name = f"{base_name}_blur_{level}.jpg"
            full_output_path = os.path.join(output_directory, file_name)
            print(f"writing: {full_output_path}")
            cv2.imwrite(full_output_path, image_blurred)


if __name__ == "__main__":
    main()
