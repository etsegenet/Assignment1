from tkinter import Tk , StringVar,ttk
from tkinter import *
import time;
import datetime
root = Tk()
root.title("Attendance")
root.geometry('1350x650+0+0')
root.configure(background = 'black')
LeftMayFrame = Frame(root,width = 1000 , height = 650 , bd=8 , relief = "raise")
LeftMayFrame.pack(side = LEFT)
RightMayFrame =Frame(root , width = 350,height = 650 , bd=8,relief = "raise")
RightMayFrame.pack(side = RIGHT)
LeftMayFrame1 = Frame(LeftMayFrame , width = 1000 , height = 100 ,bd=8 ,relief ="raise")
LeftMayFrame1.pack(side = TOP)
LeftMayFrame2 =Frame(LeftMayFrame, width =1000 , height= 550 , bd = 8,relief ="raise")
LeftMayFrame2.pack(side = TOP)
RightMayFrame1 = Frame(RightMayFrame , width =350 ,height =215 , bd = 8 ,relief ="raise").pack(side = TOP)
RightMayFrame2 = Frame(RightMayFrame , width =350 ,height =215 , bd = 8 , relief ="raise").pack(side = TOP)
#,...........................localtime..........................................................
localtime=time.asctime(time.localtime(time.time()))
#.................................left side informations.................................

#.........................images...................................
'''cont1 = Canvas(RightMayFrame2 , width = 350 , height = 425 ,bg = "black")
cont1.grid()
image5 = PhotoImage(file ="img2.gif")
cont1.create_image(200,200)
#...............image of students frame1 .................................
cont= Canvas(RightMayFrame1 , width = 350 , height = 215 ,bg = "black")
cont.grid(row = 0 ,column = 0)
image1 = PhotoImage(file ="img2.gif")
image = cont.create_image(336,208 , image = image1)
#................image....................................
def pic1():
    image = cont.create_image(200,200 , image = image1)
image1 = PhotoImage(file = "img2.gif")
def pic2():
    image = cont.create_image(200,200 , image = image2)
image2= PhotoImage(file = "img2.gif")
def pic3():
    image = cont.create_image(200,200 , image = image3)
image3 = PhotoImage(file = "img2.gif")

def pic4():
    image = cont.create_image(200,200 , image = image4)
image4 = PhotoImage(file = "img2.gif")
def pic5():
    image = cont.create_image(200,200 , image = image5)
image5 = PhotoImage(file = "img2.gif")
def pic6():
    image = cont.create_image(200,200 , image = image6)
image6 = PhotoImage(file = "img2.gif")

def pic7():
    image = cont.create_image(200,200 , image = image7)
image7 = PhotoImage(file = "img2.gif")
def pic8():
    image = cont.create_image(200,200 , image = image8)
image8 = PhotoImage(file = "img2.gif")'''
     

#..................variables.....................................
DateofOrder = StringVar()
Value0 = StringVar()
Value1= StringVar()
Value2= StringVar()
Value3= StringVar()
Value4= StringVar()
Value5= StringVar()
Value6= StringVar()
Value7= StringVar()
Value8= StringVar()
Value9= StringVar()
Value10= StringVar()
Value11= StringVar()
Value12= StringVar()
Value13= StringVar()
Value14= StringVar()
Value15= StringVar()
def Mark_Register():
    if Value0.get() == "/" :
        Value1. set("/")
        Value2. set("/")
        Value3. set("/")
        Value4. set("/")
        Value5. set("")
        Value6. set("/")
        Value7. set("/")
        Value8. set("/")
        Value9. set("/")
        Value10. set("/")
        Value11. set("/")
        Value12. set("/")
        Value13. set("/")
        Value14. set("/")
        Value15. set("/")
    elif(Value0.get() == "A"):
        Value1. set("A")
        Value2. set("A")
        Value3. set("A")
        Value4. set("A")
        Value5. set("A")
        Value6. set("A")
        Value7. set("A")
        Value8. set("A")
        Value9. set("A")
        Value10. set("A")
        Value11. set("A")
        Value12. set("A")
        Value13. set("A")
        Value14. set("A")
        Value15. set("A")
    elif(Value0.get() == "p"):
        Value1. set("p")
        Value2. set("p")
        Value3. set("p")
        Value4. set("p")
        Value5. set("p")
        Value6. set("p")
        Value7. set("p")
        Value8. set("p")
        Value9. set("p")
        Value10. set("p")
        Value11. set("p")
        Value12. set("p")
        Value13. set("p")
        Value14. set("p")
        Value15. set("p")
    elif(Value0.get() == "L"):
        Value1. set("L")
        Value2. set("L")
        Value3. set("L")
        Value4. set("L")
        Value5. set("L")
        Value6. set("L")
        Value7. set("L")
        Value8. set("L")
        Value9. set("L")
        Value10. set("L")
        Value11. set("L")
        Value12. set("L")
        Value13. set("L")
        Value14. set("L")
        Value15. set("L")
