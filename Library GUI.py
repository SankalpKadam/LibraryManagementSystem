

from tkinter import *
from tkcalendar import *
from PIL import ImageTk,Image
from tkinter.font import Font
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from datetime import datetime
from tkinter import ttk 


class viewLibrarian:
    def __init__(self,vlibrarian):
        self.root=vlibrarian
        self.root.iconbitmap(r'book.ico')
        self.wdth=600
        self.hgth=268
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('%dx%d+%d+%d'%(self.wdth,self.hgth,self.width,self.height))
        tv=ttk.Treeview(self.root,height=12)
        tv['columns']=('EmployeeName','EmployeeID','Contact','Address')
        tv.place(x=0,y=0)
        tv.heading('#0',text="Students",anchor='w')
        tv.column('#0',stretch=NO,width=2,anchor='w')
        tv.heading('EmployeeName',text="EmployeeName")
        tv.column('EmployeeName',anchor='center',width=150)
        tv.heading('EmployeeID',text="EmployeeID")
        tv.column('EmployeeID',anchor='center',width=150)
        tv.heading('Contact',text="Contact")
        tv.column('Contact',anchor='center',width=150)
        tv.heading('Address',text="Address")
        tv.column('Address',anchor='center',width=140)
        self.root.resizable(0,0)
        
        tvscrollbar=ttk.Scrollbar(self.root,orient="vertical",command=tv.yview)
        tvscrollbar.pack(side='right', fill='y')
        tv.configure(yscroll=tvscrollbar.set)
        
        con = mysql.connect(host="localhost", user="root",password="", database="library_management")
        cursor = con.cursor()
        cursor.execute("select employee_name ,employee_id ,contact_no ,address from employee_info order by employee_id ASC")
        rows = cursor.fetchall()
        for row in tv.get_children():
            tv.delete(row)
              
        for row in rows :

            tv.insert('','end',value=row)

        con.close()

        
        
        
class viewReturn:
    def __init__(self,vreturn):
        self.root=vreturn
        self.root.iconbitmap(r'book.ico')
        self.wdth=612
        self.hgth=268
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('%dx%d+%d+%d'%(self.wdth,self.hgth,self.width,self.height))
        tv=ttk.Treeview(self.root,height=12)
        tv['columns']=('StudentName','LIB. ID','BookName','BookID','IssueDate','ReturnDate')
        tv.place(x=0,y=0)
        tv.heading('#0',text="Students",anchor='w')
        tv.column('#0',stretch=NO,width=2,anchor='w')
        tv.heading('StudentName',text="StudentName")
        tv.column('StudentName',anchor='center',width=100)
        tv.heading('LIB. ID',text="LIB. ID")
        tv.column('LIB. ID',anchor='center',width=100)
        tv.heading('BookName',text="BookName")
        tv.column('BookName',anchor='center',width=100)
        tv.heading('BookID',text="BOOKID")
        tv.column('BookID',anchor='center',width=100)
        tv.heading('IssueDate',text="Issue Date")
        tv.column('IssueDate',anchor='center',width=100)
        tv.heading('ReturnDate',text="Return Date")
        tv.column('ReturnDate',anchor='center',width=90)
        self.root.resizable(0,0)
        
        tvscrollbar=ttk.Scrollbar(self.root,orient="vertical",command=tv.yview)
        tvscrollbar.pack(side='right', fill='y')
        tv.configure(yscroll=tvscrollbar.set)
        
        con = mysql.connect(host="localhost", user="root",password="", database="library_management")
        cursor = con.cursor()
        cursor.execute("select student_name ,lib_id ,book_name ,book_id ,issue_date ,return_date from book_return order by lib_id ASC")
        rows = cursor.fetchall()
        for row in tv.get_children():
            tv.delete(row)
    
        for row in rows :

            tv.insert('','end',value=row)

        con.close()

class viewIssue:
    def __init__(self,vissue):
        self.root=vissue
        self.root.iconbitmap(r'book.ico')
        self.wdth=518
        self.hgth=268
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('%dx%d+%d+%d'%(self.wdth,self.hgth,self.width,self.height))
        tv=ttk.Treeview(self.root,height=12)
        tv['columns']=('StudentName','LIB. ID','BookName','BookID','IssueDate')
        tv.place(x=0,y=0)
        tv.heading('#0',text="Students",anchor='w')
        tv.column('#0',stretch=NO,width=2,anchor='w')
        tv.heading('StudentName',text="StudentName")
        tv.column('StudentName',anchor='center',width=100)
        tv.heading('LIB. ID',text="LIB. ID")
        tv.column('LIB. ID',anchor='center',width=100)
        tv.heading('BookName',text="BookName")
        tv.column('BookName',anchor='center',width=100)
        tv.heading('BookID',text="BOOKID")
        tv.column('BookID',anchor='center',width=100)
        tv.heading('IssueDate',text="Issue Date")
        tv.column('IssueDate',anchor='center',width=100)
        self.root.resizable(0,0)
        
        tvscrollbar=ttk.Scrollbar(self.root,orient="vertical",command=tv.yview)
        tvscrollbar.pack(side='right', fill='y')
        tv.configure(yscroll=tvscrollbar.set)
        
        con = mysql.connect(host="localhost", user="root",password="", database="library_management")
        cursor = con.cursor()
        cursor.execute("select student_name ,lib_id ,book_name ,book_id ,issue_date from book_issue order by book_id ASC")
        rows = cursor.fetchall()
        for row in tv.get_children():
            tv.delete(row)
        

        for row in rows :

            tv.insert('','end',value=row)

        con.close()

        
