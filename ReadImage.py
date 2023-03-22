from PIL import Image
import numpy as np

def ReadImage(image_path: str, resize: float = 1.0) -> tuple[np.ndarray,
                                                             np.ndarray]:
    # Read in image as RGB just to show
    image_rgb = Image.open(image_path)

    # Resize RGB image
    w = int(image_rgb.width * resize)
    h = int(image_rgb.height * resize)
    image_rgb = image_rgb.resize((w, h))
    image_rgb = np.array(image_rgb)

    # Read in image as grayscale for operations
    image = Image.open(image_path).convert('L')

    # Resize gray image
    image = image.resize((w, h))

    # Store as array
    image = np.array(image)

    print(f'Read in {image_path}. Shape: {image.shape}')
    width = image.shape[1]
    height = image.shape[0]
    Image.fromarray(image)

    return image, image_rgb