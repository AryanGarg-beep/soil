

# Specify the minimum version of CMake
cmake_minimum_required(VERSION 3.28.3)

# Set the project name
project(Flippedimg)

# Find OpenCV package
find_package(OpenCV REQUIRED)

# Include OpenCV headers
include_directories(${OpenCV_INCLUDE_DIRS})

# Set the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the executable
add_executable(test cvtest.cpp)

# Link OpenCV libraries
target_link_libraries(test ${OpenCV_LIBS})

