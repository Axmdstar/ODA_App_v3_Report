import pyodbc
import random

class SQL:
    def __init__(self):
        server = "IDEAPAD-FLEX-5"
        db = "Online_Doctor"

        CONNECTION = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'\
                                        'SERVER='+server+';'\
                                        'DATABASE=' +db+';'\
                                        'trusted_connection=yes')
        self.cursor = CONNECTION.cursor()

    def inserting(self, name, sex, tel, doc, sym, time, data, price):
        # generate random id
        id = random.randint(0, 10000)
        self.cursor.execute(
            "INSERT INTO online_doc_ap(ap_id,fullname,sex,tel,doctor,symptoms,aps,aps_date, price) VALUES(?,?,?,?,?,?,?,?,?)",
            (id, name, sex, tel, doc, sym, time, data, price))

        # excute statement
        self.cursor.commit()

    def getOne(self, name):
        # check if causes error
        try:
            get_name = self.cursor.execute(f"SELECT * FROM online_doc_ap WHERE fullname = '{name}'")
            return self.cursor.fetchone()
        # else
        except:
            return ""

    def __Report_sex(self):
        self.cursor.execute("select sex, COUNT(sex) as count from online_doc_ap group by sex")
        values = self.cursor.fetchall()
        return dict(values)

    def __Report_ap(self):
        self.cursor.execute("select count(*) from online_doc_ap")
        values = self.cursor.fetchall()
        return values[ 0 ][ 0 ]

    def __Report_doc(self):
        self.cursor.execute("select doctor , count(doctor) as count from online_doc_ap\
                            GROUP BY doctor\
                            order by count desc")
        values = self.cursor.fetchall()
        return values

    def __Report_balance(self):
        self.cursor.execute("select sum(price) from online_doc_ap")
        values = self.cursor.fetchall()
        return values[0][0]

    def __Report_busy_day(self):
        self.cursor.execute("select aps_date, count(aps_date) as apcount from online_doc_ap \
                            group by aps_date \
                            order by apcount desc ")
        values = self.cursor.fetchall()
        return values

    def Reports(self):

        Report_data = {"Sex": self.__Report_sex(),
                       "busyDay": self.__Report_busy_day(),
                       "Doctor": self.__Report_doc(),
                       "balance": self.__Report_balance(),
                       "Num_aps": self.__Report_ap()}
        return Report_data

