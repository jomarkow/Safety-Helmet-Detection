import os
from ultralytics import YOLO
import cv2

PROY_FOLDER = os.getcwd().replace("\\","/")

INPUT_FOLDER =  f"{PROY_FOLDER}/test/"
OUTPUT_FOLDER = f"{PROY_FOLDER}/test_output/"
MODEL_PATH =    f"{PROY_FOLDER}/output/best.pt"

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)
    
model = YOLO(MODEL_PATH) 
files = os.listdir(INPUT_FOLDER)


def draw_box(params, frame, threshold = 0.5):
    
    x1, y1, x2, y2, score, class_id = params
    
    if score > threshold:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)  
    
    return frame


for file_name in files:

    file_path = INPUT_FOLDER + file_name
    
    if "dfgdfg" in file_name:

        video_path_out = OUTPUT_FOLDER + file_name[:-4] + "_out.mp4"

        cap = cv2.VideoCapture(file_path)
        ret, frame = cap.read()
        H, W, _ = frame.shape
        out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

        while ret:

            results = model(frame)[0]
            for result in results.boxes.data.tolist():
                frame = draw_box(result, frame)
            out.write(frame) 
            ret, frame = cap.read()
            
        cap.release()
        out.release()
    
    elif ".jpg" in file_name:
        
        image_path_out = OUTPUT_FOLDER + file_name[:-4] + "_out.jpg"
        
        image = cv2.imread(file_path,cv2.IMREAD_COLOR) 
        results = model(image)[0]
        for result in results.boxes.data.tolist():
            image = draw_box(result, image)
            
        cv2.imwrite(image_path_out, image) 
    
    cv2.destroyAllWindows()
    


            
            
            