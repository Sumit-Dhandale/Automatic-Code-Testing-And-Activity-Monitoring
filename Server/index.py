from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
import projectserver
import tester


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='mydatabase'
    )
mycursor=mydb.cursor()



class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")

        title=Label(self.root,bd=10, relief=GROOVE,text="Student Management System",font=("times new roman",40,"bold"),bg="black",fg="white")
        title.pack(side=TOP,fill=X)

        def add_student():
            roll=self.Roll_No_var.get()
            name=self.Name_var.get()
            email=self.Email_No_var.get()
            language=self.Language_var.get()
            year_info=self.Year_var.get()
            marks=0;

            if roll=="" or name=="" or email=="" or language=="" or year_info=="":
                tkinter.messagebox.showerror("Error","All fields are required")
            else:
                mycursor.execute('CREATE TABLE IF NOT EXISTS Student (Roll_No int,Name varchar(40),Email varchar(40),Year varchar(40),Subject varchar(40),Marks int)')
                query="insert into Student(Roll_No,Name,Email,Year,Subject,Marks) values(%s,%s,%s,%s,%s,%s)"
                values=(roll,name,email,year_info,language,marks)
                mycursor.execute(query,values)
                fetch_data()
                clear()
                mydb.commit()
                tkinter.messagebox.showinfo("Success","Record Inserted Successfully")

        def fetch_data():
            mycursor.execute("select * from Student")
            rows=mycursor.fetchall()
            if len(rows)!=0:
                student_table.delete(*student_table.get_children())
                for row in rows:
                    student_table.insert('',END,values=row)

        def search_data():
            if self.search_txt.get()=="" or self.search_by.get()=="":
                tkinter.messagebox.showerror("Error","All fields are required")
                return;
            mycursor.execute("select * from Student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=mycursor.fetchall()
            if len(rows)!=0:
                student_table.delete(*student_table.get_children())
                for row in rows:
                    student_table.insert('',END,values=row)

        def update_data():
            roll=self.Roll_No_var.get()
            name=self.Name_var.get()
            email=self.Email_No_var.get()
            language=self.Language_var.get()
            year_info=self.Year_var.get()

            query="update Student set Name=%s,Email=%s,Year=%s,Subject=%s where roll_no=%s"
            values=(name,email,year_info,language,roll)
            mycursor.execute(query,values)
            fetch_data()
            clear()
            mydb.commit()
            
            

        def delete_data():
            query="delete from Student where Roll_No="+str(self.Roll_No_var.get())
            mycursor.execute(query)
            mydb.commit()
            fetch_data()
            clear()
            


        def clear():
            self.Roll_No_var.set("")
            self.Name_var.set("")
            self.Email_No_var.set("")
            self.Language_var.set("")
            self.Year_var.set("")

        def get_cursor(ev):
            cursor_row=student_table.focus()
            contents=student_table.item(cursor_row)
            row=contents['values']
            self.Roll_No_var.set(row[0])
            self.Name_var.set(row[1])
            self.Email_No_var.set(row[2])
            self.Language_var.set(row[3])
            self.Year_var.set(row[4])

        def screenshot():
            projectserver.for_scr()
        
        def assign():
            flag=projectserver.assignment()
            roll=self.Roll_No_var.get()
            value=int(roll)
            query="select Marks from Student where Roll_NO=%s;"
            mycursor.execute(query,(value,))
            row=mycursor.fetchall()
            #print(row)
            mark=row[0]
            marks=mark[0]
            if flag:
                marks=marks+10
                query="update Student set Marks=%s where roll_no=%s"
                values=(marks,roll)
                mycursor.execute(query,values)
                mydb.commit()
            fetch_data()
            clear()
        

        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Database Management Systems","Confirm if you want to exit")
            if iExit>0:
                projectserver.Close()
                root.destroy()
                return
            
            

        #====================All variables=====================================
        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Email_No_var=StringVar()
        self.Language_var=StringVar()
        self.Year_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        #==============Manage Frame===========================================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cadet blue")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_Frame,bg="cadet blue",fg="white", text="Manage Students",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,bg="cadet blue",fg="white", text="Roll NO",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,bg="cadet blue",fg="white", text="Name",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,bd=5,textvariable=self.Name_var,relief=GROOVE,font=("times new roman",15,"bold"))
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,bg="cadet blue",fg="white", text="Email",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.Email_No_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        '''lbl_gender=Label(Manage_Frame,bg="cadet blue",fg="white", text="Gender",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")'''

        lbl_language=Label(Manage_Frame,bg="cadet blue",fg="white", text="Language",font=("times new roman",20,"bold"))
        lbl_language.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        combo_language=ttk.Combobox(Manage_Frame,textvariable=self.Language_var,font=("times new roman",13,"bold"),state="readonly")
        combo_language['values']=("Python","Java")
        combo_language.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_year=Label(Manage_Frame,bg="cadet blue",fg="white", text="Year",font=("times new roman",20,"bold"))
        lbl_year.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_year=ttk.Combobox(Manage_Frame,textvariable=self.Year_var,font=("times new roman",13,"bold"),state="readonly")
        combo_year['values']=("FE","SE","TE","BE")
        combo_year.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        '''lbl_address=Label(Manage_Frame,bg="cadet blue",fg="white", text="Address",font=("times new roman",20,"bold"))
        lbl_address.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=6,column=1,pady=10,padx=20,sticky="w")'''


        #==========Button frame===========================================================================================================

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="cadet blue")
        btn_Frame.place(x=10,y=400,width=420)

        addbtn=Button(btn_Frame,text="Add",width=10,command=add_student)
        addbtn.grid(row=0,column=0,padx=10,pady=10)

        updatebtn=Button(btn_Frame,text="Update",width=10,command=update_data)
        updatebtn.grid(row=0,column=1,padx=10,pady=10)

        deletebtn=Button(btn_Frame,text="Delete",width=10,command=delete_data)
        deletebtn.grid(row=0,column=2,padx=10,pady=10)

        clearbtn=Button(btn_Frame,text="Clear",width=10,command=clear)
        clearbtn.grid(row=0,column=3,padx=10,pady=10)


        #===============================================special Frame=========================================================================

        btn_Frame2=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="cadet blue")
        btn_Frame2.place(x=10,y=500,width=420)

        scrbtn=Button(btn_Frame2,text="SCR",width=10,command=screenshot)
        scrbtn.grid(row=0,column=0,padx=10,pady=10)

        assignbtn=Button(btn_Frame2,text="Assignment",width=10,command=assign)
        assignbtn.grid(row=0,column=1,padx=10,pady=10)

        exitbtn=Button(btn_Frame2,text="Exit",width=10,command=iExit)
        exitbtn.grid(row=0,column=2,padx=10,pady=10)


        
        #=============================Detail Frame==========================================================================================
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cadet blue")
        Detail_Frame.place(x=500,y=100,width=800,height=600)


        lbl_search=Label(Detail_Frame,bg="cadet blue",fg="white", text="Search By",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("times new roman",10,"bold"),state="readonly")
        combo_search['values']=("Roll_No")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,bd=5,width=20,relief=GROOVE,font=("times new roman",10,"bold"))
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=search_data)
        searchbtn.grid(row=0,column=3,padx=10,pady=10)

        show_allbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=fetch_data)
        show_allbtn.grid(row=0,column=4,padx=10,pady=10)

        #==================================Table Frame=================================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="cadet blue")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","year","language","marks"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("roll",text="Roll No.")
        student_table.heading("name",text="Name")
        student_table.heading("email",text="Email")
        student_table.heading("language",text="Language")
        student_table.heading("year",text="Year")
        student_table.heading("marks",text="Marks")
        student_table['show']='headings'
        student_table.column("roll",width=70)
        student_table.column("name",width=200)
        student_table.column("email",width=180)
        student_table.column("language",width=100)
        student_table.column("year",width=80)
        student_table.column("marks",width=100)
        student_table.pack(fill=BOTH,expand=1)
        student_table.bind("<ButtonRelease-1>",get_cursor)
        #fetch_data()


if __name__=='__main__':
    root=Tk()
    ob=Student(root)
    root.mainloop()



