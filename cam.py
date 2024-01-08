from helpers import one_hot_output, to_letter, check_spell

import tensorflow as tf
import numpy as np

import time
import cv2


# Set the frame capture interval in seconds. Adjust for faster or slower interpreting
CAPTURE_INTERVAL = 2

# Open the webcam
cap = cv2.VideoCapture(0)

# Variable to keep track of the last processed time
last_processed_time = time.time()

# Load the trained neural network
model = tf.keras.models.load_model("trained_model.h5")

# List to store transcribed letters
letters = []

while True:
    # Capture current time
    current_time = time.time()

    # Capture frame
    _, frame = cap.read()

    # Capture frame only if the capture interval has passed
    if current_time - last_processed_time >= CAPTURE_INTERVAL:
        # Process frame to be fed to neural network
        _frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _frame = cv2.resize(_frame, (50, 50))
        _frame = _frame / 255.0
        _frame = np.reshape(_frame, (1, 50, 50))

        # Get neural network prediction
        pred = model.predict(_frame)
        pred = one_hot_output(pred[0])
        l = to_letter(pred)
        if l == " ":
            print(check_spell("".join(letters)))
            letters = []
        else:
            letters.append(l)

        # Reset timer
        last_processed_time = current_time

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
