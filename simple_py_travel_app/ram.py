from tkinter import*
import mysql.connector
import tkinter.messagebox as tm
def starting_page():
    global starting_screen
    starting_screen=Tk()
    starting_screen.title("First_window")
    starting_screen.geometry("400x250")
    label_0=Label(starting_screen,text="SELVARAJ TRAVELS",width=50,font=('bold',18),bg="skyblue",fg="white").pack()
    btn1=Button(starting_screen,text="Register",fg="black",font=('bold',15),activebackground="white",command=register)
    btn1.pack(side=LEFT)
    btn2=Button(starting_screen,text="Login",fg="black",font=('bold',15),activebackground="white",command=login_page)
    btn2.pack(side=RIGHT)
def register():
    global register_screen
    register_screen=Toplevel(starting_screen)
    register_screen.title("REGISTER")
    register_screen.geometry("500x500")
    label_0=Label(register_screen,text="PASSENGER DETAILS",width=50,font=('bold',15),bg="skyblue",fg="white").pack()
    global Name
    global Contact_no
    global Aadhaar_no
    global City
    global Age
    global Gender
    global Address
    global password  
    Name=StringVar()
    Contact_no=StringVar()
    Aadhaar_no=StringVar()
    City=StringVar()
    Age=StringVar()
    Gender=StringVar()
    Address=StringVar()
    password=StringVar()
    LName=Label(register_screen,text="Name").place(x=30,y=50)
    LContact_no=Label(register_screen,text="Contact_no").place(x=30,y=100)
    LAadhaar_no=Label(register_screen,text="Aadhaar_no").place(x=30,y=150)
    LCity=Label(register_screen,text="City").place(x=30,y=200)
    LAge=Label(register_screen,text="Age").place(x=30,y=250)
    LGender=Label(register_screen,text="Gender").place(x=30,y=300)
    Radiobutton(register_screen,text="Male",padx=5,variable=Gender,value="male").place(x=100,y=300)
    Radiobutton(register_screen,text="Female",padx=5,variable=Gender,value="female").place(x=170,y=300)
    LAddress=Label(register_screen,text="Address").place(x=30,y=350)
    Lpassword=Label(register_screen,text="password").place(x=30,y=400)
    e1=Entry(register_screen,width=20,textvariable=Name).place(x=100,y=50)
    e2=Entry(register_screen,width=20,textvariable=Contact_no).place(x=100,y=100)
    e3=Entry(register_screen,width=20,textvariable=Aadhaar_no).place(x=100,y=150)
    e4=Entry(register_screen,width=20,textvariable=City).place(x=100,y=200)
    e5=Entry(register_screen,width=20,textvariable=Age).place(x=100,y=250)
    e7=Entry(register_screen,width=20,textvariable=Address).place(x=100,y=350)
    e7=Entry(register_screen,width=20,textvariable=password).place(x=100,y=400)
    sbmitbtn=Button(register_screen,text="Submit",activebackground="black",activeforeground="white",command=register_details).place(x=30,y=450)
def register_details():
    a=Name.get()
    b=Contact_no.get()
    c=Aadhaar_no.get()
    d=City.get()
    e=Age.get()
    f=Gender.get()
    g=Address.get()
    h=password.get()
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="",
    database='ram_ticket_booking'
    )
    mycursor=mydb.cursor()
    sql='INSERT INTO register(name,contact_no,Aadhaar_no,city,age,gender,address,password)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    val=(a,b,c,d,e,f,g,h)
    try:
        mycursor.execute(sql,val)
        mydb.commit()
        tm.showinfo("Success","Registration Success")
        starting_page()
    except:
        mydb.rollback()
    finally:
        mycursor.close()
        mydb.close()
def login_page():
    
    global Login_screen
    Login_screen=Toplevel(starting_screen)
    Login_screen.title("Login")
    Login_screen.geometry("400x250")
    global username_verify
    global password_verify
    username_verify=StringVar()
    password_verify=StringVar()
    label_0=Label(Login_screen,text="LOGIN",width=50,font=('bold',18),bg="skyblue",fg="white").pack()
    uname=Label(Login_screen,text="Username").place(x=30,y=50)
    password=Label(Login_screen,text="Password").place(x=30,y=90)
    e1=Entry(Login_screen,width=20,textvariable=username_verify).place(x=100,y=50)
    e2=Entry(Login_screen,width=20,textvariable=password_verify).place(x=100,y=90)
    sbmitbtn=Button(Login_screen,text="Submit",activebackground="White",activeforeground="black",command=Login).place(x=30,y=120)
    Login_screen.mainloop()
def Login():
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd="",
        database='ram_ticket_booking'
        )
    mycursor=mydb.cursor()
    if  username_verify.get()==""or password_verify.get()=="":
        tm.showerror("Error","please complete the required fields")
    else:
        mycursor.execute('select*FROM register WHERE name=%s AND password=%s',(username_verify.get(),password_verify.get()))
        if mycursor.fetchone():
            select_place()
            mycursor.close()
            mydb.close()
        else:
            user_not_found()
def user_not_found():
    tm.showerror("Error","Enter a invalid Username and password")
