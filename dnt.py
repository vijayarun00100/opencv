import cv2

input_video = cv2.VideoCapture(r'C:\Users\vijay\Downloads\input.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(r'C:\Users\vijay\Downloads\DNT.mp4', fourcc, input_video.get(cv2.CAP_PROP_FPS), (int(
    input_video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))))

frame_count = 0
while True:
    ret, frame = input_video.read()
    if not ret:
        break
    if frame_count % 4 == 0:
        output_video.write(frame)
    frame_count += 1
input_video.release()
output_video.release()
