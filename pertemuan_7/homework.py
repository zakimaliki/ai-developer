import cv2 # type: ignore
import numpy as np # type: ignore

# Load the provided image
img = cv2.imread(r"C:\Users\malik\latihan-python\pertemuan_7\exercise.jpg")  # Path to your image

# Resize the image if necessary
img = cv2.resize(img, (600, 400))  # Adjust size as needed

# Draw a rectangle around the face
cv2.rectangle(img, (270, 10), (400, 180), (0, 255, 0), 2)  # Green rectangle (Face)

# Draw a rectangle around the laptop
cv2.rectangle(img, (350, 220), (550, 380), (255, 0, 0), 2)  # Blue rectangle (Laptop)

# Draw a circle around the cup
cv2.circle(img, (360, 348), 50, (0, 0, 255), 2)  # Red circle (Cup)

# Adding labels to each section
img = cv2.putText(img, "Face", (330, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
img = cv2.putText(img, "Laptop", (360, 210), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
img = cv2.putText(img, "Cup", (335, 290), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

# Show the result
cv2.imshow("Annotated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
