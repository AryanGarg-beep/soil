import cv2

def show_camera_feed(camera_index=2):
    # Try to open the camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Cannot open camera at index {camera_index}")
        return

    print("Press 'q' to quit the camera feed.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If the frame is read correctly, ret is True
        if not ret:
            print("Failed to grab frame.")
            break
        
        # Display the resulting frame
        cv2.imshow("Camera Feed", frame)
        
        # Press 'q' on the keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()

# Example usage:
show_camera_feed(2)  # Replace 0 with the index of your camera

