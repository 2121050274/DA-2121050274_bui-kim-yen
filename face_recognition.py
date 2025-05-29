from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 
import os 
import numpy as np
from cv2.gapi import video
from PIL import ImageFont, ImageDraw, Image

class Face_recognition :
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbt = Label(self.root, text=" NHẬN DẠNG KHUÔN MẶT " , font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbt.place(x=0 , y=0 , width=1530, height=45) 

        # 1st image
        img_top=Image.open(r"college_images/face_detection.jpeg") 
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top) 
        f_lbl.place(x=0,y=55,width=650,height=700 )

        # 2st image
        img_bottom=Image.open(r"college_images/facial-recognition.png") 
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom) 
        f_lbl.place(x=650,y=55,width=950,height=700 )

        # button
        b1_1 = Button(f_lbl,text=" NHẬN DIỆN KHUÔN MẶT  ",cursor="hand2",command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(relx=0.5, rely=1.0,y=-50,anchor="s", width=400, height=40)

    # ==========================attendance==============
    # def mark_attendance(self,i,r,n,d):
    #     with open("kimyen.csv","r+",newline="\n") as f:
    #         myDataList= f.readlines() 
    #         name_list=[]
    #         for line in myDataList:
    #             Entry=line.split((",")) 
    #             name_list.append(Entry[0])
    #         if ((i not in name_list) and (r not in name_list) and (n not in name_list)and ((d not in name_list)) ) :
    #             now=datetime.now()
    #             d1=now.strftime("%d%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")
    def mark_attendance(self, i, r, n, d):
        filename = "attendance.csv"
        if not os.path.exists(filename):
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Roll", "Name", "Department", "Time", "Date", "Status"])

        with open(filename, "r+", newline="\n", encoding="utf-8") as f:
            myDataList = f.readlines()
            today = datetime.now().strftime("%d/%m/%Y")
            for line in myDataList:
                if i in line and today in line:
                    return  # đã điểm danh

            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")





    # ==================face recognition======================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,clor,tex,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 - predict) 


                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sinhnhatngay1211@", database="face_recognizer")
                    my_cursur = conn.cursor()

                    my_cursur.execute("SELECT Name FROM student WHERE Student_id=%s", (id,))
                    n = my_cursur.fetchone()
                    n = "+".join(n) if n else "Unknown"

                    my_cursur.execute("SELECT Roll FROM student WHERE Student_id=%s", (id,))
                    r = my_cursur.fetchone()
                    r = "+".join(r) if r else "Unknown"

                    my_cursur.execute("SELECT Dep FROM student WHERE Student_id=%s", (id,))
                    d = my_cursur.fetchone()
                    d = "+".join(d) if d else "Unknown"
                    
                    my_cursur.execute("SELECT Student_id FROM student WHERE Student_id=%s", (id,))
                    i = my_cursur.fetchone()
                    i = "+".join(i) if i else "Unknown"


                finally:
                    conn.close()

                if confidence>60: 
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"SBD:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Ten:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Khoa:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y] 
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create() 
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Lỗi", "Chưa có dữ liệu huấn luyện. Vui lòng bấm 'Train Data' trước.")
            return 
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:

            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Chào mừng đến với nhận dạng khuôn mặt ",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()




    
if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
