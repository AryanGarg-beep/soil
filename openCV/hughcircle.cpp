#include<iostream>
#include<opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
    // Load the image in color
    Mat image = imread("/home/aryan-garg/Pictures/circles.jpg");
    
    // Check if the image was loaded successfully
    if (image.empty()) {
        cerr << "ERROR: Could not open or find the image" << endl;
        return 1;
    }

    // Convert the image to grayscale (required for HoughCircles)
    Mat gray;
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // Apply Gaussian blur to reduce noise
    GaussianBlur(gray, gray, Size(9, 9), 2, 2);

    // Vector to store the circles
    vector<Vec3f> circles;

    // Apply Hough Circle Transform
    HoughCircles(
        gray,        // Input image (grayscale)
        circles,     // Output vector of circles
        HOUGH_GRADIENT,
        1,           // Inverse ratio of resolution
        gray.rows / 8,  // Minimum distance between detected centers
        200,         // Upper threshold for Canny edge detector
        50,          // Threshold for center detection
        0,           // Minimum radius to be detected
        0            // Maximum radius to be detected
    );

    // Draw the circles detected
    for (size_t i = 0; i < circles.size(); i++) {
        Vec3f circle = circles[i];
        Point center(cvRound(circle[0]), cvRound(circle[1]));
        int radius = cvRound(circle[2]);

        // Draw the center of the circle (green dot)
	cv::circle(image, center, 3, cv::Scalar(0, 255, 0), -1);

        // Draw the circle's perimeter (red outline)
	cv::circle(image, center, radius, cv::Scalar(0, 0, 255), 3);
    }

    // Create a window to display the image with circles
    namedWindow("Display Image with Circles", WINDOW_AUTOSIZE);
    imshow("Display Image with Circles", image);

    // Output the number of circles detected
    cout << "Number of circles detected: " << circles.size() << endl;

    // Wait for a key press
    waitKey(0);

    // Close all windows
    destroyAllWindows();

    return 0;
}

