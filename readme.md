# Bicep Counter Project

## Overview

The **Bicep Counter** is a computer vision project that uses MediaPipe Pose Estimation to count bicep curls in a video. The program detects human poses, calculates angles at key joints, and tracks progress through visual feedback, including live counters and progress bars. It is designed to demonstrate how machine learning and computer vision can be used to analyze human movement.

## Features

- **Pose Detection:** Uses MediaPipe's Pose module to identify key landmarks on the human body.
- **Angle Calculation:** Calculates angles between specified joints (e.g., shoulder, elbow, and wrist) to track bicep curls.
- **Repetition Counter:** Automatically counts bicep curls based on the movement of the arm.
- **Progress Bar:** Displays the user's progress for each curl.
- **FPS Display:** Shows the frame rate of the video processing.
- **Visual Feedback:** Overlays progress, angle, and count directly on the video.

## Installation

### Prerequisites

1. Python 3.7 or higher
2. Libraries:
    - OpenCV
    - NumPy
    - MediaPipe

### Steps

1. Clone the repository:
    
    ```
    git clone https://github.com/your-repo/bicep-counter.git
    cd bicep-counter
    ```
    
2. Install the required dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    
3. Place your video file in the `videos/` directory. For example, `videos/bicep.mp4`.

## Usage

### Running the Bicep Counter

To run the main program:

```
python bicepcounter.py
```

### Module Testing

To test the pose detection module:

```
python moduletesting.py
```

## Project Structure

```
|-- bicepcounter.py            # Main script for counting bicep curls
|-- moduletesting.py           # Script to test pose detection functionality
|-- posestimationmodule.py     # Module containing PoseDetector class
|-- videos/                    # Directory for input video files
|-- requirements.txt           # List of Python dependencies
```

## How It Works

1. **Pose Detection**
    - MediaPipe's Pose module detects 33 landmarks on the body.
2. **Angle Calculation**
    - The angle between the shoulder, elbow, and wrist landmarks is calculated to determine arm movement.
3. **Repetition Counting**
    - The program tracks the arm's angle to detect when a full curl is completed.
    - A curl is counted when the angle transitions from maximum to minimum and back.
4. **Visual Feedback**
    - Progress bars, counters, and FPS are overlaid on the video for real-time feedback.

## Key Classes and Methods

### `PoseDetector` (posestimationmodule.py)

- **Methods:**
    - `findPose(img, draw=True)`: Detects pose landmarks in the image.
    - `findPosition(img, draw=True)`: Returns a list of detected landmarks.
    - `findAngle(img, p1, p2, p3, draw=True)`: Calculates the angle between three landmarks.

### Utility Functions

- **`draw_text_with_background`**
    - Draws text with a rectangle background for better visibility.

## Example Output

The program displays the following:

- Live video with pose landmarks and movement annotations.
- A counter showing the number of bicep curls completed.
- A progress bar indicating the arm's movement in real-time.
- The frame-per-second (FPS) rate for smoothness analysis.

## Known Issues

- **Feedback Manager Warnings:** Warnings related to TensorFlow Lite feedback manager may appear but do not affect functionality.
- **Pose Detection Failures:** Ensure good lighting and visibility of the person in the video for optimal detection.

## Future Improvements

- Add support for live webcam input.
- Enhance robustness to handle videos with varying angles or occlusions.
- Integrate more advanced feedback mechanisms, such as counting reps for multiple users.
- Extend functionality to other exercises.