def Reset():
    Value0 . set("")
    Value1. set("")
    Value2. set("")
    Value3. set("")
    Value4. set("")
    Value5. set("")
    Value6. set("")
    Value7. set("")
    Value8. set("")
    Value9. set("")
    Value10. set("")
    Value11. set("")
    Value12. set("")
    Value13. set("")
    Value14. set("")
    Value15. set("")
    
def qExit():
    qExit = messagebox.askyesno("Exit System","Do you want to quit?")
    if qExit>0:
        root.destroy()
        return
    
    
#..............comboBox............................................
#lblInfo=Label(RightMayFrame ,font=('helvetica',20,'bold'),text="WELCOME TO BEGIZE ATTENDANCE",bd=10)
#lblInfo.grid(row = 1,column = 0)

#lblInfo=Label(RightMayFrame,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10)
#lblInfo.grid(row = 1,column = 0)
lblNo = Label(LeftMayFrame1, font=('arial' , 10 ,'bold'), text ="No." ,bd =16)
lblNo.grid(row=0 ,column =0 ,sticky = W)
lblStudentNo = Label(LeftMayFrame1 , font=('arial' , 10 ,'bold'), text ="Student No" ,bd =16)
lblStudentNo.grid(row=0 ,column =1 ,sticky = W)
lblStudentName = Label(LeftMayFrame1 , font=('arial' , 10 ,'bold'), text ="Student Name" ,bd =16)
lblStudentName.grid(row=0 ,column =2 ,sticky = W)
lblCourseCode = Label(LeftMayFrame1 , font=('arial' , 10 ,'bold'), text ="Course Code" ,bd =16)
lblCourseCode.grid(row=0 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame1 , textvariable = Value0,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box['values'] = ('' , 'A'  ,'p' , 'L')
box.current(0)
box.grid(row =0 , column = 4)
btnFill = Button(LeftMayFrame1 , text = 'Fill' ,padx = 2 , pady = 2 ,bd =2,fg = "black" , font =('arail','10' ,'bold'),width = 12 , height =1,command = Mark_Register).grid(row= 0,column =5)
btnResset = Button(LeftMayFrame1 , text = 'Reset' ,padx = 2 , pady = 2 ,bd =2,fg = "black" , font =('arail','10' ,'bold'),width = 12 , height =1,command=Reset).grid(row= 0,column =6)
btnExit = Button(LeftMayFrame1 , text = 'Exit' ,padx = 2 , pady = 2 ,bd =2,fg = "black" , font =('arail','10' ,'bold'),width = 12 , height =1,command=qExit).grid(row= 0,column =7)
lblDateofOrder = Label(LeftMayFrame1 , font=('arial' , 10 ,'bold'), textvariable =DateofOrder ,padx = 2,pady =2 , fg  = 'black',bg ='white' , bd =16 ).grid(row = 0 ,column = 8,sticky = W)

#................................LeftMayFrame1...................
lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1" ,bd =16)
lblNo.grid(row=1 ,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/8845/08" ,bd =16)
lblStudent_No_1.grid(row=1 ,column =1,sticky = W)
lblStudent_Name = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="Ezrael" ,bd =16)
lblStudent_Name.grid(row=1 ,column = 2,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1415" ,bd =16)
lblCourse_Code.grid(row=1 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value1,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(0)
box.grid(row =1 , column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 1 , column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 1 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 1 , column = 7)

#...................LeftMayFrame1 row2.............................
lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="2" ,bd =16)
lblNo.grid(row=2 ,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/2314/08" ,bd =16)
lblStudent_No_1.grid(row=2,column =1 ,sticky = W)
lblStudent_Name = Label(LeftMayFrame2, font=('arial' , 10 ,'bold'), text ="Eden" ,bd =16)
lblStudent_Name.grid(row=2 ,column =2 ,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1415" ,bd =16)
lblCourse_Code.grid(row=2 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value2,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(1)
box.grid(row = 2, column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 2 , column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 2 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 2 , column = 7)
#...................LeftMayFrame1 row3.............................

lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="3" ,bd =16)
lblNo.grid(row=3 ,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/3564/08" ,bd =16)
lblStudent_No_1.grid(row=3,column =1 ,sticky = W)
lblStudent_Name = Label(LeftMayFrame2, font=('arial' , 10 ,'bold'), text ="Alex" ,bd =16)
lblStudent_Name.grid(row=3 ,column =2 ,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1212" ,bd =16)
lblCourse_Code.grid(row=3 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value3,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(1)
box.grid(row=3, column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1 ).grid(row=3 , column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row=3 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row=3 , column = 7)
#................................LeftMayFrame1...................
lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="4" ,bd =16)
lblNo.grid(row=4 ,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/1245/08" ,bd =16)
lblStudent_No_1.grid(row=4 ,column =1,sticky = W)
lblStudent_Name = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="melkam" ,bd =16)
lblStudent_Name.grid(row=4 ,column = 2,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1415" ,bd =16)
lblCourse_Code.grid(row=4 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value4,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(0)
box.grid(row =4 , column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1 ).grid(row = 4 , column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 4 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 4 , column = 7)

#...................LeftMayFrame1 row2.............................
#................................LeftMayFrame5...................
lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="5" ,bd =16)
lblNo.grid(row=5 ,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/6066/08" ,bd =16)
lblStudent_No_1.grid(row=5 ,column =1,sticky = W)
lblStudent_Name = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="Ezra" ,bd =16)
lblStudent_Name.grid(row=5 ,column = 2,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1415" ,bd =16)
lblCourse_Code.grid(row=5 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value5,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(0)
box.grid(row =5 , column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 5 , column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 5 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 5 , column = 7)

#...................LeftMayFrame1 row2.............................
#................................LeftMayFrame6...................
lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="6" ,bd =16)
lblNo.grid(row=6,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/8279/08" ,bd =16)
lblStudent_No_1.grid(row=6 ,column =1,sticky = W)
lblStudent_Name = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="Rodas" ,bd =16)
lblStudent_Name.grid(row=6 ,column = 2,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1415" ,bd =16)
lblCourse_Code.grid(row=6 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value6,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(0)
box.grid(row =6 , column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 6 , column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 6 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 6 , column = 7)

#...................LeftMayFrame1 row2.............................
#................................LeftMayFrame1...................
lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="7" ,bd =16)
lblNo.grid(row=7 ,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/9045/08" ,bd =16)
lblStudent_No_1.grid(row=7 ,column =1,sticky = W)
lblStudent_Name = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="Tkkl" ,bd =16)
lblStudent_Name.grid(row=7 ,column = 2,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1415" ,bd =16)
lblCourse_Code.grid(row=7 ,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value7,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(0)
box.grid(row =7 , column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 7 , column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 7 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 7 , column = 7)

#...................LeftMayFrame1 row2.............................
#................................LeftMayFrame1...................
lblNo = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="8" ,bd =16)
lblNo.grid(row=8 ,column =0 ,sticky = W)
lblStudent_No_1 = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="ATR/8845/08" ,bd =16)
lblStudent_No_1.grid(row=8 ,column =1,sticky = W)
lblStudent_Name = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="Alemayehu" ,bd =16)
lblStudent_Name.grid(row=8 ,column = 2,sticky = W)
lblCourse_Code = Label(LeftMayFrame2 , font=('arial' , 10 ,'bold'), text ="1415" ,bd =16)
lblCourse_Code.grid(row=8,column =3 ,sticky = W)
box = ttk.Combobox(LeftMayFrame2 , textvariable = Value8,state = 'readonly')
box['values'] = (' ' , 'A'  ,'p' , 'L')
box.current(0)
box.grid(row =8, column = 4)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row =8, column = 5)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 8 , column = 6)
btnSpace = Button (LeftMayFrame2 , text='',padx = 2 , pady = 2 ,bd = 2 , fg = "black",
                   font=('arial' , 10 ,'bold'),width = 12 , height = 1).grid(row = 8 , column = 7)

#...................LeftMayFrame1 row2.............................

root.mainloop()
