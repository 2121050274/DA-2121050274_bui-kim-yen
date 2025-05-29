from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2 
import os 

# from test.test_importlib.namespace_pkgs.project1 import parent
# password = getpass.getpass("Enter your MySQL password: ")
# from pip._vendor.distlib import database
# from test.test_importlib.namespace_pkgs.project1 import parent
class Student:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        # =========================Variable================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #Ảnh thứ nhất 
        img=Image.open(r"C:\Đồ án\FaceAttendance _project\college_images/diem_danh1.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130 )

        #Ảnh thứ 2 
        img1=Image.open(r"C:\Đồ án\FaceAttendance _project\college_images/diem_danh2.jpeg") 
        img1=img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1) 
        f_lbl.place(x=500,y=0,width=500,height=130 )

        #Ảnh thứ 3 
        img2=Image.open(r"C:\Đồ án\FaceAttendance _project\college_images/diem_danh3.jpg") 
        img2=img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2) 
        f_lbl.place(x=1000,y=0,width=550,height=130 )

        #Ảnh bg 
        img3=Image.open(r"C:\Đồ án\FaceAttendance _project\college_images/bgimg.jpg") 
        img3=img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3) 
        bg_img.place(x=0,y=130,width=1530,height=710 )

        title_lbt = Label(bg_img, text="HỆ THỐNG QUẢN LÝ SINH VIÊN" , font=("times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbt.place(x=0 , y=0 , width=1530, height=45) 

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame 
        Left_frame= LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text=" Thông tin sinh viên",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Đồ án\FaceAttendance _project\college_images/diem_danh3.jpg") 
        img_left=img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left) 
        f_lbl.place(x=5,y=0,width=720,height=130 )

        #Thông tin lớp học hiện tại 
        curent_course_frame= LabelFrame(Left_frame,bd=2,bg='white',relief=RIDGE,text="Thông tin lớp học hiện tại ",font=("times new roman",12,"bold"))
        curent_course_frame.place(x=5,y=135,width=720,height=125)
        
        #khoa
        dep_label = Label(curent_course_frame,text="Khoa ",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo= ttk.Combobox(curent_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Chọn khoa ","CNTT ","Khoa co-dien ","Khoa dau khi ","Khoa xay dung ")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # Lớp học 
        course_label = Label(curent_course_frame,text="Lớp học ",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo= ttk.Combobox(curent_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Khóa ","k65","k66" ,"k67","k68")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        # Năm  
        year_label = Label(curent_course_frame,text="Năm ",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo= ttk.Combobox(curent_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("chọn năm học ","2020-21","2021-22","2022-23","2023-24","2024-25 ")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Học kì 
        Semester_label = Label(curent_course_frame,text="Học kì ",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo= ttk.Combobox(curent_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        Semester_combo["values"]=("Chọn học kì ","Học kì-1","Học kì-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        

        # Thông tin sinh viên 
        class_student_frame= LabelFrame(Left_frame,bd=2,bg='white',relief=RIDGE,text="Thông tin sinh viên ",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #   Mã số sinh viên 
        StudentId_label = Label(class_student_frame,text="mã số sinh viên :",font=("times new roman",13,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times nwe roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Tên sinh viên 
        StudentName_label = Label(class_student_frame,text=" Tên sinh viên :",font=("times new roman",13,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times nwe roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # lớp học 
        class_div_label = Label(class_student_frame,text="Lớp học  :",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo= ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)
        div_combo["values"]=("A ","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         
        # số báo danh 
        roll_no_label = Label(class_student_frame,text="Số báo danh :",font=("times new roman",13,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times nwe roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Giới tính 
        gender_label= Label(class_student_frame,text="Giới Tính :",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo= ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Nam","nu","khac") 
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #Ngày sinh 
        dob_label = Label(class_student_frame,text="Ngày sinh :",font=("times new roman",13,"bold"))
        dob_label.grid(row=2 ,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times nwe roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        Email_label = Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"))
        Email_label.grid(row=3 ,column=0,padx=10,pady=5,sticky=W)

        Email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times nwe roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #SDT 
        phonr_label = Label(class_student_frame,text="SĐT :",font=("times new roman",13,"bold"))
        phonr_label.grid(row=3 ,column=2,padx=10,pady=5,sticky=W)

        phonr_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times nwe roman",13,"bold"))
        phonr_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # địa chỉ 
        address_label = Label(class_student_frame,text="Địa chỉ  :",font=("times new roman",13,"bold"))
        address_label.grid(row=4 ,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times nwe roman",13,"bold"))
        address_entry.grid(row=4,column=1 ,padx=10,pady=5,sticky=W)
        # Tên giáo viên  
        teacher_label= Label(class_student_frame,text="Tên giáo viên  :",font=("times new roman",13,"bold"))
        teacher_label.grid(row=4 ,column=2,padx=10,pady=5,sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times nwe roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # radio Buttons 
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="   Chụp  ảnh mẫu khuôn mặt ",value="Yes")
        radionbtn1.grid(row=6, column=0)

        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text=" Không chụp ảnh mẫu ",value="No")
        radionbtn2.grid(row=6, column=1)

        #Butttons Frame 
        btn_frame= Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn = Button(btn_frame, text="Lưu ",command=self.app_data, width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Cập Nhật ",command=self.update_data, width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=1)
      
        delete_btn = Button(btn_frame, text="Xóa ", command=self.delete_data,width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Đặt lại ",command=self.reset_data, width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1= Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)


        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Chụp ảnh mẫu ", width=35, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0, column=0)
        
        update_photo_btn = Button(btn_frame1, text=" Cập nhật ảnh  mẫu", width=35, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0, column=1)









        #Right label frame 
        Right_frame= LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text=" Thông tin sinh viên",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Đồ án\FaceAttendance _project\college_images/Student.jpeg") 
        img_right=img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right) 
        f_lbl.place(x=5,y=0,width=720,height=130 )

        # ============Serach System ==================
        Serach_frame= LabelFrame(Right_frame,bd=2,bg='white',relief=RIDGE,text="Hệ thống tìm kiếm ",font=("times new roman",12,"bold"))
        Serach_frame.place(x=5,y=135,width=710,height=70)

        Search_label = Label(Serach_frame,text="Tìm kiếm theo :",font=("times new roman",15,"bold"),bg="red",fg="white")
        Search_label.grid(row=0 ,column=0,padx=10,pady=5,sticky=W)

        Search_combo= ttk.Combobox(Serach_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Lựa chọn  ","Số báo danh ","Số điện thoại ")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        

        search_entry = ttk.Entry(Serach_frame,width=15,font=("times nwe roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(Serach_frame, text="Tìm kiếm ", width=12, font=("times new roman", 12, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0, column=3,padx=4)

        showAll_btn = Button(Serach_frame, text="Hiển thị tất cả ", width=12, font=("times new roman", 12, "bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0, column=4,padx=4)
        
        # ==================table frame===========
        table_frame=Frame(Right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.Studen_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Studen_table.xview)
        scroll_y.config(command=self.Studen_table.yview)

        self.Studen_table.heading("dep",text="Khoa ")
        self.Studen_table.heading("course",text="Lớp học ")
        self.Studen_table.heading("year",text="Năm ")
        self.Studen_table.heading("sem",text="Học kì ")
        self.Studen_table.heading("id",text="Mã sinh viên ")
        self.Studen_table.heading("name",text="Tên ")
        self.Studen_table.heading("roll",text="Số báo danh ")
        self.Studen_table.heading("gender",text="Giới Tính ")
        self.Studen_table.heading("div",text="Phân ban ")
        self.Studen_table.heading("dob",text="Ngày sinh ")
        self.Studen_table.heading("email",text="Email")
        self.Studen_table.heading("phone",text="SĐT ")
        self.Studen_table.heading("address",text="Địa chỉ ")
        self.Studen_table.heading("teacher",text="Giáo Viên ")
        self.Studen_table.heading("photo",text="Trạng thái ảnh mẫu ")
        self.Studen_table["show"]="headings"

        self.Studen_table.column("dep",width=100)
        self.Studen_table.column("course",width=100)
        self.Studen_table.column("year",width=100)
        self.Studen_table.column("sem",width=100)
        self.Studen_table.column("id",width=100)
        self.Studen_table.column("name",width=100)
        self.Studen_table.column("roll",width=100)
        self.Studen_table.column("gender",width=100)
        self.Studen_table.column("div",width=100)
        self.Studen_table.column("dob",width=100)
        self.Studen_table.column("email",width=100)
        self.Studen_table.column("phone",width=100)
        self.Studen_table.column("address",width=100)
        self.Studen_table.column("teacher",width=100)
        self.Studen_table.column("photo",width=150)

        self.Studen_table.pack(fill=BOTH,expand=1)
        self.Studen_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ====================function decration=================
    def app_data(self):
        if self.var_dep.get()=="Chọn khoa " or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Lỗi ","Vui lòng điền đầy đủ thông tin bắt buộc ",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Sinhnhatngay1211@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO student (dep, course, year, semester, student_id, name, Division, roll, gender, dob, email, phone, address, teacher, PhotoSample) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Thành công ","Thêm mới sinh viên thành công ",parent= self.root)
            except Exception as es :    
                messagebox.showerror("Lỗi ",f"Đã sảy ra lỗi  : {str(es)}",parent=self.root)

# ========================fetch data==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sinhnhatngay1211@",database="face_recognizer")
        my_cursur=conn.cursor()
        my_cursur.execute("select*from student")
        data= my_cursur.fetchall()

        if len(data)!=0:
            self.Studen_table.delete(*self.Studen_table.get_children())
            for i in data:
                self.Studen_table.insert("",END,values=i)
            conn.commit()
        conn.close()
#=================get cursor====================
    def get_cursor(self,event=""):
        cursor_focus= self.Studen_table.focus()
        if not cursor_focus:
            return
        content= self.Studen_table.item(cursor_focus)
        data= content["values"]
        if not data:
            return
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate= messagebox.askyesno("Upadate ","Bạn có muốn cập nhật thông tin sinh viên này không?",parent=self.root )
                if Upadate>0 :
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sinhnhatngay1211@",database="face_recognizer")
                    my_cursur=conn.cursor()
                    my_cursur.execute(
                        
                        "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s" ,
            
                        (

                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()

                            ))
                    

                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Thành công ","Thông tin chi tiết về học sinh đã được cập nhật thành công ", parent =self.root)    
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Lỗi","SMã số sinh viên phải được điền",parent = self.root) 
        else:
            try:
                delete = messagebox.askyesno("Xóa sinh viên ", "Bạn có muốn xóa sinh viên này không ?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sinhnhatngay1211@",database="face_recognizer")
                    my_cursur=conn.cursor()
                    sql= "delete from student where Student_id=%s"
                    val=(int(self.var_std_id.get()),)
                    my_cursur.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully delete Student detials",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

# =============================Generate dataa set or take photo samples============
    def generate_dataset(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập Mã số sinh viên trước khi chụp ảnh", parent=self.root)
            return
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Sinhnhatngay1211@",database="face_recognizer")
                my_cursur=conn.cursor()
                my_cursur.execute("select*from student")
                myresult = my_cursur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursur.execute(
                        
                        "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s ,PhotoSample=%s Where Student_id =%s" ,
            
                        (

                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get() 

                            ))
                    
                conn.commit()
                self.fetch_data() 
                conn.close() 
                # ==================================load predifiend data on face frontals opencv===========

                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")



                def face_cropped(img): 
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor = 1.3 
                    # Minimum Neighbor = 5

                    for(x,y,w,h)in faces:
                        face_cropped= img[y:y+h,x:x+w]
                        return face_cropped

                if not os.path.exists("data"):
                    os.makedirs("data")


                cap=cv2.VideoCapture(0)
                img_id=0 
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        face_img = face_cropped(my_frame)
                        if face_img is not None:
                            face = cv2.resize(face_img, (200, 200 ))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            student_id = self.var_std_id.get().strip()
                            if not student_id:
                                messagebox.showerror("Lỗi", "Mã số sinh viên không được để trống!", parent=self.root)
                                return

                            file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)
                            img_id += 1


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()  
                self.reset_data()
                messagebox.showinfo("Result", "Đã tạo tập dữ liệu thành công !")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)






if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

    