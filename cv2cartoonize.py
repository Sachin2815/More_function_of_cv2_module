import cv2
import numpy as np

def cartoonize_image(image, gray_mode=False):
    # Convert image to grayscale
    if gray_mode:
        gray = image
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to reduce noise and smooth the image
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges in the image using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Create a color version of the image
    color = cv2.bilateralFilter(image, 9, 300, 300)
    
    # Combine the edges with the color image using a bitwise AND operation
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

def cartoonize_video():
    # Start video capture
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flip the frame horizontally for a more intuitive selfie view
        frame = cv2.flip(frame, 1)
        
        # Apply cartoonize effect to the frame
        cartoon_frame = cartoonize_image(frame)
        
        # Show the original and cartoonized frames side by side
        stacked_frames = np.hstack((frame, cartoon_frame))
        cv2.imshow("Cartoonizer", stacked_frames)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release video capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cartoonize_video()
    