def select_place():
    global  select_place_screen
    select_place_screen=Toplevel(Login_screen)
    select_place_screen.geometry("400x400")
    select_place_screen.title("Journey details")
    select_place_screen.config(bg='grey')
    label_0=Label(select_place_screen,text="SELECT YOUR JOURNEY",width=50,font=('bold',15),bg="skyblue",fg="white").pack()
    options_list = ["Chennai", "Madurai", "Dindigul","sivaganga","salem","erode", "Coimbatore","Bangalore","delhi","kerala","kochi","trichy","sivakasi"]
    options_list2=["Madurai","dindigul","bangalore","kodaikanal","salem","sivaganga","erode","hyderabad","delhi","kerala","kochi","trichy","sivakasi"]
    From= StringVar()
    From.set("From")
    To=StringVar()
    To.set("To")
    OptionMenu1= OptionMenu(select_place_screen, From, *options_list)
    OptionMenu1.config(font=('bold',10),width='8')
    OptionMenu1.place(x=50,y=60)
    OptionMenu2=OptionMenu(select_place_screen, To, *options_list2)
    OptionMenu2.config(font=('bold',10),width='8')
    OptionMenu2.place(x=250,y=60)
    def print_answers():
        global from_place,to_place
        from_place=From.get()
        to_place=To.get()
        update_place()
    btn= Button(select_place_screen, text='Submit', command=print_answers).pack(side=BOTTOM)
    select_place_screen.mainloop()
def update_place():
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd="",
        database='ram_ticket_booking'
        )
    mycursor=mydb.cursor()
    a1="UPDATE register SET departure=%s,destination=%s WHERE name=%s"
    b1=(from_place,to_place,username_verify.get())
    mycursor.execute(a1,b1)
    mydb.commit()
    seat_selection()
def seat_selection():
    global top
    top=Toplevel(select_place_screen)
    global s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24
    global s25,s26,s27,s28,s29,s30
    s1=IntVar()
    s2=IntVar()
    s3=IntVar()
    s4=IntVar()
    s5=IntVar()
    s6=IntVar()
    s7=IntVar()
    s8=IntVar()
    s9=IntVar()
    s10=IntVar()
    s11=IntVar()
    s12=IntVar()
    s13=IntVar()
    s14=IntVar()
    s15=IntVar()
    s16=IntVar()
    s17=IntVar()
    s18=IntVar()
    s19=IntVar()
    s20=IntVar()
    s21=IntVar()
    s22=IntVar()
    s23=IntVar()
    s24=IntVar()
    s25=IntVar()
    s26=IntVar()
    s27=IntVar()
    s28=IntVar()
    s29=IntVar()
    s30=IntVar()
    top.geometry("350x350")
    top.title("seat selection")
    label_0=Label(top,text="SELECT YOUR SEATS",width=50,font=('bold',15),bg="skyblue",fg="white").pack()
    c1=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s1).place(x=50,y=50)
    c2=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s2).place(x=80,y=50)
    c3=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s3).place(x=110,y=50)
    c4=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s4).place(x=50,y=80)
    c5=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s5).place(x=80,y=80)
    c6=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s6).place(x=110,y=80)
    c7=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s7).place(x=50,y=110)
    c8=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s8).place(x=80,y=110)
    c9=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s9).place(x=110,y=110)
    c10=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s10).place(x=50,y=140)
    c11=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s11).place(x=80,y=140)
    c12=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s12).place(x=110,y=140)
    c13=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s13).place(x=50,y=170)
    c14=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s14).place(x=80,y=170)
    c15=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s15).place(x=110,y=170)
    c16=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s16).place(x=50,y=200)
    c17=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s17).place(x=80,y=200)
    c18=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s18).place(x=110,y=200)
    c19=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s19).place(x=240,y=50)
    c20=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s20).place(x=270,y=50)
    c21=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s21).place(x=240,y=80)
    c22=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s22).place(x=270,y=80)
    c23=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s23).place(x=240,y=110)
    c24=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s24).place(x=270,y=110)
    c25=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s25).place(x=240,y=140)
    c26=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s26).place(x=270,y=140)
    c27=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s27).place(x=240,y=170)
    c28=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s28).place(x=270,y=170)
    c29=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s29).place(x=240,y=200)
    c30=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=s30).place(x=270,y=200)
    Button(top,text="Submit",width=20,bg='white',fg='black',command=seat_confirmation).place(x=100,y=270)
    label=Label(top,text="A").place(x=10,y=58)
    label=Label(top,text="B").place(x=10,y=90)
    label=Label(top,text="C").place(x=10,y=120)
    label=Label(top,text="D").place(x=10,y=150)
    label=Label(top,text="E").place(x=10,y=180)
    label=Label(top,text="F").place(x=10,y=210)
    label=Label(top,text="1").place(x=50,y=30)
    label=Label(top,text="2").place(x=80,y=30)
    label=Label(top,text="3").place(x=110,y=30)
    label=Label(top,text="4").place(x=245,y=30)
    label=Label(top,text="5").place(x=275,y=30)
    top.mainloop()
