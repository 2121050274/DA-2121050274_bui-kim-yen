from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2 
import os 
import numpy as np

class Train :
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbt = Label(self.root, text="HUẤN LUYỆN DỮ LIỆU" , font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbt.place(x=0 , y=0 , width=1530, height=45) 

        img_top=Image.open(r"college_images/facialrecognition.png") 
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top) 
        f_lbl.place(x=0,y=55,width=1530,height=325 )

        # button
        b1_1 = Button(self.root, text="TRAIN DATA  ",command=self.train_classifier,cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60) 

        img_bottom=Image.open(r"college_images/opencv_face_reco_more_data.jpg") 
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom) 
        f_lbl.place(x=0,y=440,width=1530,height=325 )

    def train_classifier(self):
        data_dir= ("data")
        path =[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            try:
                img = Image.open(image).convert("L")  # chuyển sang ảnh xám
                imageNp = np.array(img, 'uint8')
        
                filename = os.path.basename(image)  # ví dụ: user.2023001.0.jpg
                parts = filename.split('.')
        
                if len(parts) >= 3 and parts[1].isdigit():
                    id = int(parts[1])
                    faces.append(imageNp)
                    ids.append(id)
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)
                else:
                    print(f"[BỎ QUA] File không hợp lệ: {filename}")

            except Exception as e:
                
                print(f"[LỖI] Không xử lý được ảnh {image}: {e}")
        ids = np.array(ids)   
        # ===========================train the classifier And save ==================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows ()
        messagebox.showinfo("Kết quả","Đã hoàn thành dữ liệu đào tạo! ")






if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
