import cv2

# Load the image
image = cv2.imread('checker.png')

# Get user input for new dimensions
new_width = int(input("Enter the new width: "))
new_height = int(input("Enter the new height: "))

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
output_filename = 'compressed_image.jpg'
cv2.imwrite(output_filename, resized_image)

# Display the original and resized images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image has been compressed and saved as '{output_filename}'")
