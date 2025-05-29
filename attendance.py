from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2 
import os 
import csv 
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogiton System")

        # ===============VariableS===============
        self.var_atten_id= StringVar() 
        self.var_atten_roll= StringVar() 
        self.var_atten_name= StringVar() 
        self.var_atten_dep= StringVar() 
        self.var_atten_time= StringVar() 
        self.var_atten_date= StringVar() 
        self.var_atten_attendance= StringVar() 

        #Ảnh thứ nhất 
        img=Image.open(r"college_images/diem-danh-truong-hoc-thong-minh.gif")
        img = img.resize((800, 300), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=300 )

        #Ảnh thứ 2 
        img1=Image.open(r"college_images/diem_danh3.jpg") 
        img1=img1.resize((800, 300), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1) 
        f_lbl.place(x=800,y=0,width=800,height=300 )
        #anh bg 
        img3=Image.open(r"college_images/bgimg.jpg") 
        img3=img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=200,width=1530,height=710 )

        title_lbt = Label(bg_img, text="HỆ THỐNG QUẢN LÝ ĐIỂM DANH" , font=("times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbt.place(x=0 , y=0 , width=1530, height=45) 

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
         
         #left label frame 
        Left_frame= LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Thông tin điểm danh của sinh viên ",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"college_images/diem_danh4.jpg") 
        img_left=img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left) 
        f_lbl.place(x=5,y=0,width=720,height=130 )

        left_inside_frame = Frame(bg_img,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=25,y=220,width=720,height=400)

        # Labeland entry
        # Attendance id 
        attendanceId_label = Label(left_inside_frame,text="ID điểm danh:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times nwe roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll 
        rollLabel=Label(left_inside_frame,text="Số báo danh:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        # name
        nameLabel= Label(left_inside_frame,text="Tên:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0) 

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #Department 
        depLabel= Label(left_inside_frame,text="Khoa:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2) 

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        #time 
        timeLabel= Label(left_inside_frame,text="Thời gian:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0) 

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        # date
        dateLabel= Label(left_inside_frame,text="Ngày:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2) 

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        # attendance
        attendanceLabel = Label(left_inside_frame,text="Tình trạng tham dự",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Trạng thái","Có mặt ","Vắng mặt") 
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame= Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn = Button(btn_frame, text="Nhập csv  ",command=self.importCsv, width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Xuất csv ",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=1)
      
        delete_btn = Button(btn_frame, text="Xóa ",width=17,command=self.delete_data, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Đặt lại ",command=self.reset_data,width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=3)


        #Right label frame 
        Right_frame= LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Chi tiết điểm danh",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame= Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        # ====================scroll bar table =======================
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendace ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendace")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

#========================fetch data==============
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv
    # def importCsv(self):
    #     global mydata
    #     mydata.clear()
    #     fln=filedialog.askopenfilename(initialdir= os.getcwd(),title="Mở file csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root )
    #     with open(fln) as myfile:
    #         csvread=csv.reader(myfile,delimiter=",")
    #         for i in csvread:
    #             mydata.append(i)
    #         self.fetchData(mydata)
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Mở file csv",
                                        filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if not fln:
            return
        try:
            with open(fln, newline='') as myfile:
                csvread = csv.reader(myfile, delimiter=',')
                headers = next(csvread, None)  # bỏ dòng tiêu đề
                for i in csvread:
                    if len(i) == 7:
                        mydata.append(i)
            self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc file CSV: {str(e)}", parent=self.root)
        

    #export csv 
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Không có dữ liệu ","Không tìm thấy dữ liệu đề xuất ",parent= self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir= os.getcwd(),title="Mở file csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root )
            with open(fln,mode="w",newline="") as myfile:
                exp_write= csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Xuất dữ liệu","Dữ liệu của bạn đã xuất sang  "+os.path.basename(fln)+"Thành công")
        except Exception as es :    
                messagebox.showerror("Lỗi ",f"Đã sảy ra lỗi  : {str(es)}",parent=self.root)

    #delete_data 
    def delete_data(self):
        selected = self.AttendanceReportTable.focus()
        if not selected:
            messagebox.showwarning("Chọn dòng", "Hãy chọn một dòng để xóa", parent=self.root)
            return
        values = self.AttendanceReportTable.item(selected, "values")
        if values:
            mydata.remove(list(values))
            self.fetchData(mydata)


            
    def get_cursor(self,Event=""):
        cursor_row= self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0]) 
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5]) 
        self.var_atten_attendance.set(rows[6])  

    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("") 
        self.var_atten_attendance.set("")  


        








if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()