#video 1:5-1:16 minutes and line no 272 - 293 link 374 and 378
#612,512,510 stops diffrents  / and 611,513,514,515 that are used to hold "student mangment system"
def addstudent():
    def Submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d:%m:%y")
        try:
            #####insert query for insert data in mysql"query is strr"
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()   #### it used for data update in mysql for secure not show error
            res = messagebox.askyesnocancel('Notification',
                                            'id{} name{} added sucessfully..want to clean the form'.format(id,name),
                                            parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notification', 'Id already exist try another Id..', parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(* studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
#########################################that used to create  "connect to database 'add' " phase
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('student management system')
    addroot.config(bg='Slate Gray')
    addroot.iconbitmap('man.ico')
    addroot.resizable(False, False)
###########################################add student label that means button like "enter id" etc in welcome section
    idLabel = Label(addroot, text='Enter Id:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idLabel.place(x=10, y=10)

    nameLabel = Label(addroot, text='Enter Name:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    nameLabel.place(x=10, y=70)

    mobileLabel = Label(addroot, text='Enter Mobile:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobileLabel.place(x=10, y=130)

    emailLabel = Label(addroot, text='Enter Email:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emailLabel.place(x=10, y=190)

    addressLabel = Label(addroot, text='Enter Address:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addressLabel.place(x=10, y=250)

    genderLabel = Label(addroot, text='Enter Gender:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderLabel.place(x=10, y=310)

    dobLabel = Label(addroot, text='Enter D.O.B:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    dobLabel.place(x=10, y=370)

###########################################add student entry that write user
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
###################################### submit button in welcome section
    submitbtn = Button(addroot, text='submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='Dim Gray',
                   activeforeground='white',
                   bg='khaki', command=Submitadd)
    submitbtn.place(x=150, y=420)
    addroot.mainloop()

def searchstudent():
    def Submitsearch():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d:%m:%y")
        if(id != ''):
            strr = 'select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # it used search new data and previous delete
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # it used search new data and previous delete
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(email != ''):
            strr = 'select *from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # it used search new data and previous delete
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(address != ''):
            strr = 'select *from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # it used search new data and previous delete
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(gender != ''):
            strr = 'select *from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # it used search new data and previous delete
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(dob != ''):
            strr = 'select *from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # it used search new data and previous delete
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(addeddate != ''):
            strr = 'select *from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) # it used search new data and previous delete
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
#########################################that used to create  "connect to database 'search' " phase
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('student management system')
    searchroot.config(bg='Slate Gray')
    searchroot.iconbitmap('man.ico')
    searchroot.resizable(False, False)
###########################################add student label that means button like "enter id" etc in welcome section
    idLabel = Label(searchroot, text='Enter Id:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                width=12, anchor='w')
    idLabel.place(x=10, y=10)

    nameLabel = Label(searchroot, text='Enter Name:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                  borderwidth=3, width=12, anchor='w')
    nameLabel.place(x=10, y=60)

    mobileLabel = Label(searchroot, text='Enter Mobile:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    mobileLabel.place(x=10, y=120)

    emailLabel = Label(searchroot, text='Enter Email:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    emailLabel.place(x=10, y=180)

    addressLabel = Label(searchroot, text='Enter Address:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    addressLabel.place(x=10, y=240)

    genderLabel = Label(searchroot, text='Enter Gender:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    genderLabel.place(x=10, y=300)

    dobLabel = Label(searchroot, text='Enter D.O.B:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                 borderwidth=3, width=12, anchor='w')
    dobLabel.place(x=10, y=360)

    dateLabel = Label(searchroot, text='Enter Date:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                  borderwidth=3, width=12, anchor='w')
    dateLabel.place(x=10, y=420)
###########################################add student entry that write user
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
###################################### submit button in welcome section
    submitbtn = Button(searchroot, text='submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='Dim Gray',
                   activeforeground='white',
                   bg='khaki', command=Submitsearch)
    submitbtn.place(x=150, y=480)
    searchroot.mainloop()

def deletestudent():
    cc = studenttable.focus()        #data delete hoga as pr "focus" kr vey ga
    content = studenttable.item(cc)
    pp = content['values'][0]        #data delete bcz indexs so every id unique
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo('Notification', 'Id deleted sucessfully ...'.format(pp))

    strr = 'select * from studentdata1'   # as line sy 7 line tk data jb delette hoga as time show hu jye ga
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = timeval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,time=%s,date=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, time, date, id))
        con.commit()            # used for update data in database
        messagebox.showinfo('Notification', 'id {} modified sucessfully...'.format(id),parents=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

#########################################that used to create  "connect to database 'update' " phase
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x540+220+200')
    updateroot.title('student management system')
    updateroot.config(bg='Slate Gray')
    updateroot.iconbitmap('man.ico')
    updateroot.resizable(False, False)
###########################################add student label that means button like "enter id" etc in welcome section
    idLabel = Label(updateroot, text='Enter Id:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idLabel.place(x=10, y=10)

    nameLabel = Label(updateroot, text='Enter Name:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    nameLabel.place(x=10, y=60)

    mobileLabel = Label(updateroot, text='Enter Mobile:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobileLabel.place(x=10, y=120)

    emailLabel = Label(updateroot, text='Enter Email:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emailLabel.place(x=10, y=180)

    addressLabel = Label(updateroot, text='Enter Address:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addressLabel.place(x=10, y=240)

    genderLabel = Label(updateroot, text='Enter Gender:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderLabel.place(x=10, y=300)

    dobLabel = Label(updateroot, text='Enter D.O.B:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    dobLabel.place(x=10, y=360)

    dateLabel = Label(updateroot, text='Enter Date:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    dateLabel.place(x=10, y=420)

    timeLabel = Label(updateroot, text='Enter Time:', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timeLabel.place(x=10, y=420)
    ###########################################add student entry that write user
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=430)
    ###################################### submit button in welcome section
    submitbtn = Button(updateroot, text='submit', font=('roman', 15, 'bold'), width=20, bd=5,activebackground='Dim Gray',
                       activeforeground='white',bg='khaki', command=update)
    submitbtn.place(x=150, y=480)

    cc = studenttable.focus()        # it used for update data (as line sy 13-no line tk)
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def exportstudent():
    ff = filedialog.asksaveasfilename() #ope file directly
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)  #"i" means get every children data
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(
            pp[4]), gender.append(pp[5]),                              # append means include everyone
        dob.append(pp[6]), addeddate.append(pp[7]), addedtime.append(pp[8])
    dd = ['id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'AddedDate', 'AddedTime']
    df = pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob,
                    addeddate, addedtime)), columns=dd)  #insert export values
    paths = r'{}.csv'.format(ff)      #"r" make readable
    df.to_csv(paths, index=False)    #it used for saves data filein csv folder index false when show autoindex genrate
    messagebox.showinfo('Notification', 'student data is saved{}'.format(paths))

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit ?')
    if(res == True):
        root.destroy()
#########################################connection of database
def connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordentry.get()
        host = 'localhost'
        user = 'root'
        password = 'saim51214'
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again')
            return
        try:
            strr = 'create database studentmangmentsystem1'
            mycursor.execute(strr)
            strr = ' use studentmangmentsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(15),mobile varchar(15),email varchar(15),address varchar(50),gender varchar(15),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'database created and Now you are connected to the database----',
                                parent=dbroot)
        except:
            strr = 'use studentmangmentsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'Now you are connected to the database----', parent=dbroot)
            dbroot.destroy()
            
    dbroot = Toplevel()
    dbroot.grab_set() # if first cross then start next activity
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('man.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='SlateGray')

#######################################connect dbLabel
    hostlabel = Label(dbroot,text='Enter Host :',bg='Gray',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text='Enter User :', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text='Enter Password :', bg='Gray', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    passwordlabel.place(x=10, y=130)
#######################################connectdb entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable= hostval)
    hostentry.place(x=250,y=10)
    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    hostentry.place(x=250, y=70)
    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)
########################################connectdb button(submit)
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='khaki',bd=4,width=20,
                          activebackground='DimGray',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()

######################
def tick():
    time_string = time.strftime("%H,%M,%S")
    date_string = time.strftime("%d/,%m/,%y")
    clock.config(text='Date :'+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)
##############################intro slider diff color
import random
#colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    #  fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)
def IntroLabelTick():
    global count,text
    if (count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)    #speed of the word

from tkinter import *
from tkinter import Toplevel,messagebox,filedialog     #filedialog used for save file before open
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title("student management system")
root.config(bg='gray')
root.geometry('1174x700+200+50')
root.iconbitmap('man.ico')
root.resizable(True,True)   #that are used to big page

#################################1st frame lift
DataEntryFrame = Frame(root,bg='gray',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
###############################################################data entry frame (welcome)
frontlabel = Label(DataEntryFrame,text='------------WELCOME------------',width=30,font=('arial',22,'italic bold'),bg='gray')
frontlabel.pack(side=TOP,expand=True)

###################################################buttons create in data entry frame
addbtn = Button(DataEntryFrame, text='1.  Add Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                activebackground='DimGray', relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP, expand=True)
searchbtn = Button(DataEntryFrame, text='2.  Search Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='DimGray', relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP, expand=True)
deletebtn = Button(DataEntryFrame, text='3.  Delete Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='DimGray', relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP, expand=True)
updatebtn = Button(DataEntryFrame, text='4.  Update Student', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='DimGray', relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP, expand=True)
sallbtn = Button(DataEntryFrame, text='5.  Show All', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                 activebackground='DimGray', relief=RIDGE,activeforeground='white',command=showstudent)
sallbtn.pack(side=TOP, expand=True)
exportbtn = Button(DataEntryFrame, text='6.  Export data', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                   activebackground='DimGray', relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP, expand=True)
exitbtn = Button(DataEntryFrame, text='7.  Exit', width=25, font=('Roboto', 20, 'bold'), bd=6, bg='khaki',
                 activebackground='DimGray', relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP, expand=True)
###################################2nd frame right
ShowEntryFrame = Frame(root,bg='gray',relief=GROOVE,borderwidth=5)
ShowEntryFrame.place(x=550,y=80,width=620,height=600)
########################################################(ShowEntryFrame-result)
style = ttk.Style()
style.configure('Treeview.Heading', font=('Roboto', 18, 'bold'), foreground='black')
style.configure('Treeview', font=('times', 17, 'bold'), foreground='black',bg='Slate Gray')
scroll_x = Scrollbar(ShowEntryFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowEntryFrame, orient=VERTICAL)
studenttable = Treeview(ShowEntryFrame, columns=('Id', 'Name', 'Mobile no', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile no', text='Mobile no')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id', width=100)
studenttable.column('Name', width=170)
studenttable.column('Mobile no', width=200)
studenttable.column('Email', width=170)
studenttable.column('Address', width=170)
studenttable.column('Gender', width=130)
studenttable.column('D.O.B', width=130)
studenttable.column('Added Date', width=180)
studenttable.column('Added Time', width=180)
studenttable.pack(fill=BOTH,expand=1)
#########################slider-show(ss)
ss = " Welcome to student management system "
count = 0
text = ''
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='SlateGray')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
#IntroLabelColorTick()
#################################################clock
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='SlateGray')
clock.place(x=0,y=0)
tick()
############################################################connectdatabase button
Grid.columnconfigure(root, 0, weight=200) 
connectbutton = Button(root,text='Connect to Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bd=6,bg='SlateGray',
                       activebackground='DimGray',activeforeground='white',command=connectdb)
connectbutton.grid(row=0, column=0, sticky="e")
#connectbutton.place(x=930,y=0)
root.mainloop()