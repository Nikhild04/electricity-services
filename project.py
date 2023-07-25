from tkinter import *
# from PIL import Image,ImageTk
import sqlite3
from time import *

root=Tk()
root.geometry("1000x700")
root.resizable(False,False)
# root.wm_iconbitmap('logo.png')

root.config(bg="lightblue")
Label(root,text="ELECTRICITY SERVICES",bg="black",fg="white",font=("calibri",28),width="300",height="1").pack()


#========================================================================
#output frame
class frames:
    def __init__(self,root):
        # self.root=root
        self.output=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=2)
        self.output.config(bg="lightgreen",width=330,height=500)
        self.output.place(x=650,y=150)
        self.l1=Label(self.output,text="OUPUT FRAME",font=("Gabriola",22,"bold"),fg="black",bg="lightgreen").place(x=70,y=5)


    
    def project1(self):
       Label(self.output,text='  ',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)

    def clear1(self):
            self.project1()
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
    
    def clear(self):
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
    #========================================================================
    #Bill genrator frame
    def bill_genrator(self):
        self.project1()
        self.Bill_genrator=Frame(root,bg="#84bdbc",highlightbackground="black",highlightthickness=2)
        self.Bill_genrator.config(bg="#84bdbc",width=630,height=500)
        self.Bill_genrator.place(x=10,y=150)
        self.bill_no1=Label(self.Bill_genrator,text="GENRATE YOUR BILL ",font=("Gabriola",20,"bold"),fg="black",bg="#84bdbc").place(x=100,y=5)
        self.bill_no2=Label(self.Bill_genrator,text='BILL NO',font=("Arial ",12,"bold"),fg="black",bg="#84bdbc").place(x=20,y=80)
        self.bill_no3=Label(self.Bill_genrator,text='HOUSE NO',font=("Arial ",12,"bold"),fg="black",bg="#84bdbc").place(x=20,y=110)
        self.bill_no4=Label(self.Bill_genrator,text='NAME',font=("Arial ",12,"bold"),fg="black",bg="#84bdbc").place(x=20,y=140)
        self.bill_no5=Label(self.Bill_genrator,text='NO UNITS',font=("Arial ",12,"bold"),fg="black",bg="#84bdbc").place(x=20,y=170)
        self.bill_no6=Label(self.Bill_genrator,text='TYPE',font=("Arial ",12,"bold"),fg="black",bg="#84bdbc").place(x=20,y=200)

        self.r=StringVar()
        self.r.set('domestic')
        self.r1=Radiobutton(self.Bill_genrator,text='HOME',font=("Arial",12,"bold"),fg="black",bg="#84bdbc",variable=self.r,value='domestic').place(x=120,y=200)
        self.r2=Radiobutton(self.Bill_genrator,text='COMMERTIAL',font=("Arial",12,"bold"),fg="black",bg="#84bdbc",variable=self.r,value='commertial').place(x=220,y=200)
        
        self.e1=Entry(self.Bill_genrator,width=50)
        self.e1.place(x=120,y=80)
        self.e2=Entry(self.Bill_genrator,width=50)
        self.e2.place(x=120,y=110)
        self.e3=Entry(self.Bill_genrator,width=50)
        self.e3.place(x=120,y=140)
        self.e4=Entry(self.Bill_genrator,width=50)
        self.e4.place(x=120,y=170)

        def project():
            self.bill_no2=Label(self.output,text='BILL NO',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=80)
            self.bill_no3=Label(self.output,text='HOUSE NO',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=110)
            self.bill_no4=Label(self.output,text='NAME',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=140)
            self.bill_no5=Label(self.output,text='BILL TYPE',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=170)
            self.bill_no6=Label(self.output,text='NO UNITS',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=200)
            self.bill_no7=Label(self.output,text='TOTAL AMT',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=230)

            self.ll=Label(self.output,text=":  "+self.e1.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=80)
            self.ll=Label(self.output,text=":  "+self.e2.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=110)
            self.ll=Label(self.output,text=":  "+self.e3.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=140)
            self.ll=Label(self.output,text=":  "+self.r.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=170)
            self.ll=Label(self.output,text=":  "+self.e4.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=200)
            # self.ll=Label(self.output,text=":  "+self.e5.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=200)
            

            self.tq=Label(self.output,text="HAVE A NICE DAY  :)",font=("Gabriola",22,"bold"),fg="black",bg="lightgreen").place(x=100,y=400)
            self.clear()

        def genrate():
            try:
                conn=sqlite3.connect('BILL_DATA.db')
                c=conn.cursor()
                q="select * from elecricity"
                c.execute(q)
                r=c.fetchall()
                billno=int(self.e1.get())
                houseno=int(self.e2.get())
                name=self.e3.get()
                no_units=int(self.e4.get())
                typ=self.r.get()
                # bno=[]
                # hno=[]
                # n=[]
                # bi=[]
                # ty=[]
                # for i in r:
                #     bno.append(i[0])
                #     hno.append(i[1])
                #     n.append(i[2])
                #     bi.append(i[3])
                #     ty.append(i[4])
                # if ((billno in bno ) and (houseno in hno ) and (name in n ) ):
                #     print('1st')
                if ((billno==int(r[houseno-1][0])) and (name==str(r[houseno-1][2])) and typ==r[houseno-1][4]) :
                        if typ=='domestic':
                            cost=120
                        else:
                            cost=150
                        bill_charge=no_units*cost
                        cbill=int(r[houseno-1][3])
                        nbill=cbill+bill_charge
                        q="update elecricity set bill=(?) where house_no=(?)"
                        c.execute(q,(nbill,houseno))
                        print('bill updated')
                        Label(self.output,text=":  "+str(nbill),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=230)
                        project()
                else:
                    self.li=Label(self.output,text='Invalid details.',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)



                # q="update elecricity set bill_no=(?) where house_no=(?)"
                # c.execute(q,(mr,roll))
                conn.commit()
                conn.close()
            except Exception as e:
                Label(self.output,text='Invalid details.',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)
                print(e)

        self.bt=Button(self.Bill_genrator,text="SUMBIT",font=("Arial ",12,"bold"),command=genrate).place(x=260,y=400)
        self.reset=Button(self.Bill_genrator,text="RESET ",font=("Arial ",12,"bold"),command=self.clear1).place(x=180,y=400)

        

    #========================================================================
    # def bill_payment()
    def bill_payment(self):
        self.project1()
        self.Bill_pay=Frame(root,bg="pink",highlightbackground="black",highlightthickness=2)
        self.Bill_pay.config(bg="pink",width=630,height=500)
        self.Bill_pay.place(x=10,y=150)
        self.bill_no1=Label(self.Bill_pay,text="PAY YOUR BILL ",font=("Gabriola",20,"bold"),fg="black",bg="pink").place(x=100,y=5)
        self.bill_no2=Label(self.Bill_pay,text='BILL NO',font=("Arial ",12,"bold"),fg="black",bg="pink").place(x=20,y=80)
        self.bill_no3=Label(self.Bill_pay,text='HOUSE NO',font=("Arial ",12,"bold"),fg="black",bg="pink").place(x=20,y=110)
        self.bill_no4=Label(self.Bill_pay,text='NAME',font=("Arial ",12,"bold"),fg="black",bg="pink").place(x=20,y=140)
        self.bill_no4=Label(self.Bill_pay,text='AMOUNT',font=("Arial ",12,"bold"),fg="black",bg="pink").place(x=20,y=170)
        self.bill_no6=Label(self.Bill_pay,text='TYPE',font=("Arial ",12,"bold"),fg="black",bg="pink").place(x=20,y=200)

        self.r=StringVar()
        self.r.set('domestic')
        self.r1=Radiobutton(self.Bill_pay,text='HOME',font=("Arial",12,"bold"),fg="black",bg="pink",variable=self.r,value='domestic').place(x=120,y=200)
        self.r2=Radiobutton(self.Bill_pay,text='COMMERTIAL',font=("Arial",12,"bold"),fg="black",bg="pink",variable=self.r,value='commertial').place(x=220,y=200)

        self.e1=Entry(self.Bill_pay,width=50)
        self.e1.place(x=120,y=80)
        self.e2=Entry(self.Bill_pay,width=50)
        self.e2.place(x=120,y=110)
        self.e3=Entry(self.Bill_pay,width=50,state=DISABLED)
        self.e3.place(x=120,y=140)
        self.e4=Entry(self.Bill_pay,width=50,state=DISABLED)
        self.e4.place(x=120,y=170)

        def makebill():
            t=IntVar()
            t.set(1)
            Radiobutton(self.Bill_pay,text='UPI',font=("Arial",12,"bold"),fg="black",bg="pink",value=1,variable=t).place(x=120,y=290)
            Radiobutton(self.Bill_pay,text='NET BANKING',font=("Arial",12,"bold"),fg="black",bg="pink",value=0,variable=t).place(x=200,y=290)

            try:    
                conn=sqlite3.connect('BILL_DATA.db')
                c=conn.cursor()
                q="select * from elecricity"
                c.execute(q)
                r=c.fetchall()
                billno=int(self.e1.get())
                houseno=int(self.e2.get())
                typ=self.r.get()
                print(r[houseno-1][2],r[houseno-1][3])
                if billno==int(r[houseno-1][0]) and typ==str(r[houseno-1][4]):
                    print('yes')
                    self.e3=Entry(self.Bill_pay,width=50)
                    self.e3.insert(0,r[houseno-1][2])
                    self.e3.place(x=120,y=140)
                    self.e4=Entry(self.Bill_pay,width=50)
                    self.e4.insert(0,r[houseno-1][3])
                    self.e4.place(x=120,y=170)
                    self.bt=Button(self.Bill_pay,text="MAKE PAYMENT",font=("Arial ",12,"bold"),command=makepayment).place(x=260,y=400)
                    # self.e4.insert(r[houseno-1][3])
                else:
                    Label(self.output,text='Invalid details.',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)
                conn.commit()
                conn.close()
            except Exception as e:
                Label(self.output,text='Invalid details.',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)
                print(e)

        def makepayment():
            try:
                houseno=int(self.e2.get())
                conn=sqlite3.connect('BILL_DATA.db')
                c=conn.cursor()
                q="update elecricity set bill=(?) where house_no=(?)"
                c.execute(q,(0,houseno))
            except:
                print('error occered ')
            sleep(2)
            li=Label(self.output,text='Payment Completed .',font=("Arial ",12,"bold"),fg="black",bg="lightgreen")
            li.place(x=0,y=80)
            self.tq=Label(self.output,text="HAVE A NICE DAY  :)",font=("Gabriola",22,"bold"),fg="black",bg="lightgreen").place(x=100,y=400)
            
        
        def project():
            self.l1=Label(self.output,text=self.d1,font=("Gabriola",22,"bold"),fg="black",bg="lightgreen").place(x=70,y=50)

        self.bt=Button(self.Bill_pay,text="MAKE BILL",font=("Arial ",12,"bold"),command=makebill).place(x=120,y=250)
        self.bt=Button(self.Bill_pay,text="MAKE PAYMENT",font=("Arial ",12,"bold"),command=makepayment,state=DISABLED).place(x=260,y=400)
        self.reset=Button(self.Bill_pay,text="RESET ",font=("Arial ",12,"bold"),command=self.clear1).place(x=180,y=400)

    #========================================================================
    # def bill_payment()
    def bill_viwer(self):
        self.project1()
        self.Bill_viewer=Frame(root,bg="#cc7676",highlightbackground="black",highlightthickness=2)
        self.Bill_viewer.config(bg="#cc7676",width=630,height=500)
        self.Bill_viewer.place(x=10,y=150)
        self.bill_no1=Label(self.Bill_viewer,text="CHECK YOUR BILL ",font=("Gabriola",20,"bold"),fg="black",bg="#cc7676").place(x=100,y=5)
        self.bill_no2=Label(self.Bill_viewer,text='BILL NO',font=("Arial ",12,"bold"),fg="black",bg="#cc7676").place(x=20,y=80)
        self.bill_no3=Label(self.Bill_viewer,text='HOUSE NO',font=("Arial ",12,"bold"),fg="black",bg="#cc7676").place(x=20,y=110)
        self.bill_no4=Label(self.Bill_viewer,text='NAME',font=("Arial ",12,"bold"),fg="black",bg="#cc7676").place(x=20,y=140)
        # self.bill_no4=Label(self.Bill_viewer,text='NO UNITS',font=("Arial ",12,"bold"),fg="black",bg="#cc7676").place(x=20,y=170)
        self.bill_no6=Label(self.Bill_viewer,text='TYPE',font=("Arial ",12,"bold"),fg="black",bg="#cc7676").place(x=20,y=170)

        self.e1=Entry(self.Bill_viewer,width=50)
        self.e1.place(x=120,y=80)
        self.e2=Entry(self.Bill_viewer,width=50)
        self.e2.place(x=120,y=110)
        self.e3=Entry(self.Bill_viewer,width=50)
        self.e3.place(x=120,y=140)
        # self.e4=Entry(self.Bill_viewer,width=50)
        # self.e4.place(x=120,y=170)

        self.r=StringVar()
        self.r.set('domestic')
        Radiobutton(self.Bill_viewer,text='HOME',font=("Arial",12,"bold"),fg="black",bg="#cc7676",variable=self.r,value='domestic').place(x=120,y=170)
        Radiobutton(self.Bill_viewer,text='COMMERTIAL',font=("Arial",12,"bold"),fg="black",bg="#cc7676",variable=self.r,value='commertial').place(x=220,y=170)
        def clear():
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
        def clear1():
            self.project1()
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)

        def project():        

            self.bill_no2=Label(self.output,text='BILL NO',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=80)
            self.bill_no3=Label(self.output,text='HOUSE NO',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=110)
            self.bill_no4=Label(self.output,text='NAME',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=140)
            self.bill_no5=Label(self.output,text='TYPE OF',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=170)
            self.bill_no6=Label(self.output,text='TOTAL BILL',font=("Arial ",12,"bold"),fg="black",bg="lightgreen").place(x=10,y=200)

            self.ll=Label(self.output,text=":  "+self.e1.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=80)
            self.ll=Label(self.output,text=":  "+self.e2.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=110)
            self.ll=Label(self.output,text=":  "+self.e3.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=140)
            self.ll=Label(self.output,text=":  "+self.r.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=170)
            # self.ll=Label(self.output,text=":  "+self.e5.get(),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=200)

            self.tq=Label(self.output,text="HAVE A NICE DAY  :)",font=("Gabriola",22,"bold"),fg="black",bg="lightgreen").place(x=100,y=400)

        def genrate():
            Label(self.output,text='',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)
            try:
                conn=sqlite3.connect('BILL_DATA.db')
                c=conn.cursor()
                q="select * from elecricity"
                c.execute(q)
                r=c.fetchall()
                billno=int(self.e1.get())
                houseno=int(self.e2.get())
                name=self.e3.get()
                typ=self.r.get()
                if ((billno==int(r[houseno-1][0])) and (name==str(r[houseno-1][2])) and typ==r[houseno-1][4]) :
                        Label(self.output,text=":  "+str(r[houseno-1][3]),font=("Arial",12,"bold"),fg="black",bg="lightgreen").place(x=100,y=200)
                        project()
                else:
                    self.li=Label(self.output,text='Invalid details.',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)
                conn.commit()
                conn.close()
            except Exception as e:
                Label(self.output,text='Invalid details.',font=("Arial ",12,"bold"),fg="black",bg="lightgreen",width=32,height=19).place(x=0,y=80)
                print(e)
        self.bt=Button(self.Bill_viewer,text="VIEW BILL",font=("Arial ",12,"bold"),command=genrate).place(x=260,y=400)
        self.reset=Button(self.Bill_viewer,text="RESET ",font=("Arial ",12,"bold"),command=clear1).place(x=180,y=400)
# myimg=ImageTk.PhotoImage(Image.open('logo1.jpg'))
# my_label=Label(image=myimg)
# my_label.place(x=0,y=0)

# img2=ImageTk.PhotoImage(Image.open('zenetsu.jpg'))
# my_label2=Label(image=img2)
# my_label2.place(x=850,y=0)

d=frames(root)
genrate=Button(root,text="GENRATE BILL",font=("Arial ",12,"bold"),width="15",command=d.bill_genrator)
genrate.place(x=50,y=75)
pay=Button(root,text="PAY BILL",font=("Arial ",12,"bold"),width="15",bg="white",command=d.bill_payment)
pay.place(x=250,y=75)
view=Button(root,text="VIEW BILL",font=("Arial ",12,"bold"),width="15",bg="white",command=d.bill_viwer)
view.place(x=450,y=75)
Button(root,text="EXIT PROGRAM",font=("Arial ",12,"bold"),width="15",bg="white",command=root.quit).place(x=330,y=660)
root.mainloop()