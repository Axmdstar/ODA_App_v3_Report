from time import sleep
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import ImageTk
import PIL.Image
from tkinter import *
from Sql import SQL
import tkinter as tk


class TimePicker(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs, bg="white")

        # Hour spinner
        self.hour_var = tk.StringVar(value='12')
        self.hour_spinner = tk.Spinbox(self, from_=1, to=12, width=3, textvariable=self.hour_var, bg='white')
        self.hour_spinner.pack(side='left')

        # Minute spinner
        self.minute_var = tk.StringVar(value='00')
        self.minute_spinner = tk.Spinbox(self, from_=0, to=59, width=3, textvariable=self.minute_var, bg='white')
        self.minute_spinner.pack(side='left')

        # AM/PM selector
        self.am_pm_var = tk.StringVar(value='AM')
        self.am_pm_selector = tk.OptionMenu(self, self.am_pm_var, 'AM', 'PM')
        self.am_pm_selector.pack(side='left')

    def get(self):
        return f"{self.hour_var.get()}:{self.minute_var.get()} {self.am_pm_var.get()}"


class CreateAp(ttk.Frame):
    def __init__(self, root, sql):
        self.sql = sql
        super().__init__(root, width=900, height=600)

        # image
        self.bg_img = PIL.Image.open('../Images/bg.png')
        self.resize = self.bg_img.resize((500, 600))
        self.img = ImageTk.PhotoImage(self.resize)
        self.bg = Label(self, image=self.img)

        # labels
        self.name = Label(self, text="Full Name :", bg='white', font=('Helvetica', '13'))
        self.sex = Label(self, text="Sex :", bg='white', font=('Helvetica', '13'))
        self.tel = Label(self, text="Tel :", bg='white', font=('Helvetica', '13'))
        self.doctor = Label(self, text="Doctor :", bg='white', font=('Helvetica', '13'))
        self.symptoms = Label(self, text="Symptoms :", bg='white', font=('Helvetica', '13'))
        self.time = Label(self, text="Time :", bg='white', font=('Helvetica', '13'))
        self.date = Label(self, text="Date :", bg='white', font=('Helvetica', '13'))
        self.payment = Label(self, text="Payment :", bg='white', font=('Helvetica', '13'))
        self.Lprice = Label(self, text="Price :", bg='white', font=('Helvetica', '13'))
        self.price_ = Label(self, text="", bg='white', font=('Helvetica', '13'))
        self.storepr = ''

        # inputs
        self.inpt_name = Entry(self, borderwidth=0, justify='center',
                               font=('Helvetica', '14'), highlightthickness=2,highlightcolor='#72efdd')
        self.inpt_sex = StringVar()
        self.male = Radiobutton(self, text="Male", value="Male", variable=self.inpt_sex, bg='white')
        self.female = Radiobutton(self, text="Female", value="Female", variable=self.inpt_sex, bg='white')
        self.inpt_tel = Entry(self, borderwidth=0, justify='center',
                              font=('Helvetica', '14'), highlightthickness=2,highlightcolor='#72efdd')

        # Doctors
        self.doctors = ("Choose Doctor",
                       "Doctor ka indhaha : Ophthalmology",
                       "Doctor ka carurta : Pediatrics",
                       "Doctor ka jirka : Rheumatology",
                       "Doctor ka Calosha : Gastroenterology")

        self.option_var = StringVar()
        self.option_var.set(self.doctors[0])
        self.inpt_doctor = OptionMenu(
                            self,
                            self.option_var,
                            *self.doctors, command=self.checkdocprice)

        # symptoms
        self.inpt_symptoms = Text(self, width=25, height=8, borderwidth=2)

        # date and time
        self.inpt_time_aval = TimePicker(self)
        self.inpt_date = DateEntry(self)


        # buttons
        self.bg_btn = PIL.Image.open('../Images/Asset 4@2x.png')
        self.rebtn = self.bg_btn.resize((100, 50))
        self.btn = ImageTk.PhotoImage(self.rebtn)
        self.submit = Button(self, bg="white",
                             image=self.btn, borderwidth=0, command=self.submit)

        # placement
        self.bg.pack()
        self.name.place(x=50, y=30)
        self.inpt_name.place(x=145, y=30)

        self.sex.place(x=50, y=70)
        self.male.place(y=70, x=145)
        self.female.place(y=70, x=255)

        self.tel.place(x=50, y=110)
        self.inpt_tel.place(x=145, y=110)

        self.doctor.place(x=50, y=150)
        self.inpt_doctor.place(y=150, x=145)

        self.Lprice.place(y=400, x=50)
        self.price_.place(y=400, x=100)

        self.symptoms.place(x=50, y=190)
        self.inpt_symptoms.place(x=145, y=190)

        self.time.place(x=50, y=350)
        self.inpt_time_aval.place(x=120, y=350)

        self.date.place(x=300, y=350)
        self.inpt_date.place(x=350, y=350)

        self.submit.place(x=200, y=400)


    # functions
    def submit(self):

        # getting entry values
        name_value = self.inpt_name.get()
        sex_value = self.inpt_sex.get()
        tel_value = self.inpt_tel.get()
        doctor_value = self.option_var.get()
        sym_value = self.inpt_symptoms.get("1.0", "end")
        time_value = self.inpt_time_aval.get()
        data_value = self.inpt_date.get()
        prices = self.storepr

        # adding to the db
        self.sql.inserting(name_value, sex_value, tel_value, doctor_value, sym_value, time_value, data_value, prices)
        # debugging
        # print(name_value)
        # print(sex_value)
        # print(tel_value)
        # print(doctor_value)
        # print(sym_value)
        # print(time_value)
        # print(data_value)
        # print(prices)

        # clear Entries
        self.inpt_name.delete(0, 'end')
        self.inpt_tel.delete(0, 'end')
        self.inpt_symptoms.delete('1.0', 'end')
        self.inpt_date.delete(0, 'end')

    def checkdocprice(self, *args):
        docprices = {"Doctor ka indhaha : Ophthalmology": 60,
                     "Doctor ka carurta : Pediatrics": 30,
                     "Doctor ka jirka : Rheumatology": 40,
                     "Doctor ka Calosha : Gastroenterology": 20,
                     "Choose Doctor": ""
                     }

        newvalue = self.option_var.get()
        self.price_.config(text=f"{docprices[newvalue]}$")
        self.storepr = docprices[newvalue]


