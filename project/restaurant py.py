#........etsegenet melese .............
#.........ATR/8845/08..................
from tkinter import *
import random
import time;
root = Tk()
root.geometry("1600x800+0+0")
root.title("resturant managment system")
text_Input=StringVar()
operator = ""
Tops = Frame(root,width = 100,height = 50,  bg = "powder blue" , relief=SUNKEN)
Tops.pack(side= TOP)
f1=Frame(root , width=100, height = 700,relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root , width=100, height = 700 , bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)
#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="MENEN MGBET MANAGEMENT",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Dorowet.get()==""):
        CoDorowet=0
    else:
        CoDorowet=float(Dorowet.get())


    
    if (Pizza.get()==""):
        CoPizza=0
    else:
        CoPizza=float(Pizza.get())



    if (Salad.get()==""):
        CoSalad=0
    else:
        CoSalad=float(Salad.get())



    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

        
    if (Pasta.get()==""):
        CoPasta=0
    else:
        CoPasta=float(Pasta.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofDorowet =CoDorowet * 140
    CostofDrinks=CoD * 65
    CostofPizza = CoPizza* 90
    CostofSalad = CoSalad * 140
    CostBurger = CoBurger* 260
    CostPasta=CoPasta * 300

    CostofMeal= "Birr", str(CostofDorowet+CostofDrinks+CostofPizza+CostofSalad+CostBurger+CostPasta)

    PayTax=((CostofDorowet+CostofDrinks+CostofPizza+CostofSalad+CostBurger+CostPasta) * 2)

    TotalCost=(CostofDorowet+CostofDrinks+CostofPizza+CostofSalad+CostBurger+CostPasta)
 
    #Ser_Charge= ((CostofDorowet+CostofDrinks+CostofPizza+CostofSalad+CostBurger+CostPasta)/99)

    Service = "Birr", str (PayTax+TotalCost)

    OverAllCost ="Birr", str (PayTax+TotalCost)

    PaidTax= "Birr", str (PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Dorowet.set("")
    Pizza.set("")
    Salad.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Pasta.set("")
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Dorowet=StringVar()
Pizza=StringVar()
Salad=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Pasta=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblDorowet= Label(f1, font=('arial', 16, 'bold'),text="Dorowet",bd=16,anchor="w")
lblDorowet.grid(row=1, column=0)
txtDorowet=Entry(f1, font=('arial',16,'bold'),textvariable=Dorowet,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDorowet.grid(row=1,column=1)


lblPizza= Label(f1, font=('arial', 16, 'bold'),text="Pizza",bd=16,anchor="w")
lblPizza.grid(row=2, column=0)
txtPizza=Entry(f1, font=('arial',16,'bold'),textvariable=Pizza,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPizza.grid(row=2,column=1)


lblSalad= Label(f1, font=('arial', 16, 'bold'),text="Salad",bd=16,anchor="w")
lblSalad.grid(row=3, column=0)
txtSalad=Entry(f1, font=('arial',16,'bold'),textvariable=Salad,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSalad.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=1)

lblPasta= Label(f1, font=('arial', 16, 'bold'),text="Pasta",bd=16,anchor="w")
lblPasta.grid(row=5, column=0)
txtPasta=Entry(f1, font=('arial',16,'bold'),textvariable=Pasta,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPasta.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)
#=============================calculator===========================
txtDisplay = Entry(f2 , font=('arial' , 25, 'bold') , textvariable = text_Input , bd=10 , insertwidth = 8,
                bg="powder blue",justify='left')
txtDisplay.grid(columnspan=30)
btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7" ,bg="powder blue" , command=lambda: btnClick(7)).grid(row=2,column=0)
btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8" ,bg="powder blue" , command=lambda: btnClick(8)).grid(row=2,column=1)
btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9" ,bg="powder blue" , command=lambda: btnClick(9)).grid(row=2,column=2)
Addition = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+" ,bg="powder blue" , command=lambda: btnClick("+")).grid(row=2,column=3)
#-----------------------------------------------------------------
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4" ,bg="powder blue" , command=lambda: btnClick(4)).grid(row=3,column=0)
btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5" ,bg="powder blue" , command=lambda: btnClick(5)).grid(row=3,column=1)
btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6" ,bg="powder blue" , command=lambda: btnClick(6)).grid(row=3,column=2)
Subtraction = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-" ,bg="powder blue" , command=lambda: btnClick("-")).grid(row=3,column=3)

#----------------------------------------------------------------------
btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1" ,bg="powder blue" , command=lambda: btnClick(1)).grid(row=4,column=0)
btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2" ,bg="powder blue" , command=lambda: btnClick(2)).grid(row=4,column=1)
btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3" ,bg="powder blue" , command=lambda: btnClick(3)).grid(row=4,column=2)
Multiply = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="x" ,bg="powder blue" , command=lambda: btnClick("*")).grid(row=4,column=3)

#----------------------------------------------------------------------
btn0 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0" ,bg="powder blue" , command=lambda: btnClick(1)).grid(row=5,column=0)
btnEquals = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=" ,bg="powder blue", command=btnEqualsInput).grid(row=5,column=1)
btnClear= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C" ,bg="powder blue" , command=btnClearDisplay).grid(row=5,column=2)
Division = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/" ,bg="powder blue" , command=lambda: btnClick("*")).grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


root.mainloop()