class viewStudent:
    def __init__(self,vstud):
        self.root=vstud
        self.root.iconbitmap(r'book.ico')
        self.wdth=520
        self.hgth=268
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('%dx%d+%d+%d'%(self.wdth,self.hgth,self.width,self.height))
        tv=ttk.Treeview(self.root,height=12)
        tv['columns']=('StudentName','LIB. ID','Unique ID','Course','Contact')
        tv.place(x=0,y=0)
        tv.heading('#0',text="Students",anchor='w')
        tv.column('#0',stretch=NO,width=2,anchor='w')
        tv.heading('StudentName',text="StudentName")
        tv.column('StudentName',anchor='center',width=100)
        tv.heading('LIB. ID',text="LIB. ID")
        tv.column('LIB. ID',anchor='center',width=100)
        tv.heading('Unique ID',text="UNIQUE ID")
        tv.column('Unique ID',anchor='center',width=100)
        tv.heading('Course',text="COURSE")
        tv.column('Course',anchor='center',width=100)
        tv.heading('Contact',text="CONTACT")
        tv.column('Contact',anchor='center',width=100)
        self.root.resizable(0,0)
        
        tvscrollbar=ttk.Scrollbar(self.root,orient="vertical",command=tv.yview)
        tvscrollbar.pack(side='right', fill='y')
        tv.configure(yscroll=tvscrollbar.set)
        
        con = mysql.connect(host="localhost", user="root",password="", database="library_management")
        cursor = con.cursor()
        cursor.execute("select student_name ,lib_id ,unique_id ,course ,contact_no from student_info order by lib_id ASC")
        rows = cursor.fetchall()
        for row in tv.get_children():
            tv.delete(row)
              
        for row in rows :

            tv.insert('','end',value=row)

        con.close()

        
        
        
        
        
class viewBOOK:
    def __init__(self,vbook):
        self.root=vbook
        self.root.iconbitmap(r'book.ico')
        self.wdth=616
        self.hgth=326
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('%dx%d+%d+%d'%(self.wdth,self.hgth,self.width,self.height))
        tv=ttk.Treeview(self.root,height=15)
        tv['columns']=('BookName','BookID','Author','Publisher','Cost','Category','Attribute')
        tv.place(x=0,y=0)
        tv.heading('#0',text="Books",anchor='w')
        tv.column('#0',stretch=NO,width=2,anchor='w')
        tv.heading('BookName',text="BookName")
        tv.column('BookName',anchor='center',width=85)
        tv.heading('BookID',text="BookID")
        tv.column('BookID',anchor='center',width=85)
        tv.heading('Author',text="Author")
        tv.column('Author',anchor='center',width=85)
        tv.heading('Publisher',text="Publisher")
        tv.column('Publisher',anchor='center',width=85)
        tv.heading('Cost',text="Cost")
        tv.column('Cost',anchor='center',width=85)
        tv.heading('Category',text="Category")
        tv.column('Category',anchor='center',width=85)
        tv.heading('Attribute',text="Attribute")
        tv.column('Attribute',anchor='center',width=85)
        
        self.root.resizable(0,0)
        
        tvscrollbar=ttk.Scrollbar(self.root,orient="vertical",command=tv.yview)
        tvscrollbar.pack(side='right', fill='y')
        tv.configure(yscroll=tvscrollbar.set)
        
        con = mysql.connect(host="localhost", user="root",password="", database="library_management")
        cursor = con.cursor()
        cursor.execute("select * from book_add order by book_id ASC")
        rows = cursor.fetchall()
        for row in tv.get_children():
            tv.delete(row)
        
        
        for row in rows :

            tv.insert('','end',value=row)

        con.close()