class ReportFrame(tk.Frame):
    def __init__(self, root, sql):
        self.root = root
        self.sql = sql
        self.report_data = self.sql.Reports()
        super().__init__(root, width=100, height=100)
        self.configure(background="White")


        self.number_ap_L = Label(self, text="Number of Appointments:", bg='white', font=('Helvetica', '13'), pady=5)
        self.male_L = Label(self, text="Number of Male:", bg='white', font=('Helvetica', '13'), pady=5)
        self.female_L = Label(self, text="Number of Female:", bg='white', font=('Helvetica', '13'), pady=5)
        self.balance_L = Label(self, text="Total balance:", bg='white', font=('Helvetica', '13'), pady=5)
        self.mostbusy_L = Label(self, text="Most busy Day:", bg='white', font=('Helvetica', '13'), pady=5)
        self.mostdoc_L = Label(self, text="Doctor with Most Ap:", bg='white', font=('Helvetica', '13'), pady=5)
        self.leastbusy_L = Label(self, text="Least busy Day:", bg='white', font=('Helvetica', '13'), pady=5)
        self.leastdoc_L = Label(self, text="Doctor with least Ap:", bg='white', font=('Helvetica', '13'), pady=5)

        self.number_ap = Label(self, text=self.report_data["Num_aps"], bg='white', font=('Helvetica', '11'))
        self.male = Label(self, text=self.report_data["Sex"]["Male"], bg='white', font=('Helvetica', '11'))
        self.female = Label(self, text=self.report_data[ "Sex" ][ "Female" ], bg='white', font=('Helvetica', '11'))
        self.balance = Label(self, text=f'{self.report_data[ "balance" ]}$', bg='white', font=('Helvetica', '11'))
        self.mostbusy = Label(self, text=self.report_data["busyDay"][0][0], bg='white', font=('Helvetica', '11'))
        self.leastbusy = Label(self, text=self.report_data["busyDay"][-1][0], bg='white', font=('Helvetica', '11'))
        self.mostdoc = Label(self, text=self.report_data["Doctor"][1][0], bg='white', font=('Helvetica', '11'))
        self.leastdoc = Label(self, text=self.report_data["Doctor"][-1][0], bg='white', font=('Helvetica', '11'))

        self.number_ap_L.grid(row= 0, column=0, sticky="w")
        self.number_ap.grid(row= 0, column=1)
        self.balance_L.grid(row=1, column=0, sticky="w")
        self.balance.grid(row=1, column=1)

        self.male_L.grid(row=2, column=0, sticky="w")
        self.male.grid(row=2, column=1)
        self.female_L.grid(row=3, column=0, sticky="w")
        self.female.grid(row=3, column=1)

        self.mostbusy_L.grid(row=4, column=0, sticky="w")
        self.mostbusy.grid(row=4, column=1)
        self.leastbusy_L.grid(row=5, column=0, sticky="w")
        self.leastbusy.grid(row=5, column=1)

        self.mostdoc_L.grid(row=6, column=0, sticky="w")
        self.mostdoc.grid(row=6, column=1)
        self.leastdoc_L.grid(row=7, column=0, sticky="w")
        self.leastdoc.grid(row=7, column=1)