def seat_confirmation():
    global seat_name,Amount
    seat_name=""
    Amount=0
    if (s1.get()==1):
        seat_name+="A1, "
        Amount+=599
    if (s2.get()==1):
        seat_name+="A2, "
        Amount+=599
    if (s3.get()==1):
        seat_name+="A3, "
        Amount+=599
    if (s4.get()==1):
        seat_name+="B1, "
        Amount+=599
    if (s5.get()==1):
        seat_name+="B2, "
        Amount+=599
    if (s6.get()==1):
        seat_name+="B3, "
        Amount+=599
    if (s7.get()==1):
        seat_name+="C1, "
        Amount+=599
    if (s8.get()==1):
        seat_name+="C2, "
        Amount+=599
    if (s9.get()==1):
        seat_name+="C3, "
        Amount+=599
    if (s10.get()==1):
        seat_name+="D1, "
        Amount+=599
    if (s11.get()==1):
        seat_name+="D2, "
        Amount+=599
    if (s12.get()==1):
        seat_name+="D3, "
        Amount+=599
    if (s13.get()==1):
        seat_name+="E1, "
        Amount+=599
    if (s14.get()==1):
        seat_name+="E2, "
        Amount+=599
    if (s15.get()==1):
        seat_name+="E3, "
        Amount+=599
    if (s16.get()==1):
        seat_name+="F1, "
        Amount+=599
    if (s17.get()==1):
        seat_name+="F2, "
        Amount+=599
    if (s18.get()==1):
        seat_name+="F3, "
        Amount+=599
    if (s19.get()==1):
        seat_name+="A4, "
        Amount+=599
    if (s20.get()==1):
        seat_name+="A5, "
        Amount+=599
    if (s21.get()==1):
        seat_name+="B4, "
        Amount+=599
    if (s22.get()==1):
        seat_name+="B5, "
        Amount+=599
    if (s23.get()==1):
        seat_name+="C4, "
        Amount+=599
    if (s24.get()==1):
        seat_name+="C5, "
        Amount+=599
    if (s25.get()==1):
        seat_name+="D4, "
        Amount+=599
    if (s26.get()==1):
        seat_name+="D5, "
        Amount+=599
    if (s27.get()==1):
        seat_name+="E4, "
        Amount+=599
    if (s28.get()==1):
        seat_name+="E5, "
        Amount+=599
    if (s29.get()==1):
        seat_name+="F4, "
        Amount+=599
    if (s30.get()==1):
        seat_name+="F5, "
        Amount+=599
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd="",
        database='ram_ticket_booking'
        )
    mycursor=mydb.cursor()
    a1="UPDATE register SET seat_no=%s,Ticket_price=%s WHERE name=%s"
    b1=(seat_name,Amount,username_verify.get())
    mycursor.execute(a1,b1)
    mydb.commit()
    fetch_details()
def fetch_details():
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd="",
        database='ram_ticket_booking'
        )
    mycursor=mydb.cursor()
    a3='select name,contact_no,gender FROM register WHERE name=%s'
    a4=(username_verify.get(),)
    try:
        mycursor.execute(a3,a4)
        for a1 in mycursor:
                for a2 in range(len(a1)):
                    print(a1[a2])
        global b1,c1,d1
        b1=a1[0]
        c1=a1[1]
        d1=a1[2]
        print(b1,c1,d1)
    except:
        mydb.rollback()
    final_details()
def final_details():
    global final_details_screen
    final_details_screen=Toplevel(top)
    final_details_screen.title("CHECKOUT DETAILS")
    final_details_screen.geometry("500x500")
    label_0=Label(final_details_screen,text="CHECKOUT DETAILS",width=50,font=('bold',15),bg="orange",fg="white").pack()
    Name=Label(final_details_screen,text="Name:").place(x=30,y=50)
    Contact_no=Label(final_details_screen,text="Contact_no:").place(x=30,y=100)
    Seat_no=Label(final_details_screen,text="Seat_no:").place(x=30,y=150)
    From=Label(final_details_screen,text="Departure:").place(x=30,y=200)
    Destiny=Label(final_details_screen,text="Destination:").place(x=30,y=250)
    Gender=Label(final_details_screen,text="Gender:").place(x=30,y=300)
    Ticket_amount=Label(final_details_screen,text="Ticket_price:").place(x=30,y=350)
    e1=Label(final_details_screen,width=20,text=b1).place(x=120,y=50)
    e2=Label(final_details_screen,width=20,text=c1).place(x=120,y=100)
    e3=Label(final_details_screen,width=20,text=seat_name).place(x=120,y=150)
    e4=Label(final_details_screen,width=20,text=from_place).place(x=120,y=200)
    e5=Label(final_details_screen,width=20,text=to_place).place(x=120,y=250)
    e6=Label(final_details_screen,width=20,text=d1).place(x=120,y=300)
    e7=Label(final_details_screen,width=20,text=Amount).place(x=120,y=350)
    sbmitbtn=Button(final_details_screen,text="Submit",activebackground="black",activeforeground="white",command=ticket_booked).place(x=30,y=400)
def ticket_booked():
    tm.showinfo("confirmed","ticket booked successfully")
starting_page()
