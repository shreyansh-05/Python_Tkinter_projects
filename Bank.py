import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import random
import datetime

class Bank(tk.Frame):
    Accounts={}
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.grid()
        self.f=Font(family="Helvetica",size=72,underline=True)
        self.Acc=Font(family="Calibri",size=10,underline=True)
        self.Flag=0
        self.Widget1()
    def Widget1(self):
        
       
        self.Usertext=tk.Label(text="ACCOUNT HOLDER")
        self.Usertext.grid(row=1,column=0)
        self.username=tk.Entry()
        self.username.grid(row=1,column=1)
        self.Passtext=tk.Label(text="PASSWORD")
        self.Passtext.grid(row=2,column=0)
        self.password=tk.Entry(show="*")
        self.password.grid(row=2,column=1)
        self.enter=tk.Button(text="LOGIN",fg="black",bg="white",font=("Calibri",12),command=self.AccessAcc)
        self.enter.grid(row=3,column=0)
        self.exit=tk.Button(text="QUIT",fg="black",bg="white",command=root.quit,font=("Calibri",12))
        self.exit.grid(row=3,column=1)
        self.createAcc=tk.Button(text="CREATE ACCOUNT",command=self.Create)
        self.createAcc.grid(row=4,column=0)
        self.createAcc.config(font=self.Acc)
    def AccessAcc(self):
        self.e1=self.username.get()
        self.e2=self.password.get()
        if (self.e1 in Bank.Accounts):
            if (Bank.Accounts[self.e1])["Password"]==self.e2:
                self.Trans=tk.Toplevel(self)
                self.MainWin()
            else:
                    messagebox.showerror("Error", message="Invalid Password!")
        else:
                messagebox.showerror("Error", message="Invalid Username!")
    def MainWin(self):
        self.Transf=tk.Frame(self.Trans)
        self.Transf.grid()
        self.Welco=tk.Label(self.Transf,text=("WELCOME "+str(self.Uname).upper()+"!"),font="Courier 50",fg="blue")
        self.Welco.grid(row=0,column=0)
        self.now = datetime.datetime.now()
        self.date=tk.Label(self.Transf,text=("Date:"+str(self.now.day)+"/"+str(self.now.month)+"/"+str(self.now.year)),font="Ariel 20")
        self.date.grid(row=1,column=0)
        self.Time=tk.Label(self.Transf,font="Ariel 20")
        self.Time.grid(row=2,column=0)
        self.BalEnq=tk.Button(self.Transf,text="Balance Enquiry",command=self.BalanceDisp)
        self.BalEnq.grid(row=3,column=0)
        self.With=tk.Button(self.Transf,text="Withdrawal",command=self.Withdraw)
        self.With.grid(row=4,column=0)
        self.Dep=tk.Button(self.Transf,text="Deposit",command=self.Deposit)
        self.Dep.grid(row=5,column=0)
        self.Oth=tk.Button(self.Transf,text="Others",command=self.OthScr)
        self.Oth.grid(row=6,column=0)
        self.Logout=tk.Button(self.Transf,text="Logout", command=self.Trans.destroy)
        self.Logout.grid(row=7,column=3,padx=10,pady=10)
        self.clock()
    def clock(self):
        self.time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        self.Time.config(text=self.time)
        self.Transf.after(1000, self.clock)
    def Withdraw(self):
        self.Transf.destroy()
        self.WithWin=tk.Frame(self.Trans)
        self.WithWin.grid()
        self.WithHead=tk.Label(self.WithWin,text="Cash Withdraw")
        self.WithHead.grid(row=1,column=1)
        self.ModeOfDep=tk.Label(self.WithWin,text="MODE OF DEPOSIT")
        self.ModeOfDep.grid(row=2,column=0)
        self.ModVar=tk.IntVar()
        self.Mod1=tk.Radiobutton(self.WithWin,text="By Cash",variable=self.ModVar,value=1)
        self.Mod2=tk.Radiobutton(self.WithWin,text="By Cheque",variable=self.ModVar,value=2)
        self.Mod1.grid(row=2,column=1)
        self.Mod2.grid(row=2,column=2)
        self.WithAmt=tk.Label(self.WithWin,text="Withdraw Amount: ")
        self.WithAmt.grid(row=3,column=0)
        self.WithAmtGet=tk.IntVar()
        self.WithAmtEnt=tk.Entry(self.WithWin,textvariable=self.WithAmtGet)
        self.WithAmtEnt.grid(row=3,column=1)
        self.WithOk=ttk.Button(self.WithWin,text="OK",command=self.WithMoney)
        self.WithOk.grid(row=4,column=1)
    def WithMoney(self):
        if self.WithAmtGet.get()>self.Uopen:
            messagebox.showerror(message="Insufficient Funds",parent=self.WithWin)
        else:
            self.Uopen=self.Uopen-self.WithAmtGet.get()
            Bank.Accounts[self.Uname]["Opening Amount"]=self.Uopen
            self.WithDone=messagebox.showinfo(message="Transaction Successful",parent=self.WithWin)
            self.WithWin.destroy()
            self.MainWin()
    def Deposit(self):
        self.Transf.destroy()
        self.DepWin=tk.Frame(self.Trans)
        self.DepWin.grid()
        self.DepHead=tk.Label(self.DepWin,text="Cash/Cheque Deposit")
        self.DepHead.grid(row=1,column=1)
        self.ModeOfDep=tk.Label(self.DepWin,text="MODE OF DEPOSIT")
        self.ModeOfDep.grid(row=2,column=0)
        self.ModVar=tk.IntVar()
        self.Mod1=tk.Radiobutton(self.DepWin,text="By Cash",variable=self.ModVar,value=1)
        self.Mod2=tk.Radiobutton(self.DepWin,text="By Cheque",variable=self.ModVar,value=2)
        self.Mod1.grid(row=2,column=1)
        self.Mod2.grid(row=2,column=2)
        self.DepAmt=tk.Label(self.DepWin,text="Deposit Amount: ")
        self.DepAmt.grid(row=3,column=0)
        self.DepAmtGet=tk.IntVar()
        self.DepAmtEnt=tk.Entry(self.DepWin,textvariable=self.DepAmtGet)
        self.DepAmtEnt.grid(row=3,column=1)
        self.DepOk=ttk.Button(self.DepWin,text="OK",command=self.DepoMoney)
        self.DepOk.grid(row=4,column=1)
    def DepoMoney(self):
        self.Uopen=self.Uopen+self.DepAmtGet.get()
        Bank.Accounts[self.Uname]["Opening Amount"]=self.Uopen
        self.DepDone=messagebox.showinfo(message="Transaction Successful",parent=self.DepWin)
        self.DepWin.destroy()
        self.MainWin()
    def BalanceDisp(self):
        self.Transf.destroy()
        self.BalWin=tk.Frame(self.Trans)
        self.BalWin.pack()
        self.Disp=tk.Label(self.BalWin,text=("A/C Number: "+str(self.Uacno)+"\n Username: "+str(self.Uname)+"\n Age: "+str(self.Uage)+"\n Occupation: "+str(self.Uoccu)+"\n Address: "+str(self.Uaddress)+"\n Phone Number: "+str(self.Uphoneno)+"\n Current Balance: "+str(self.Uopen)),font="Calibri 30")
        self.Disp.pack()
        self.BalOk=ttk.Button(self.BalWin,text="Ok",command=self.Combine)
        self.BalOk.pack()
    def Combine(self):
        self.BalWin.destroy()
        self.MainWin()
    def OthScr(self):
        self.Transf.destroy()
        self.OthFr=tk.Frame(self.Trans)
        self.OthFr.pack()
        self.Alt=tk.Label(self.OthFr,text="ACCOUNT ALTERATION SCREEN",font="Calibri 40",fg="red")
        self.Alt.pack()
        self.AccMod=tk.Button(self.OthFr,text="Account Modification",command=self.Combine3)
        self.AccMod.pack()
        self.ChanPass=tk.Button(self.OthFr,text="Change Password",command=self.ChangePassword)
        self.ChanPass.pack()
        self.ClosAcc=tk.Button(self.OthFr,text="Closing Account",command=self.Closing)
        self.ClosAcc.pack()
        self.Ext=tk.Button(self.OthFr,text="Exit",command=self.Trans.destroy)
        self.Ext.pack(anchor="se")
    def Closing(self):
        self.Answer=messagebox.askyesno(message="Are you sure you want to close your Account?",parent=self.Trans)
        if self.Answer==True:
            self.OthFr.destroy()
            self.ClosFr=tk.Frame(self.Trans)
            self.ClosFr.pack()
            self.EndLab=tk.Label(self.ClosFr,text=("Thank you!"+"\n A/C Number: "+str(self.Uacno)+"\n Username: "+str(self.Uname)+"\n Age: "+str(self.Uage)+"\n Occupation: "+str(self.Uoccu)+"\n Address: "+str(self.Uaddress)+"\n Phone Number: "+str(self.Uphoneno)+"\n Balance: "+str(self.Uopen)),font="Calibri 30")
            self.EndLab.pack()
            del Bank.Accounts[self.Uname]
            self.EndOk=tk.Button(self.ClosFr,text="Ok",command=self.Trans.destroy)
            self.EndOk.pack()
        else:
            self.OthFr.destroy()
            self.MainWin()
    def Combine3(self):
        self.ModAsk=messagebox.askyesno(message="Are you sure you want to modify your account?",parent=self.Trans)
        if self.ModAsk==True:
            self.Uac=long(Bank.Accounts[self.Uname]["Account Number"])
            self.Openamt=int(Bank.Accounts[self.Uname]["Opening Amount"])
            del Bank.Accounts[self.Uname]
            self.Flag=1
            self.Trans.destroy()
            self.Create()
        else:
            self.OthFr.destroy()
            self.MainWin()
    def ChangePassword(self):
        self.OthFr.destroy()
        self.Chaf=tk.Frame(self.Trans)
        self.Chaf.grid()
        self.ChafHead=tk.Label(self.Chaf,text="CHANGE PASSWORD",font="Calibri 40")
        self.ChafHead.grid(row=1,column=0,sticky=W)
        self.ChafMess=tk.Label(self.Chaf,text="Enter New Password")
        self.ChafMess.grid(row=2,column=0,sticky=W)
        self.ChafNew=tk.Entry(self.Chaf)
        self.ChafNew.grid(row=2,column=1,sticky=W)
        self.PasChan=tk.Button(self.Chaf,text="CHANGE",command=self.StNewPass)
        self.PasChan.grid(row=3,column=0,sticky=W)
        self.ChanCan=tk.Button(self.Chaf,text="CANCEL",command=self.Combine1)
        self.ChanCan.grid(row=3,column=1,sticky=W)
    def StNewPass(self):
        self.Newpass=self.ChafNew.get()
        Bank.Accounts[self.Uname]["Password"]=self.Newpass
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
        self.name=tk.Label(self.Window,text="Name")
        self.name.grid(row=0,column=0,sticky='W')
        self.Name=tk.Entry(self.Window)
        self.Name.grid(row=0,column=1)
        self.age=tk.Label(self.Window,text="Age")
        self.age.grid(row=1,column=0,sticky='W')
        self.Age=tk.Entry(self.Window)
        self.Age.grid(row=1,column=1)
        self.passcode=tk.Label(self.Window,text="Password")
        self.passcode.grid(row=2,column=0,sticky='W')
        self.Passcode=tk.Entry(self.Window)
        self.Passcode.grid(row=2,column=1)
        self.occu=tk.Label(self.Window,text="Occupation")
        self.occu.grid(row=3,column=0,sticky='W')
        self.Occu=tk.Entry(self.Window)
        self.Occu.grid(row=3,column=1)
        self.address=tk.Label(self.Window,text="Address")
        self.address.grid(row=4,column=0,sticky='W')
        self.Address=tk.Entry(self.Window)
        self.Address.grid(row=4,column=1)
        self.phoneno=tk.Label(self.Window,text="Phone Number")
        self.phoneno.grid(row=5,column=0,sticky='W')
        self.Phoneno=tk.Entry(self.Window)
        self.Phoneno.grid(row=5,column=1)
        if self.Flag==0:
            self.open=tk.Label(self.Window,text="Opening Amount")
            self.open.grid(row=6,column=0,sticky='W')
            self.Open1=tk.IntVar()
            self.Open=tk.Entry(self.Window,textvariable=self.Open1)
            self.Open.grid(row=6,column=1)
        self.cheque=tk.Label(self.Window,text="Cheque Facility")
        self.var=tk.IntVar()
        self.Cheque=tk.Label(self.Window,text="Cheque Facility")
        self.Cheque.grid(row=7,column=0,sticky='W')
        self.ChequeR1=tk.Radiobutton(self.Window,text="Yes",variable=self.var,value=1)
        self.ChequeR2=tk.Radiobutton(self.Window,text="No",variable=self.var,value=2)
        self.ChequeR1.grid(row=7,column=1)
        self.ChequeR2.grid(row=7,column=2)
        self.var1=tk.IntVar()
        self.typ=tk.Label(self.Window,text="Account Type")
        self.typ.grid(row=8,column=0,sticky='W')
        self.typ1=tk.Radiobutton(self.Window,text="Savings",variable=self.var1,value=1)
        self.typ2=tk.Radiobutton(self.Window,text="Current",variable=self.var1,value=2)
        self.typ3=tk.Radiobutton(self.Window,text="Fixed Deposit",variable=self.var1,value=3)
        self.typ4=tk.Radiobutton(self.Window,text="Recurring Deposit",variable=self.var1,value=4)
        self.typ1.grid(row=8,column=1)
        self.typ2.grid(row=8,column=2)
        self.typ3.grid(row=8,column=3)
        self.typ4.grid(row=8,column=4)
        self.Sub=tk.Button(self.Window,text="Submit",command=self.submit)
        self.Can=tk.Button(self.Window,text="Cancel",command=self.Wind.destroy)
        self.Sub.grid(row=9,column=0,sticky='W')
        self.Can.grid(row=9,column=1)
    def submit(self):
        self.Uname=self.Name.get()
        self.Uage=self.Age.get()
        self.Upasscode=self.Passcode.get()
        self.Uoccu=self.Occu.get()
        self.Uaddress=self.Address.get()
        self.Uphoneno=self.Phoneno.get()
        if self.Flag==0:
            self.Uopen=self.Open1.get()
            self.Uacno=random.randint(100000000,1000000000)
        else:
            self.Uopen=int(self.Openamt)
            self.Uacno=self.Uac
        self.CheqFac=self.var
        self.AcTyp=self.var
        Bank.Accounts[self.Uname]={"Password":self.Upasscode,"Age":self.Uage,"Occupation":self.Uoccu,"Address":self.Uaddress,"Phone Number":self.Uphoneno,"Opening Amount":self.Uopen,"Cheque Facility":self.CheqFac,"Account Type":self.AcTyp,"Account Number":self.Uacno}
        self.Window.destroy()
        self.Term()
    def Term(self):
        self.TermWin=tk.Frame(self.Wind)
        self.TermWin.grid()
        self.TermHead=tk.Label(self.TermWin,text="TERMS AND CONDITIONS",fg="red",font="Calibri, 40")
        self.TermHead.grid(row=0,column=0)
        self.ThingToRem=tk.Label(self.TermWin,text="THINGS TO REMEMBER",fg="blue",font="Calibri, 40")
        self.ThingToRem.grid(row=1,column=0)
        self.Mess=tk.Label(self.TermWin, text="        Account Type \t Minimum Balance \n \
Saving \t 1000 \n \
Current \t 3000 \n \
Fixed Deposit \t 2000 \n \
Recurring Deposit \t 3000 ")
        self.Mess.grid(row=2,column=0)
        self.Mess.config(font="ariel,12")
        self.Line=tk.Label(self.TermWin,text='''
Pin Number must be of 4 digits.
While re- opening an account,the deposit amount must be at least Rs. 2000''')
        self.Line.grid(row=3,column=0)
        self.Line.config(font="ariel,12")
        self.Checkvar=tk.IntVar()
        self.Accept=tk.Checkbutton(self.TermWin,text="I have read the terms and conditions.",variable=self.Checkvar)
        self.Accept.deselect()
        self.Accept.grid(row=4,column=0)
        self.oka=tk.Button(self.TermWin,text="Ok",command=self.Combine4)
        self.oka.grid(row=5,column=0)
    def Combine4(self):
        if self.Checkvar.get()==0:
            messagebox.showwarning(message="Please accept the terms and conditions!",parent=self.Wind)
        else:
            self.Congrats()
    def Congrats(self):
        self.TermWin.destroy()
        self.CongScr=tk.Frame(self.Wind)
        self.CongScr.pack()
        self.CongDisp=tk.Label(self.CongScr,text=('CONGRATULATIONS FOR YOUR NEW ACCOUNT \n Your Account Number is '+str(self.Uacno)),fg="red",font="Ariel,30")
        self.CongDisp.pack()
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
root.title("Bank")
root.geometry("900x700")
root.resizable(0,0)
app=Bank(master=root)
app.mainloop()
root.destroy()