class dellibrarian:
    def __init__(self,dltsb):
        self.root=dltsb
        self.root.iconbitmap(r'book.ico')
    
        
        self.wdth=400
        self.hgth=500
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x500+%d+%d'%(self.width,self.height))
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="DELETE LIBRARIAN",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=80,y=10) 
        l2=Label(self.root,text="______________________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=70,y=70)
        l3=Label(self.root,text="EMPLOYEE NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l7=Label(self.root,text="______________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l7.place(x=0,y=170)
        l4=Label(self.root,text="EMPLOYEE ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e12=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e12.place(x=10,y=240)
        l5=Label(self.root,text="CONTACT NO.",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=280)
        self.e13=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e13.place(x=10,y=320)
        l6=Label(self.root,text="ADDRESS",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=360)
        self.e11=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e11.place(x=10,y=390)
        btndel=Button(self.root,text="DELETE",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.deletelibrariann)
        btndel.place(x=160,y=440)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchlibrarian)
        btnsearch.place(x=300,y=130)
        self.root.resizable(0,0)
    def deletelibrariann(self):
        
        if(self.e1.get() == ""):
            messagebox.showinfo("Delete Status","ID is Necessary to delete")
        else:
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("delete from employee_info where employee_id='"+ self.e1.get() +"'")
            cursor.execute("commit");

 
        
            messagebox.showinfo("Delete Status","Deleted Successfully")
            con.close()
        
        
    
    
#        self.root.destroy()
    def searchlibrarian(self):
        
             
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
            self.e12.delete(0, 'end')
            self.e13.delete(0, 'end')
            self.e11.delete(0, 'end')
            
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from employee_info where employee_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows :
            self.e12.insert(0, row[0])
            self.e13.insert(0, row[1])
            self.e11.insert(0, row[3])
        
            
            
            
        con.close()
        
        

        
class updatelibrarian:
    def __init__(self,udpl):
        self.root=udpl
        self.root.iconbitmap(r'book.ico')
        self.hgth=500
        self.wdth=400
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x500+%d+%d'%(self.width,self.height))
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="UPDATE LIBRARIAN",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=80,y=10) 
        l2=Label(self.root,text="___________________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=70,y=70)
        l3=Label(self.root,text="EMPLOYEE NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l71=Label(self.root,text="______________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l71.place(x=0,y=170)
        l4=Label(self.root,text="EMPLOYEE ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e2.place(x=10,y=240)
        l5=Label(self.root,text="ADDRESS",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=280)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e3.place(x=10,y=320)
        l6=Label(self.root,text="CONTACT NO.",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=360)
        self.e4=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e4.place(x=10,y=390)
        
        btnupd=Button(self.root,text="UPDATE",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.updatelibrariann)
        btnupd.place(x=180,y=430)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchemployee)
        btnsearch.place(x=300,y=130)
        self.root.resizable(0,0)
    def updatelibrariann(self):
        
        if(self.e1.get()=="" or self.e2.get()==""  or self.e3.get()==""  or self.e4.get()==""):
            messagebox.showinfo("Update Status","All Fields are required")
        else:    
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("update employee_info set employee_name='"+ self.e2.get() +"', address='"+ self.e3.get() +"', contact_no='"+ self.e4.get() +"' where employee_id='"+ self.e1.get() +"'               ")    
            cursor.execute("commit");
         
            
            messagebox.showinfo("update Status","updated Successfully")
            con.close()
        
        self.root.destroy()
      
    def searchemployee(self):
        
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
            self.e2.delete(0, 'end')
            self.e3.delete(0, 'end')
            self.e4.delete(0, 'end')
            
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from employee_info where employee_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows :
            self.e2.insert(0, row[0])
            self.e3.insert(0, row[3])
            self.e4.insert(0, row[1])
            
            
            
            
        con.close()
        
   
        
        
        
        
class delstudents:
    def __init__(self,dlts):
        self.root=dlts
        self.root.iconbitmap(r'book.ico')
        self.wdth=400
        self.hgth=500
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x500+%d+%d'%(self.width,self.height))
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="DELETE STUDENTS",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=80,y=10) 
        l2=Label(self.root,text="_________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=120,y=70)
        l3=Label(self.root,text="STUDENT NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l7=Label(self.root,text="______________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l7.place(x=0,y=170)
        l4=Label(self.root,text="LIB. ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e2.place(x=10,y=240)
        l5=Label(self.root,text="UNIQUE ID",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=280)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e3.place(x=10,y=320)
        l6=Label(self.root,text="COURSE",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=360)
        self.e4=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e4.place(x=10,y=390)
        btndels=Button(self.root,text="DELETE",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.deletestudentss)
        btndels.place(x=160,y=440)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchstudent)
        btnsearch.place(x=300,y=130)
        self.root.resizable(0,0)
    def deletestudentss(self):
        
                
        if(self.e1.get() == ""):
            messagebox.showinfo("Delete Status","ID is Necessary to delete")
        else:
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("delete from student_info where lib_id='"+ self.e1.get() +"'")
            cursor.execute("commit");

         
        
            messagebox.showinfo("Delete Status","Deleted Successfully")
            con.close()
        
        
#        self.root.destroy()
        
    def searchstudent(self):
        
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from student_info where lib_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows :
            self.e2.insert(0, row[0])
            self.e3.insert(0, row[3])
            self.e4.insert(0, row[4])
            
            
        con.close()
   
        
class updatestudents:
    def __init__(self,udp):
        self.root=udp
        self.root.iconbitmap(r'book.ico')
        self.hgth=560
        self.wdth=400
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x560+%d+%d'%(self.width,self.height))
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="UPDATE STUDENTS",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=80,y=10) 
        l2=Label(self.root,text="_________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=120,y=70)
        l3=Label(self.root,text="STUDENT NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l71=Label(self.root,text="______________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l71.place(x=0,y=170)
        l4=Label(self.root,text="LIB. ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e2.place(x=10,y=240)
        l5=Label(self.root,text="UNIQUE ID",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=280)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e3.place(x=10,y=320)
        l6=Label(self.root,text="CONTACT NO.",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=360)
        self.e4=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e4.place(x=10,y=390)
        l7=Label(self.root,text="COURSE",font=mfont1,fg="BLACK",bg="WHITE")
        l7.place(x=10,y=430)
        self.e5=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e5.place(x=10,y=470)
       
        btnudp=Button(self.root,text="UPDATE",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.updatestudentss)
        btnudp.place(x=180,y=510)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchstudent4)
        btnsearch.place(x=300,y=130)
        self.root.resizable(0,0)
    def updatestudentss(self):
        
        if(self.e1.get()=="" or self.e2.get()==""  or self.e3.get()==""  or self.e4.get()==""  or self.e5.get()==""):
            messagebox.showinfo("Update Status","All Fields are required")
        else:    
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("update student_info set student_name='"+ self.e2.get() +"', unique_id='"+ self.e3.get() +"', contact_no='"+ self.e4.get() +"', course='"+ self.e5.get() +"' where lib_id='"+ self.e1.get() +"'               ")    
            cursor.execute("commit");
         
         
            
            messagebox.showinfo("update Status","updated Successfully")
            con.close()
    def searchstudent4(self):
            
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
            self.e2.delete(0, 'end')
            self.e3.delete(0, 'end')
            self.e4.delete(0, 'end')
            self.e5.delete(0, 'end')
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from student_info where lib_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows :
            self.e2.insert(0, row[0])
            self.e3.insert(0, row[3])
            self.e4.insert(0, row[1])
            self.e5.insert(0, row[4])
            
            
            
        con.close()
        
        
        
        
        

    
class updatebook:
    def __init__(self,upk):
        self.root=upk
        self.root.iconbitmap(r'book.ico')
        self.hgth=660
        self.wdth=400
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x680+%d+%d'%(self.width,self.height))
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="UPDATE BOOKS IN LIBRARY",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=30,y=10) 
        l2=Label(self.root,text="_________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=120,y=70)
        l3=Label(self.root,text="BOOK NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l71=Label(self.root,text="______________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l71.place(x=0,y=170)
        l4=Label(self.root,text="BOOK ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e2.place(x=10,y=240)
        l5=Label(self.root,text="AUTHOR",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=280)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e3.place(x=10,y=320)
        l6=Label(self.root,text="PUBLISHER",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=360)
        self.e4=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e4.place(x=10,y=390)
        l7=Label(self.root,text="COST",font=mfont1,fg="BLACK",bg="WHITE")
        l7.place(x=10,y=430)
        self.e5=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e5.place(x=10,y=470)
        l8=Label(self.root,text="CATEGORY",font=mfont1,fg="BLACK",bg="WHITE")
        l8.place(x=10,y=510)
        self.e6=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e6.place(x=10,y=540)
        l9=Label(self.root,text="ATTRIBUTE",font=mfont1,fg="BLACK",bg="WHITE")
        l9.place(x=10,y=570)
        self.e10=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e10.place(x=10,y=600)
        btnudpp=Button(self.root,text="UPDATE",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.updateboook)
        btnudpp.place(x=180,y=640)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchbook1)
        btnsearch.place(x=300,y=130)
        self.root.resizable(0,0)
    def updateboook(self):
        
        if(self.e1.get()=="" or self.e2.get()==""  or self.e3.get()==""  or self.e4.get()==""  or self.e5.get()==""  or self.e6.get()==""  or self.e10.get()==""):
            messagebox.showinfo("Update Status","All Fields are required")
        else:    
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("update book_add set book_name='"+ self.e2.get() +"', author='"+ self.e3.get() +"', publisher='"+ self.e4.get() +"', cost='"+ self.e5.get() +"', category='"+ self.e6.get() +"', attribute='"+ self.e10.get() +"' where book_id='"+ self.e1.get() +"'               ")     
            cursor.execute("commit");
         
            
            messagebox.showinfo("update Status","updated Successfully")
            con.close()
        
        self.root.destroy()
    def searchbook1(self):
        
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e10.delete(0, 'end')
        
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from book_add where book_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows :
            self.e2.insert(0, row[0])
            self.e3.insert(0, row[2])
            self.e4.insert(0, row[3])
            self.e5.insert(0, row[4])
            self.e6.insert(0, row[5])
            self.e10.insert(0, row[6])
            
        con.close()
        
               
class delbooks:
    def __init__(self,el):
        
        self.root=el
        self.wdth=400
        self.hgth=680
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x500+%d+%d'%(self.width,self.height))
        self.root.iconbitmap(r'book.ico')
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="DELETE BOOKS FROM LIBRARY",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=30,y=10) 
        l2=Label(self.root,text="_________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=120,y=70)
        l3=Label(self.root,text="BOOK NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l7=Label(self.root,text="______________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l7.place(x=0,y=170)
        l4=Label(self.root,text="BOOK ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e2.place(x=10,y=240)
        l5=Label(self.root,text="AUTHOR",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=280)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e3.place(x=10,y=320)
        l6=Label(self.root,text="PUBLISHER",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=360)
        self.e4=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e4.place(x=10,y=390)
        btndele=Button(self.root,text="DELETE",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.deletebook)
        btndele.place(x=160,y=440)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchbook)
        btnsearch.place(x=300,y=130)
        self.root.resizable(0,0)
        
    def deletebook(self):
        
        
        ax1 = self.e1.get()
        ax2 = self.e2.get()
        ax3 = self.e3.get()
        ax4 = self.e4.get()
        
        if(ax1 == ""):
            messagebox.showinfo("Delete Status","ID is Necessary to delete")
        else:
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("delete from book_add where book_id='"+ ax1 +"'")
            cursor.execute("commit");

        
            messagebox.showinfo("Delete Status","Deleted Successfully")
            con.close()
        
        
        
               
             
#        self.root.destroy()
        
    def searchbook(self):
        
       
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        
        
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from book_add where book_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows :
            self.e2.insert(0, row[1])
            self.e3.insert(0, row[2])
            self.e4.insert(0, row[3])
        con.close()
        
        
    
    
        
class librarians:
    def __init__(self,std):
        self.root=std
        self.hgth=410
        self.wdth=400
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x410+%d+%d'%(self.width,self.height))
        self.root.iconbitmap(r'book.ico')
        menuu=Menu(self.root)
        menuu.add_command(label='VIEW',command=self.viewdatabase)
        menuu.add_command(label='DELETE',command=self.deletelibrariann)
        menuu.add_command(label='UPDATE',command=self.updatelibrariann)
        self.root.config(menu=menuu)
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="ADD EMPLOYEE INFO",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=80,y=10) 
        l2=Label(self.root,text="_____________________________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=70,y=70)
        l4=Label(self.root,text="EMPLOYEE NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l3=Label(self.root,text="CONTACT NO.",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=170)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e2.place(x=10,y=200)
        l=Label(self.root,text="EMPLOYEE ID",font=mfont1,fg="BLACK",bg="WHITE")
        l.place(x=10,y=230)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e3.place(x=10,y=260)
        l4=Label(self.root,text="ADDRESS",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=290)
        self.e4=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e4.place(x=10,y=320)
      
        btnreturn=Button(self.root,text="ADD",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.libinfo)
        btnreturn.place(x=150,y=360)
        self.root.resizable(0,0)
    def libinfo(self):
        
        if(self.e1.get()=="" or self.e2.get()==""  or self.e3.get()==""):
            messagebox.showinfo("Insert Status","All Fields are required")
        else:    
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
         
            cursor.execute("insert into employee_info values('"+ self.e1.get() +"','"+ self.e2.get() +"','"+ self.e3.get() +"','"+ self.e4.get() +"')")     
            cursor.execute("commit");
         
            messagebox.showinfo("Insert Status","Inserted Successfully")
        con.close()
        
        
        
        
        
        
        
        
        self.root.destroy()
    def viewdatabase(self):
        
        vlibrarian=Tk()
        viewLibrarian(vlibrarian)
        vlibrarian.mainloop()
        
    def updatelibrariann(self):
        udpl=Tk()
        updatelibrarian(udpl)
        udpl.mainloop()
    def deletelibrariann(self):
    
        dltsb=Tk()
        dellibrarian(dltsb)
        dltsb.mainloop()
class studentsinfo:
    def __init__(self,std):
        
        self.root=std
        self.hgth=500
        self.wdth=400
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x500+%d+%d'%(self.width,self.height))
        self.root.iconbitmap(r'book.ico')
        menuu=Menu(self.root)
        menuu.add_command(label='VIEW',command=self.viewdatabase)
        menuu.add_command(label='DELETE',command=self.deletestudent)
        menuu.add_command(label='UPDATE',command=self.updatestudent)
        self.root.config(menu=menuu)
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="ADD STUDENT INFO",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=80,y=10) 
        l2=Label(self.root,text="_____________________________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=70,y=70)
        l4=Label(self.root,text="STUDENT NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l3=Label(self.root,text="CONTACT NO.",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=170)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e2.place(x=10,y=200)
        l=Label(self.root,text="LIB. ID",font=mfont1,fg="BLACK",bg="WHITE")
        l.place(x=10,y=230)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e3.place(x=10,y=260)
        l4=Label(self.root,text="UNIQUE ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=290)
        self.e4=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e4.place(x=10,y=320)
        l5=Label(self.root,text="COURSE",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=350)
        self.e5=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e5.place(x=10,y=380)
        btnadd=Button(self.root,text="ADD",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.stdinfo)
        btnadd.place(x=150,y=440)
        self.root.resizable(0,0)
    def stdinfo(self):
        
        
    
        if(self.e1.get()=="" or self.e2.get()==""  or self.e3.get()==""  or self.e4.get()==""  or self.e5.get()==""):
            messagebox.showinfo("Insert Status","All Fields are required")
        else:    
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
         
            cursor.execute("insert into student_info values('"+ self.e1.get() +"','"+ self.e2.get() +"','"+ self.e3.get() +"','"+ self.e4.get() +"','"+ self.e5.get() +"')")     
            cursor.execute("commit");
      
         
            messagebox.showinfo("Insert Status","Inserted Successfully")
        con.close()
        
        
        self.root.destroy()
    def viewdatabase(self):
        
        vstud=Tk()
        viewStudent(vstud)
        vstud.mainloop()
    def updatestudent(self):
        
        udp=Tk()
        updatestudents(udp)
        udp.mainloop()
    def deletestudent(self):
        
      
        dlts=Tk()
        delstudents(dlts)
        dlts.mainloop()
class returnbooks:
    def __init__(self,rtb):
        
        self.root=rtb
        self.hgth=500
        self.wdth=400
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        self.root.geometry('400x500+%d+%d'%(self.width,self.height))
        self.root.iconbitmap(r'book.ico')
        menuu=Menu(self.root)
        menuu.add_command(label='VIEW',command=self.viewdatabase)
        self.root.config(menu=menuu)
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="RETURN BOOKS",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=110,y=10) 
        l2=Label(self.root,text="____________________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=90,y=70)
        l4=Label(self.root,text="LIB. ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=20)
        self.e1.place(x=10,y=130)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchbook3)
        btnsearch.place(x=300,y=130)
        l71=Label(self.root,text="______________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l71.place(x=0,y=170)
        l3=Label(self.root,text="BOOK NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e2=Entry(self.root,relief="sunken",bd=4,width=30)
        self.e2.place(x=10,y=240)
        l5=Label(self.root,text="STUDENT NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=10,y=280)
        self.e3=Entry(self.root,relief="sunken",bd=4,width=30)
        self.e3.place(x=10,y=320)
        l6=Label(self.root,text="BOOK ID",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=360)
        self.e11=Entry(self.root,relief="sunken",bd=4,width=30)
        self.e11.place(x=10,y=390)
        l7=Label(self.root,text="ISSUE DATE",font=mfont1,fg="BLACK",bg="WHITE")
        l7.place(x=250,y=210)
        self.e12=DateEntry(self.root,relief="sunken",bd=4,width=20)
        self.e12.place(x=250,y=240)
        self.e12.delete(0, 'end')
        l5=Label(self.root,text="RETURN DATE",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=250,y=280)
        self.e31=DateEntry(self.root,relief="sunken",bd=4,width=20)
        self.e31.place(x=250,y=320)
        self.e31.delete(0, 'end')
        btnretn=Button(self.root,text="RETURN",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.returnboook)
        btnretn.place(x=150,y=440)
        self.root.resizable(0,0)
    def returnboook(self):
        
        ca1 = datetime.strptime(self.e12.get(),"%m/%d/%y")
        ca2 = datetime.strftime(ca1,"%Y-%m-%d")
        
        ga1 = datetime.strptime(self.e31.get(),"%m/%d/%y")
        ga2 = datetime.strftime(ga1,"%Y-%m-%d")
        
        if(self.e1.get()=="" or self.e2.get()=="" or self.e3.get()=="" or self.e11.get()=="" or self.e12.get()=="" or self.e31.get()==""):
            messagebox.showinfo("Insert Status","All Fields are required")
        else:    
            
            
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            
            cursor.execute("insert into book_return values('"+ self.e1.get() +"','"+ self.e2.get() +"','"+ self.e3.get() +"','"+ self.e11.get() +"','"+ ca2 +"','"+ ga2 +"')")     
            cursor.execute("commit");
         

            messagebox.showinfo("Insert Status","Inserted Successfully")
            con.close()
        
        
        self.root.destroy()
    def searchbook3(self):
        
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e11.delete(0, 'end')
        self.e12.delete(0, 'end')
        
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
           
            self.e2.delete(0, 'end')
            self.e3.delete(0, 'end')
            self.e11.delete(0, 'end')
            self.e12.delete(0, 'end')
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from book_issue where lib_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows:
            self.e2.insert(0, row[1])
            self.e3.insert(0, row[7])
            
            self.e11.insert(0, row[0])
            self.e12.insert(0, row[9])
            
        a2 = self.e12.get()
        self.e12.delete(0, 'end')
        fa1 = datetime.strptime(a2,"%Y-%m-%d")   
        fa2 = datetime.strftime(fa1,"%m/%d/%Y")    
        fa3 = datetime.strptime(fa2,"%m/%d/%Y")    
        fa4 = datetime.strftime(fa3,"%m/%d/%y")
        self.e12.insert(0,fa4)
        
        con.close() 
        
        
        
        
        
        

        
    
        
    def viewdatabase(self):
        
        vreturn=Tk()
        viewReturn(vreturn)
        vreturn.mainloop()
class issuebook:
    def __init__(self,isb):
        self.root=isb
        self.root.iconbitmap(r'book.ico')
        self.wdth=800
        self.hgth=700
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.title("Library Management System")
        mfont1=Font(self.root,family="Times",size=14)
        mfont=Font(self.root,family="Comic Sans MS",size=16,weight="bold")
        menuu=Menu(self.root)
        menuu.add_command(label='VIEW',command=self.viewdatabase)
        self.root.config(menu=menuu)
        self.root.geometry('650x700+%d+%d'%(self.width,self.height))
        l11=Label(self.root,bg="WHITE",font=mfont1,height=500,width=400)
        l11.place(x=0,y=0)
        l1=Label(self.root,text="ISSUE BOOKS",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
        l1.place(x=250,y=10)
        l2=Label(self.root,text="_________________________________",fg="GREEN",bg="WHITE")
        l2.place(x=250,y=70)
        l3=Label(self.root,text="BOOK NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=210)
        self.e1=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e1.place(x=10,y=130)
        l71=Label(self.root,text="______________________________________________________________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l71.place(x=0,y=170)
        l4=Label(self.root,text="BOOK ID",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=10,y=100)
        self.e11=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e11.place(x=10,y=240)
        l5=Label(self.root,text="AUTHOR",font=mfont1,fg="BLACK",bg="WHITE")
        l5.place(x=350,y=210)
        self.e12=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e12.place(x=350,y=240)
        l6=Label(self.root,text="PUBLISHER",font=mfont1,fg="BLACK",bg="WHITE")
        l6.place(x=10,y=280)
        self.e13=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e13.place(x=10,y=310)
        l7=Label(self.root,text="COST",font=mfont1,fg="BLACK",bg="WHITE")
        l7.place(x=350,y=280)
        self.e14=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e14.place(x=350,y=310)
        l8=Label(self.root,text="CATEGORY",font=mfont1,fg="BLACK",bg="WHITE")
        l8.place(x=350,y=350)
        self.e15=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e15.place(x=350,y=380)
        l9=Label(self.root,text="ATTRIBUTE",font=mfont1,fg="BLACK",bg="WHITE")
        l9.place(x=10,y=350)
        self.e16=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e16.place(x=10,y=380)
        l71=Label(self.root,text="_____________________________________________________________________________________________________________________________________",fg="GREEN",bg="WHITE")
        l71.place(x=0,y=420)
        l3=Label(self.root,text="STUDENT NAME",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=460)
        self.e17=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e17.place(x=10,y=490)
        l3=Label(self.root,text="LIB. ID",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=10,y=530)
        self.e18=Entry(self.root,relief="sunken",bd=4,width=40)
        self.e18.place(x=10,y=560)
        l3=Label(self.root,text="DATE",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=350,y=460)
        self.e2=DateEntry(self.root,relief="sunken",bd=4,width=40,selectmode="day")
        self.e2.place(x=350,y=490)
        self.e2.delete(0, 'end')
        btnissue=Button(self.root,text="ISSUE",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.issueboook,width=15)
        btnissue.place(x=250,y=600)
        btnsearch=Button(self.root,text="SEARCH",fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.searchbook2)
        btnsearch.place(x=400,y=130)
        self.root.resizable(0,0)
    def issueboook(self):
        
         
        da1 = datetime.strptime(self.e2.get(),"%m/%d/%y")
        da2 = datetime.strftime(da1,"%Y-%m-%d")
        
        if(self.e1.get()=="" or self.e2.get()=="" or self.e11.get()=="" or self.e12.get()=="" or self.e13.get()=="" or self.e14.get()=="" or self.e15.get()=="" or self.e16.get()=="" or self.e17.get()=="" or self.e18.get()==""):
            messagebox.showinfo("Insert Status","All Fields are required")
        else:    
            
            
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            
            cursor.execute("insert into book_issue values('"+ self.e1.get() +"','"+ self.e11.get() +"','"+ self.e13.get() +"','"+ self.e16.get() +"','"+ self.e12.get() +"','"+ self.e14.get() +"','"+ self.e15.get() +"','"+ self.e17.get() +"','"+ self.e18.get() +"','"+ da2 +"')")     
            cursor.execute("commit");

            messagebox.showinfo("Insert Status","Inserted Successfully")
            con.close()
        
        
        
        self.root.destroy()
        
        
        
        
        
    def searchbook2(self):
        
        
        self.e11.delete(0, 'end')
        self.e12.delete(0, 'end')
        self.e13.delete(0, 'end')
        self.e14.delete(0, 'end')
        self.e15.delete(0, 'end')
        self.e16.delete(0, 'end')
        
        if(self.e1.get() == ""):
            messagebox.showinfo("Fetch Status","ID is Necessary to delete")
        else:
        
            con = mysql.connect(host="localhost", user="root",password="", database="library_management")
            cursor = con.cursor()
            cursor.execute("select * from book_add where book_id='"+ self.e1.get() +"'")
            rows = cursor.fetchall()
        
        for row in rows:
            self.e11.insert(0, row[0])
            self.e12.insert(0, row[2])
            self.e13.insert(0, row[3])
            self.e14.insert(0, row[4])
            self.e15.insert(0, row[5])
            self.e16.insert(0, row[6])
            
        con.close() 
        
    def viewdatabase(self):
        
        vissue=Tk()
        viewIssue(vissue)
        vissue.mainloop()
        
class books:
    def __init__(self):
         
         top=Toplevel()
         wdth=400
         hgth=640
         width=(top.winfo_screenwidth()/2)-(wdth/2)
         height=(top.winfo_screenheight()/2)-(hgth/2)
         top.geometry('%dx%d+%d+%d'%(wdth,hgth,width,height))
         top.iconbitmap(r'book.ico')
         mfont1=Font(family="Times",size=14)
         mfont2=Font(family="Comic Sans MS",size=14)
         l1=Label(top,bg="WHITE",font=mfont1,height=hgth,width=wdth)
         l1.place(x=0,y=0)
         l10=Label(top,text="________________________________",fg="GREEN",bg="WHITE")
         l10.place(x=120,y=80)
         mfont=Font(family="Comic Sans MS",size=20,weight="bold")
         l2=Label(top,text="ADD BOOKS TO LIBRARY",font=mfont,fg="green",bg="WHITE",bd=5,relief="raised")
         l2.place(x=10,y=10) 
         l3=Label(top,text="BOOK NAME",font=mfont1,fg="BLACK",bg="WHITE")
         l3.place(x=10,y=140)
         self.e1=Entry(top,relief="sunken",bd=4,width=40)
         self.e1.place(x=10,y=170)
         l4=Label(top,text="BOOK ID",font=mfont1,fg="BLACK",bg="WHITE")
         l4.place(x=10,y=200)
         self.e2=Entry(top,relief="sunken",bd=4,width=40)
         self.e2.place(x=10,y=230)
         l5=Label(top,text="AUTHOR",font=mfont1,fg="BLACK",bg="WHITE")
         l5.place(x=10,y=260)
         self.e3=Entry(top,relief="sunken",bd=4,width=40)
         self.e3.place(x=10,y=290)
         l6=Label(top,text="PUBLISHER",font=mfont1,fg="BLACK",bg="WHITE")
         l6.place(x=10,y=320)
         self.e4=Entry(top,relief="sunken",bd=4,width=40)
         self.e4.place(x=10,y=350)
         l7=Label(top,text="COST",font=mfont1,fg="BLACK",bg="WHITE")
         l7.place(x=10,y=380)
         self.e5=Entry(top,relief="sunken",bd=4,width=40)
         self.e5.place(x=10,y=410)
         l8=Label(top,text="CATEGORY",font=mfont1,fg="BLACK",bg="WHITE")
         l8.place(x=10,y=440)
         self.e6=Entry(top,relief="sunken",bd=4,width=40)
         self.e6.place(x=10,y=470)
         l9=Label(top,text="ATTRIBUTE",font=mfont1,fg="BLACK",bg="WHITE")
         l9.place(x=10,y=500)
         self.e7=Entry(top,relief="sunken",bd=4,width=40)
         self.e7.place(x=10,y=530)
         btnadd=Button(top,text="ADD",font=mfont2,fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.addbook)
         btnadd.place(x=160,y=580)
         
         menuu=Menu(top)
         submenu=Menu(menuu,tearoff=0)
         
         menuu.add_cascade(label='BOOKS',menu=submenu)
        
         submenu.add_command(label='DELETE',command=self.delebooks)
         submenu.add_command(label='UPDATE',command=self.updatebooks)
         submenu.add_command(label='VIEW',command=self.viewbooks)
         
         
         
         top.config(menu=menuu)
         top.resizable(0,0)
         top.mainloop()
    def updatebooks(self):
         upk=Tk()
         updatebook(upk)
         upk.mainloop()
    def viewbooks(self):
        
        vbook=Tk()
        viewBOOK(vbook)
        vbook.mainloop()
      
    def addbook(self):
      

         

         if(self.e1.get()=="" or self.e2.get()==""  or self.e3.get()=="" or self.e4.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()==""):
             messagebox.showinfo("Insert Status","All Fields are required")
         else:    
             con = mysql.connect(host="localhost", user="root",password="", database="library_management")
             cursor = con.cursor()
             cursor.execute("insert into book_add values('"+ self.e1.get() +"','"+ self.e2.get() +"','"+ self.e3.get() +"','"+ self.e4.get() +"','"+ self.e5.get() +"','"+ self.e6.get() +"','"+ self.e7.get() +"')")     
             cursor.execute("commit")
  
             
             messagebox.showinfo("Insert Status","Inserted Successfully")
             con.close()

         self.root.destroy()
    def delebooks(self):
       
        el=Tk()
        delbooks(el)    
        el.mainloop()
class functionswindow:
    def __init__(self):
        main=Tk()
        main.iconbitmap(r'book.ico')
        main.title("LIBRARY MANAGEMENT SYSTEM")
        widthh=400
        heigthh=400
        mfont2=Font(family="Comic Sans MS",size=14)
        
        f1=Frame(main,height=heigthh,width=widthh)
        f1.place(x=0,y=0)
        l1=Label(f1,bg="WHITE",height=heigthh,width=widthh)
        l1.place(x=0,y=0)
        btnbooks=Button(text="BOOKS",font=mfont2,fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.bookss,width=10)
        btnbooks.place(x=130,y=50)
        btnissue=Button(text="ISSUE",font=mfont2,fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.issue,width=10)
        btnissue.place(x=130,y=110)
        btnreturn=Button(text="RETURN",font=mfont2,fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.returnbook,width=10)
        btnreturn.place(x=130,y=170)
        btnstudents=Button(text="STUDENTS",font=mfont2,fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.students,width=10)
        btnstudents.place(x=130,y=230)
        btnstudents=Button(text="LIBRARIAN",font=mfont2,fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.librarian,width=10)
        btnstudents.place(x=130,y=290)
        widht=(main.winfo_screenwidth()/2)-(widthh/2)
        height=(main.winfo_screenheight()/2)-(heigthh/2)
        main.geometry('%dx%d+%d+%d'%(widthh,heigthh,widht,height))
        main.resizable(0,0)
        main.mainloop()
    def bookss(self):
        books()
    def issue(self):
      
        isb=Tk()
        issuebook(isb)
        isb.mainloop()
    def returnbook(self):
      
         rtb=Tk()
         obj=returnbooks(rtb)
         rtb.mainloop()
    def students(self):
       
         std=Tk()
         obj=studentsinfo(std)
         std.mainloop()
    def librarian(self):
         
         lib=Tk()
         librarians(lib)
         lib.mainloop()
class loginwindow:
    def __init__(self,win):
        self.root=win
        self.root.iconbitmap(r'book.ico')
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.et1=StringVar()
        self.et2=StringVar()
        mfont=Font(family="Comic Sans MS",size=20,weight="bold")
        mfont2=Font(family="Comic Sans MS",size=14)
        mfont1=Font(family="Times",size=14)
        self.wdth=400
        self.hgth=400
        self.width=(self.root.winfo_screenwidth()/2)-(self.wdth/2)
        self.height=(self.root.winfo_screenheight()/2)-(self.hgth/2)
        self.root.geometry('400x400+%d+%d'%(self.width,self.height))
        f1=Frame(self.root,bg="WHITE",height=400,width=400)
        f1.place(x=0,y=0)
        l1=Label(f1,text="SIGN IN TO LIBRARY!!",font=mfont,fg="GREEN",bg="WHITE",relief="raised",bd=5)
        l1.place(x=40,y=10)
        l2=Label(f1,text="________________________",fg="GREEN",bg="WHITE")
        l2.place(x=130,y=60)
        l3=Label(f1,text="UserName",font=mfont1,fg="BLACK",bg="WHITE")
        l3.place(x=50,y=100)
        e1=Entry(relief="sunken",bd=4,width=40,textvariable=self.et1)
        e1.place(x=50,y=130)
        l4=Label(f1,text="PassWord",font=mfont1,fg="BLACK",bg="WHITE")
        l4.place(x=50,y=170)
        e2=Entry(relief="sunken",bd=4,width=40,textvariable=self.et2)
        e2.place(x=50,y=200)
        l5=Button(f1,text="Forgot Password?",font=mfont1,fg="RED",bg="WHITE",command=self.click)
        l5.place(x=250,y=250)
        btnlogin=Button(text="LOGIN",font=mfont2,fg="WHITE",bg="GREEN",relief="raised",bd=5,command=self.clicked)
        btnlogin.place(x=160,y=300)
        win.resizable(0,0)
        win.mainloop()
    def clicked(self):
        if(self.et1.get()=="" or self.et2.get()==""):

            con1=Tk()
            con1.iconbitmap(r'book.ico')
            con1.title("Confirmation")
            wdth=300
            hgth=100
            width=(con1.winfo_screenwidth()/2)-(wdth/2)
            height=(con1.winfo_screenheight()/2)-(hgth/2)
            con1.geometry('%dx%d+%d+%d'%(wdth,hgth,width,height))
            l1=Label(con1,text="Fill All Details")
            l1.place(x=150,y=10)
            con1.resizable(0,0)
            con1.mainloop()
        elif(self.et1.get()=="admin" and self.et2.get()=="admin123"):
            
            self.root.destroy()
           
            functionswindow()
    
        else:
           
            con1=Tk()
            con1.iconbitmap(r'book.ico')
            con1.title("Confirmation")
            wdth=300
            hgth=100
            width=(con1.winfo_screenwidth()/2)-(wdth/2)
            height=(con1.winfo_screenheight()/2)-(hgth/2)
            con1.geometry('%dx%d+%d+%d'%(wdth,hgth,width,height))
            l1=Label(con1,text="Login Unsuccessful")
            l1.place(x=150,y=10)
            con1.resizable(0,0)
            con1.mainloop()
    def click(self):
        con=Tk()
        con.iconbitmap(r'book.ico')
        wdth=300
        hgth=300
        mfont1=Font(family="Times",size=14)
        width=(win.winfo_screenwidth()/2)-(wdth/2)
        height=(win.winfo_screenheight()/2)-(hgth/2)
        con.title("Confirmation")
        l1=Label(con,text="UserName",font=mfont1)
        l1.place(x=80,y=30)
        e1=Entry(con,relief="sunken")
        e1.place(x=80,y=60)
        l1=Label(con,text="Old PassWord",font=mfont1)
        l1.place(x=80,y=90)
        e2=Entry(con,relief="sunken")
        e2.place(x=80,y=120)
        l1=Label(con,text="New PassWord",font=mfont1)
        l1.place(x=80,y=150)
        e3=Entry(con,relief="sunken")
        e3.place(x=80,y=180)
        btn=Button(con,text="OK",bg="WHITE")
        btn.place(x=140,y=240)
        con.geometry('%dx%d+%d+%d'%(wdth,hgth,width,height))
        con.resizable(0,0)
        con.mainloop()

win=Tk()
loginwindow(win)
win.mainloop()
    
     
        

    