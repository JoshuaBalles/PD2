# Livestock Detection

This repository contains code for detecting livestock in images and videos using deep learning models.

## Installation

1. Install Python 3.10.11. Make sure it's the only Python version installed or ensure that Python 3.10.11 is above other versions in your system's environment path if you want to keep other versions installed.

2. Clone this repository:

    ```bash
    git clone <repository link>
    ```

3. Open CMD and navigate to the cloned repository:

    ```bash
    cd <repository directory>
    ```

4. Create a Python virtual environment:

    ```bash
    python -m venv .venv
    ```

5. Activate the virtual environment:

    ```bash
    .venv\Scripts\activate
    ```

6. Install all required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- To run inference on images or videos, use the following command after putting the images or videos in the `input` folder:

    ```bash
    python -m livestock_detection
    ```

- To run inference on live video feed, use the following command:

    ```bash
    python -m camera_livestock_detection
    ```

    Press `q` to quit the inference.

## Results

All results are saved in the `runs/detect` folder.
