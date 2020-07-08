import cv2

video_file_name= ".mp4"

video = cv2.VideoCapture(video_file_name)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,640))
first_frame=None
while True:
    print("haii")
    motion=0
    motion_status=False
    status,frame = video.read()
    # width,height,channel = frame.shape
    if frame is not None:
        print(frame.shape)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        if first_frame is None:
            first_frame=gray
            continue


        difference = cv2.absdiff(first_frame, gray)
        thresh = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        image,cnts,heir = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 1000:
                continue
            motion = 1

            (x, y, w, h) = cv2.boundingRect(contour)
            # making green rectangle arround the moving object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if motion==1:
            motion_status=True
            print("motion status ",motion_status)
            # frame = frame.resize(640,480)
            out.write(frame)
            print("video writing")

    else:
        break
video.release()

out.release()