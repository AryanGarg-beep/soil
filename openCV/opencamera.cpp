#include <opencv4/opencv2/opencv.hpp>  // Use opencv4 if OpenCV 4 is installed
#include <iostream>

int main() {
    // Open the default camera (ID 0)
    cv::VideoCapture camera(0);

    // Check if the camera opened successfully
    if (!camera.isOpened()) {
        std::cerr << "ERROR: Could not open camera" << std::endl;
        return 1;
    }

    // Create a window to display the video feed
    cv::namedWindow("Webcam Feed", cv::WINDOW_AUTOSIZE);

    // Variable to store the current frame
    cv::Mat frame;

    // Loop to continuously capture and display frames
    while (true) {
        // Capture the next frame from the webcam
        camera >> frame;

        // Check if the frame was successfully captured
        if (frame.empty()) {
            std::cerr << "ERROR: Could not grab a frame" << std::endl;
            break;
        }

        // Display the current frame in the window
        cv::imshow("Webcam Feed", frame);

        // Exit the loop if any key is pressed
        if (cv::waitKey(10) >= 0) {
            break;
        }
    }

    // Release the camera when done
    camera.release();
    cv::destroyAllWindows();

    return 0;
}

