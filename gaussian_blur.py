import cv2
import numpy as np

def clamp(value):
    return max(0, min(255, int(value)))

def gaussian_blur(image):
    height, width, channels = image.shape

    # Define the 3x3 Gaussian kernel
    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ], dtype=np.float32) / 16.0

    # Output image
    blurred = np.zeros_like(image)

    # Apply convolution (skip border)
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            for c in range(channels):  # For each channel (B, G, R)
                region = image[y - 1:y + 2, x - 1:x + 2, c]
                value = np.sum(region * kernel)
                blurred[y, x, c] = clamp(value)

    return blurred

# Load image
image = cv2.imread('./photos/cat.jpeg')  # Make sure this path is correct
if image is None:
    raise ValueError("Image not found. Check the path.")

# Apply Gaussian Blur
blurred_image = gaussian_blur(image)

# Save and show result
cv2.imwrite('gaussian_output.jpg', blurred_image)
# cv2.imshow('Original', image)
h = np.hstack((image, blurred_image))
cv2.imshow('Original & Gaussian Blurred', h)
cv2.waitKey(0)
cv2.destroyAllWindows()
