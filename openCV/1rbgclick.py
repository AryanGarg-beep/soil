import cv2

# Function to display RGB values and the coordinates of the pixel clicked
def click_event(event, x, y, flags, param):
    # Check if the left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the BGR values from the image
        b, g, r = img[y, x]
        # Convert to RGB format (since OpenCV uses BGR)
        print(f"Coordinates: ({x}, {y}), RGB Values: ({r}, {g}, {b})")
        
        # Display the coordinates and RGB values on the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"RGB: ({r}, {g}, {b})"
        cv2.putText(img, text, (x, y), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)

# Load an image
img = cv2.imread('/home/aryan-garg/Pictures/0-0-255.jpg')  # Replace with your image path

# Create a window and bind the function to the mouse click event
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)

# Display the image until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

