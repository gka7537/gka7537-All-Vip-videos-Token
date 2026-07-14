import cv2

def get_thumbnail(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    success, image = cap.read()
    if success:
        cv2.imwrite(output_path, image)
    cap.release()
    return output_path
  