class Checkap(ttk.Frame):
    def __init__(self, root, sql):
        self.root = root
        self.sql = sql
        super().__init__(root, width=500, height=600)


        # bg image
        self.bg_img = PIL.Image.open('../Images/bg.png')
        self.resize = self.bg_img.resize((500, 600))
        self.img = ImageTk.PhotoImage(self.resize)
        self.bg = Label(self, image=self.img)

        # label
        self.entername = Label(self, text="Enter Name ", font=('Helvetica', '14'), bg='white')

        # TreeView columns
        col = ["Fullname", "Sex", "Tel", "Doctor", "Symptoms", "Time", "Date", "Price"]
        self.table = ttk.Treeview(self, columns=col, show='headings')

        # the treeview header and column width
        self.table.heading("Fullname", text="Fullname")
        self.table.column("Fullname", width=80)

        self.table.heading("Sex", text="Sex")
        self.table.column("Sex", width=80)

        self.table.heading("Tel", text="Tel")
        self.table.column("Tel", width=80)

        self.table.heading("Doctor", text="Doctor")
        self.table.column("Doctor", width=100)

        self.table.heading("Symptoms", text="symptoms")
        self.table.column("Symptoms", width=80)

        self.table.heading("Price", text="Price")
        self.table.column("Price", width=80)

        self.table.heading("Time", text="Time")
        self.table.column("Time", width=80)

        self.table.heading("Date", text="Date")
        self.table.column("Date", width=80)

        # x axis scrollbar for table
        self.scrollbar = Scrollbar(self, orient=HORIZONTAL, command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.table.xview)

        # button
        self.checkbtn = Button(self, text="Check", command=self.checkname)
        self.Report = Button(self, text='Report', command=self.getReport)

        # inputs
        self.name_inpt = Entry(self, borderwidth=0, justify='center',
                               font=('Helvetica', '14'), highlightthickness=2,highlightcolor='#72efdd')

        # placement
        self.bg.pack()
        self.entername.place(x=20, y=50)
        self.name_inpt.place(x=20, y=80)
        self.checkbtn.place(x=250, y=80)
        self.Report.place(x=12, y=550)

    # functions
    def errormsg(self):
        messagebox.showerror('Error', "This name is not Found")

    def checkname(self):
        value = self.name_inpt.get()
        res = self.sql.getOne(value)


        if res:
            newtuple = tuple( res[x] for x in range(len(res)) if x != 0)
            self.table.insert("", END, values=newtuple)
            self.scrollbar.place(x=0, y=430, width=500)
            self.table.place(x=0, y=200, width=500)

        else:
            # if name not found send Message.
            self.errormsg()

        self.reportobj.place_forget()


    def getReport(self):
        self.reportobj = ReportFrame(root=self, sql=self.sql)
        self.table.place_forget()
        self.scrollbar.place_forget()
        self.reportobj.place(y=200, x=12)


class Ui(Tk):
    def __init__(self):
        super().__init__()
        # window
        self.title("Online Doctor Appointment")
        self.geometry('500x600')
        self.resizable(width=False ,height=False)


        # background image
        self.bg_img = PIL.Image.open('../Images/oda.png')
        self.resize = self.bg_img.resize((500, 600))
        self.img = ImageTk.PhotoImage(self.resize)
        self.bg = Label(self,image=self.img).place(x=0, y=0)

        # SQL Object
        self.sql = SQL()

        # Frame Objects
        self.createap = CreateAp(self, self.sql)
        self.checkap = Checkap(self, self.sql)


        # buttons image
        # check button
        self.check_img = PIL.Image.open('../Images/check@2x.png')
        self.checkresize = self.check_img.resize((330, 34))
        self.check = ImageTk.PhotoImage(self.checkresize)
        self.checkbtn = Button(self, image=self.check, command=self.checkfn, borderwidth=0, bg="white")

        # Create appointment button
        self.getap_img = PIL.Image.open('../Images/getap@2x.png')
        self.getapresize = self.getap_img.resize((330, 34))
        self.getap = ImageTk.PhotoImage(self.getapresize)
        self.get_ap = Button(self, image=self.getap, command=self.getap_fn, borderwidth=0, bg="white")

        # Placement
        self.checkbtn.place(x=220, y=540)
        self.get_ap.place(x=266, y=500)

    # Functions
    # packing and unpacking frames
    def checkfn(self):
        self.createap.pack_forget()
        self.checkap.pack()

    def getap_fn(self):
        self.checkap.pack_forget()
        self.createap.pack()

