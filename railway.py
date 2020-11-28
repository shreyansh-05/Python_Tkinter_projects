import tkinter as tk
from tkinter import ttk
import random
import datetime
from tkinter.font import Font
from tkinter import messagebox
class Railways(tk.Frame):
    Accounts={}
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.Usertext=tk.Label(text="USERNAME")
        self.Usertext.grid(row=1,column=0,padx=10,pady=10,columnspan=2)
        self.username=tk.Entry()
        self.username.grid(row=1,column=2)
        self.Passtext=tk.Label(text="PASSWORD")
        self.Passtext.grid(row=2,column=0,padx=10,pady=10,columnspan=2)
        self.password=tk.Entry(show="*")
        self.password.grid(row=2,column=2)
        self.enter=tk.Button(text="LOGIN",font=("Comic Sans",26),command=self.AccessAcc)
        self.enter.grid(row=3,column=0,padx=1,pady=1)
        self.exit=tk.Button(text="QUIT",command=root.quit,font=("Calibri",26))
        self.exit.grid(row=3,column=1,padx=1,pady=1)
        self.createAcc=tk.Button(text="CREATE ACCOUNT",font=("Calibri",26),command=self.Create)
        self.createAcc.grid(row=4,column=0,padx=1,pady=1,columnspan=2)
        
    def AccessAcc(self):
        self.e1=self.username.get()
        self.e2=self.password.get()
        if (self.e1 in Railways.Accounts):
            if (Railways.Accounts[self.e1]["Password"]==self.e2):
                self.Trans=tk.Toplevel(self)
                self.MainWin()
            else:
                    messagebox.showerror("Error", message="are galat hai")
        else:
                messagebox.showerror("Error", message="Khali thodi hota hai bhai")
    def MainWin(self):
        self.Transf=tk.Frame(self.Trans)
        self.Transf.grid()
        self.Trans.geometry("800x700")
        self.Welco=tk.Label(self.Transf,text=("WELCOME "+str(self.Uname).upper()+"!"),font="Courier 50",fg="blue")
        self.Welco.grid(row=0,column=0)
        self.now = datetime.datetime.now()
        self.date=tk.Label(self.Transf,text=("Date:"+str(self.now.day)+"/"+str(self.now.month)+"/"+str(self.now.year)),font="Ariel 20")
        self.date.grid(row=3,column=0)
        self.Time=tk.Label(self.Transf,font="Ariel 20")
        self.Time.grid(row=4,column=0)
        self.Plan=tk.Button(self.Transf,text="Plan My Ticket",command=self.PlanTicket)
        self.Plan.grid(row=5,column=0)
        self.Oth=tk.Button(self.Transf,text="Others",command=self.OthScr)
        self.Oth.grid(row=8,column=0)
        self.Logout=tk.Button(self.Transf,text="Logout", command=self.Trans.destroy)
        self.Logout.grid(row=9,column=3,padx=10,pady=10)
        self.clock()
        
    def clock(self):
        self.time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        self.Time.config(text=self.time)
        self.Transf.after(1000, self.clock)   
    def PlanTicket(self):
        self.Transf.destroy()
        self.PlanWin=tk.Frame(self.Trans)
        self.PlanWin.grid()
        self.Plan=tk.Label(self.PlanWin,text='Plan My Ticket', font="Ariel 20")
        self.Plan.grid(row=0,column=0)
        self.From=tk.Label(self.PlanWin,text="FROM")
        self.From.grid(row=1,column=0)
        self.Usfrom=tk.StringVar()
        self.Ufrom=tk.Entry(self.PlanWin,textvariable=self.Usfrom)
        self.Ufrom.grid(row=1,column=1)
        self.To=tk.Label(self.PlanWin,text="TO")
        self.To.grid(row=2,column=0)
        self.Usto=tk.StringVar()
        self.Uto=tk.Entry(self.PlanWin,textvariable=self.Usto)
        self.Uto.grid(row=2,column=1)
        self.Date=tk.Label(self.PlanWin,text="DATE")
        self.Date.grid(row=3,column=0)
        self.Day=tk.StringVar()
        self.Month=tk.StringVar()
        self.Year=tk.StringVar()
        self.Daybox=ttk.Combobox(self.PlanWin,textvariable=self.Day)
        self.Daybox['values']=('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        self.Daybox.grid(row=3,column=1)
        self.Monthbox=ttk.Combobox(self.PlanWin,textvariable=self.Month)
        self.Monthbox['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
        self.Monthbox.grid(row=3,column=2)
        self.Yearbox=ttk.Combobox(self.PlanWin,textvariable=self.Year)
        self.Yearbox['values']=('2017','2018')
        self.Yearbox.grid(row=3,column=3)
        self.quota=tk.IntVar()
        self.q=tk.Label(self.PlanWin,text="Quota")
        self.q.grid(row=4,column=0)
        self.q1=tk.Radiobutton(self.PlanWin,text="General",variable=self.quota,value=1,state='active')
        self.q2=tk.Radiobutton(self.PlanWin,text="Tatkal",variable=self.quota,value=2)
        self.q1.grid(row=4,column=1)
        self.q2.grid(row=4,column=2)
        self.Tname=tk.Label(self.PlanWin,text="Train Name")
        self.Tname.grid(row=5,column=0)
        self.Trname=tk.StringVar()
        self.Train=tk.Entry(self.PlanWin,textvariable=self.Trname)
        self.Train.grid(row=5,column=1)
        self.ctype=tk.IntVar()
        self.c=tk.Label(self.PlanWin,text="Coach Type:")
        self.c.grid(row=6,column=0)
        self.c1=tk.Radiobutton(self.PlanWin,text="General",variable=self.ctype,value=1)
        self.c2=tk.Radiobutton(self.PlanWin,text="Sleeper Class",variable=self.ctype,value=2)
        self.c3=tk.Radiobutton(self.PlanWin,text="AC 1 Tier",variable=self.ctype,value=3)
        self.c4=tk.Radiobutton(self.PlanWin,text="AC 2 Tier",variable=self.ctype,value=4)
        self.c5=tk.Radiobutton(self.PlanWin,text="AC 3 Tier",variable=self.ctype,value=5)
        self.c1.grid(row=6,column=1)
        self.c2.grid(row=6,column=2)
        self.c3.grid(row=6,column=3)
        self.c4.grid(row=6,column=4)
        self.c5.grid(row=6,column=5)
        self.km=tk.Label(self.PlanWin,text="Number of Kilometres")
        self.km.grid(row=7,column=0)
        self.kiloms=tk.IntVar()
        self.kilo=tk.Entry(self.PlanWin,textvariable=self.kiloms)
        self.kilo.grid(row=7,column=1)
        self.people=tk.Label(self.PlanWin,text="Number of People")
        self.people.grid(row=8,column=0)
        self.peoples=tk.IntVar()
        self.npeople=tk.Entry(self.PlanWin,textvariable=self.peoples)
        self.npeople.grid(row=8,column=1)
        self.CFare=tk.Button(self.PlanWin,text="Calculate Fare",command=self.Fare)
        self.CFare.grid(row=9,column=0)
        self.Canc=tk.Button(self.PlanWin,text="Cancel",command=self.Combine6)
        self.Canc.grid(row=10,column=0)
    def Combine6(self):
        self.PlanWin.destroy()
        self.MainWin()
    def Fare(self):
        self.fare=0.0
        if (self.kiloms.get()==0):
            messagebox.showerror("Error", message="Kilometres Field Cannot be empty",parent=self.PlanWin)
        elif (self.peoples.get()==0):
            messagebox.showerror("Error", message="Number of People Field Cannot be empty",parent=self.PlanWin)
        else:
            self.Calculate()
    def Calculate(self):
        self.coach=self.ctype.get()
        self.kms=self.kiloms.get()
        if self.coach==1:
            self.fare=self.kms*10
        elif self.coach==2:
            self.fare=self.kms*14
        elif self.coach==3:
            self.fare=self.kms*16
        elif self.coach==4:
            self.fare=self.kms*22
        else:
            self.fare=self.kms*26
        self.fare=self.fare*int(self.peoples.get())
        self.TicketMake()
    def TicketMake(self):
        self.PlanWin.destroy()
        self.TickWin=tk.Frame(self.Trans)
        self.TickWin.grid()
        self.Passengers=list()
        self.Passhead=tk.Label(self.TickWin,text="Passenger Information",font=("Calibri 40"))
        self.Passhead.grid(row=0,column=0,columnspan=10)
        self.Passcol=tk.Label(self.TickWin,text=" S.No    \t        Name \t \t     Age \t \t            Berth Preference")
        self.Passcol.grid(row=1,column=0,columnspan=4,sticky='W')
        self.TotalPeople=self.peoples.get()
        self.Pname=[0]*self.TotalPeople
        self.Page=[0]*self.TotalPeople
        self.Pseat=[0]*self.TotalPeople
        self.Psno=[0]*self.TotalPeople
        self.Passseat=[0]*self.TotalPeople
        self.Currpass=0
        for i in range(self.TotalPeople):
            self.Pname[i]=tk.StringVar()
            self.Page[i]=tk.StringVar()
            self.Pseat[i]=tk.StringVar()
            self.Psno[i]=tk.Label(self.TickWin,text=str(i+1)+".")
            self.Psno[i].grid(row=i+2,column=0)
            self.Passname=tk.Entry(self.TickWin,textvariable=self.Pname[i])
            self.Passage=tk.Entry(self.TickWin,textvariable=self.Page[i])
            self.Passseat[i]=ttk.Combobox(self.TickWin,textvariable=self.Pseat[i],state="readonly")
            self.Passseat[i].bind("<<ComboboxSelected>>",self.princombo)
            self.Passseat[i]["values"]=("Lower","Upper","Middle","Side Upper","Side Lower")
            self.Passname.grid(row=i+2,column=1,padx=1,pady=3,sticky='W')
            self.Passage.grid(row=i+2,column=2,padx=1,pady=3,sticky='W')
            self.Passseat[i].grid(row=i+2,column=3,padx=1,pady=3,sticky='W')
            self.Passsubmit=tk.Button(self.TickWin,text="Submit",command=self.Printing)
            self.Passsubmit.grid(row=self.TotalPeople+3,column=0,columnspan=2,padx=2)
            self.Passcancel=tk.Button(self.TickWin,text="Cancel",command=self.Combine8)
            self.Passcancel.grid(row=self.TotalPeople+3,column=1,columnspan=2,padx=2)
    def princombo(self,event):
        pass
    def Printing(self):
        self.TickWin.destroy()
        self.PrinWin=tk.Frame(self.Trans)
        self.PrinWin.grid()
        self.PHead=tk.Label(self.PrinWin,text="Ticket Summary",font="Ariel 30 bold",justify="center")
        self.PHead.grid(row=0,column=0,columnspan=5)
        self.Quotas=["General","General","Tatkal"]
        self.Coaches=["General","General","Sleeper Class","AC 1 Tier","AC 2 Tier","AC 3 Tier"]
        self.Tdetails=tk.Label(self.PrinWin,text=("""
From: """+self.Usfrom.get()+"""
To: """+self.Usto.get()+"""
Date: """+self.Day.get()+' '+self.Month.get()+" "+self.Year.get()+"""
Quota:"""+self.Quotas[self.quota.get()]+"""
Coach Type :"""+self.Coaches[self.ctype.get()]+"""
Distance: """+str(self.kms)+"km"+"""
Fare: """+str(self.fare)),font="Ariel 20",justify="left")
        self.Tdetails.grid(row=1,column=0,sticky='W')
        self.Plist=tk.Label(self.PrinWin,text="Passengers:",justify="center",font='Ariel 25 bold')
        self.Plist.grid(row=2,column=0,columnspan=5)
        tk.Label(self.PrinWin,text="\t  S.No.  \t Name \t  Age \t Berth Preference",font='Ariel 20').grid(row=3,column=0,columnspan=5)
        for i in range(self.TotalPeople):
            tk.Label(self.PrinWin,text="  "+str(i+1)+".",font='Ariel 20').grid(row=i+4,column=0)
            tk.Label(self.PrinWin,text=self.Pname[i].get()+'\t'+self.Page[i].get()+'\t'+self.Pseat[i].get(),font='Ariel 20').grid(row=i+4,column=1,sticky='w')
        self.Okb=tk.Button(self.PrinWin,text="Ok",command=self.Combination)
        self.Okb.grid(row=10,column=0)
    def Combination(self):
        self.PrinWin.destroy()
        self.MainWin()
    def Combine8(self):
       self.TickWin.destroy()
       self.MainWin()
    def OthScr(self):
        self.Transf.destroy()
        self.Trans.geometry("550x220")
        self.OthFr=tk.Frame(self.Trans)
        self.OthFr.pack()
        self.Alt=tk.Label(self.OthFr,text="ACCOUNT ALTERATION SCREEN",font="Calibri 30",fg="red")
        self.Alt.pack()
        self.AccMod=tk.Button(self.OthFr,text="Account Modification",command=self.Combine3)
        self.AccMod.pack()
        self.ChanPass=tk.Button(self.OthFr,text="Change Password",command=self.ChangePassword)
        self.ChanPass.pack()
        self.ClosAcc=tk.Button(self.OthFr,text="Closing Account",command=self.Closing)
        self.ClosAcc.pack()
        self.back=tk.Button(self.OthFr,text="Go Back",command=self.Goback)
        self.back.pack(anchor="se")
        self.Ext=tk.Button(self.OthFr,text="Exit",command=self.Trans.destroy)
        self.Ext.pack(anchor="se")
    def Closing(self):
        self.closure=messagebox.askyesno("Warning!",message="Are you sure you want to close your account?",parent=self.Trans)
        if self.closure:
            del Railways.Accounts[self.Uname]
            self.Trans.destroy()
        else:
            pass
    def Goback(self):
        self.OthFr.destroy()
        self.MainWin()
    def Combine3(self):
        self.ModAsk=messagebox.askyesno(message="Are you sure you want to modify your account?",parent=self.Trans)
        if self.ModAsk==True:
            self.Trans.destroy()
            self.Create()
        else:
            self.OthFr.destroy()
            self.MainWin()
    def ChangePassword(self):
        self.OthFr.destroy()
        self.Trans.geometry("800x800")
        self.Chaf=tk.Frame(self.Trans)
        self.Chaf.grid()
        self.ChafHead=tk.Label(self.Chaf,text="CHANGE PASSWORD",font="Calibri 30")
        self.ChafHead.grid(row=0,column=0)
        self.ChafMess=tk.Label(self.Chaf,text="Enter New Password")
        self.ChafMess.grid(row=2,column=0,columnspan=2)
        self.ChafNew=tk.Entry(self.Chaf)
        self.ChafNew.grid(row=2,column=2,columnspan=2)
        self.PasChan=tk.Button(self.Chaf,text="CHANGE",command=self.StNewPass)
        self.PasChan.grid(row=3,column=0)
        self.ChanCan=tk.Button(self.Chaf,text="CANCEL",command=self.Combine1)
        self.ChanCan.grid(row=3,column=1)
    def StNewPass(self):
        self.Newpass=self.ChafNew.get()
        Railways.Accounts[self.Uname]["Password"]=self.Newpass
        self.Chaf.destroy()
        self.PasChd=tk.Frame(self.Trans)
        self.PasChd.pack()
        self.PasMess=tk.Label(self.PasChd,text="Password Successfully Changed!")
        self.PasMess.pack()
        self.PasOk=ttk.Button(self.PasChd,text="Ok",command=self.Combine2)
        self.PasOk.pack()
    def Combine1(self):
        self.Chaf.destroy()
        self.MainWin()
    def Combine2(self):
        self.PasChd.destroy()
        self.MainWin()
    def Create(self):
        self.Wind=tk.Toplevel(self)
        self.Wind.title("Create/Modify Account")
        self.Window=tk.Frame(self.Wind)
        self.Window.grid()
        self.Wind.geometry("700x700")
        self.id=tk.Label(self.Window,text="USER ID")
        self.id.grid(row=0,column=0,padx=10,pady=10,columnspan=2)
        self.Id=tk.Entry(self.Window)
        self.Id.grid(row=0,column=2)
        self.passcode=tk.Label(self.Window,text="Password")
        self.passcode.grid(row=1,column=0,padx=10,pady=10,columnspan=2)
        self.Passcode=tk.Entry(self.Window)
        self.Passcode.grid(row=1,column=2)
        self.name=tk.Label(self.Window,text="Name")
        self.name.grid(row=2,column=0,padx=10,pady=10,columnspan=2)
        self.Name=tk.Entry(self.Window)
        self.Name.grid(row=2,column=2)
        self.gender=tk.Label(self.Window,text="Gender")
        self.gender.grid(row=3,column=0)
        self.genop=tk.IntVar()
        self.g1=tk.Radiobutton(self.Window,text="Male",variable=self.genop,value=1)
        self.g2=tk.Radiobutton(self.Window,text="Female",variable=self.genop,value=2)
        self.g1.grid(row=3,column=1)
        self.g2.grid(row=3,column=2)
        self.dob=tk.Label(self.Window,text="Date Of Birth")
        self.dob.grid(row=4,column=0)
        self.Dob=tk.Entry(self.Window)
        self.Dob.grid(row=4,column=1)
        self.occu=tk.Label(self.Window,text="Occupation")
        self.occu.grid(row=5,column=0)
        self.Occu=tk.Entry(self.Window)
        self.Occu.grid(row=5,column=1)
        self.phoneno=tk.Label(self.Window,text="Phone Number")
        self.phoneno.grid(row=6,column=0)
        self.Phoneno=tk.Entry(self.Window)
        self.Phoneno.grid(row=6,column=1)
        self.nat=tk.Label(self.Window,text="Nationality")
        self.nat.grid(row=7,column=0)
        self.Nat=tk.Entry(self.Window)
        self.Nat.grid(row=7,column=1)
        self.address=tk.Label(self.Window,text="Address")
        self.address.grid(row=8,column=0)
        self.Address=tk.Entry(self.Window)
        self.Address.grid(row=8,column=1)
        self.Sub=tk.Button(self.Window,text="Submit",command=self.submit)
        self.Can=tk.Button(self.Window,text="Cancel",command=self.Wind.destroy)
        self.Sub.grid(row=9,column=0)
        self.Can.grid(row=9,column=1)
    def submit(self):
        self.Uid=self.Id.get()
        self.Upasscode=self.Passcode.get()
        self.Uname=self.Name.get()
        self.Ugender=self.genop
        self.Udob=self.Dob.get()
        self.Uoccu=self.Occu.get()
        self.Uphoneno=self.Phoneno.get()
        self.Unat=self.Nat.get()
        self.Uaddress=self.Address.get()
        Railways.Accounts[self.Uname]={"User ID":self.Uid,"Password":self.Upasscode,"Name":self.Uname,"Gender":self.Ugender,"Date of Birth":self.Udob,"Occupation":self.Uoccu,"Phone Number":self.Uphoneno,"Nationality":self.Unat,"Address":self.Uaddress}
        self.Window.destroy()
        self.Term()
    def Term(self):
        self.TermWin=tk.Frame(self.Wind)
        self.TermWin.grid()
        self.Wind.geometry("1000x400")
        self.TermHead=tk.Label(self.TermWin,text="TERMS AND CONDITIONS",fg="red",font="Calibri, 40")
        self.TermHead.grid(row=0,column=0)
        self.Mess=tk.Label(self.TermWin, text="By submitting your registration information, you indicate that you have read, understood and accepted the services offered.")
        self.Mess.grid(row=1,column=0)
        self.Mess.config(font="ariel,12")
        self.Checkvar=tk.IntVar()
        self.Accept=tk.Checkbutton(self.TermWin,text="I have read the terms and conditions.",variable=self.Checkvar)
        self.Accept.deselect()
        self.Accept.grid(row=2,column=0)
        self.oka=ttk.Button(self.TermWin,text="Agree and continue",command=self.Combine4)
        self.oka.grid(row=3,column=0)
        self.nok=ttk.Button(self.TermWin,text="Not Agree",command=self.Combine5)
        self.oka.grid(row=4,column=0)
    def Combine5(self):
        self.Wind.destroy()
        self.Create()
    def Combine4(self):
        if self.Checkvar.get()==0:
            showwarning(message="Please accept the terms and conditions!",parent=self.Wind)
        else:
            self.Congrats()
    def Congrats(self):
        self.TermWin.destroy()
        self.CongScr=tk.Frame(self.Wind)
        self.CongScr.pack()
        self.Udisp=tk.Label(self.CongScr,text=("Your Username="+str(self.Uname)),font="Ariel,30")
        self.Udisp.pack()
        self.Pdisp=tk.Label(self.CongScr,text=("Your Passcode="+str(self.Upasscode)),font="Ariel,30")
        self.Pdisp.pack()
        self.Disp=tk.Label(self.CongScr,text="You Have 5 Seconds to Note Your Username And Password....",font="Ariel,30")
        self.Disp.pack()
        self.Prog=ttk.Progressbar(self.CongScr,mode="determinate",value=0,maximum=90)
        self.Prog.pack()
        self.Prog.start(35)
        self.Wind.after(5550,lambda:self.Wind.destroy())
root=tk.Tk()
root.title("Railways")
root.geometry("900x700")
app=Railways(master=root)
app.mainloop()
root.destroy()
