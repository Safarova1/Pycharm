from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import re
from PIL import ImageTk, Image
import csv


class LoginWindow(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.master.title('АВТОПРОКАТ')
        self.master.iconbitmap(default=r'icon_and_image\racing.ico')
        self.master.config(bg = '#000000')
        self.master.geometry('1150x680+120+10')
        self.master.resizable(False,False)
        self.create_widgets()


    def create_widgets(self):


        image = Image.open(r"icon_and_image\a.jpg")
        resize_image = image.resize((1160, 690))
        img = ImageTk.PhotoImage(resize_image)

        label1 = Label(image=img)
        label1.image = img
        label1.pack()

        lbl_nazvaniye = Label(self.master, text='АРЕНДА АВТО')
        lbl_nazvaniye.config(fg='#F7D91E', bg='#000', font=('Segoe UI Black', 40))
        lbl_nazvaniye.place(x=60, y=80)

        lbl_vopros = Label(self.master, text='У вас уже есть аккаунт?')
        lbl_vopros.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        lbl_vopros.place(x=60, y=150)

        self.btn_avtorizaciya = Button(self.master, text='   АВТОРИЗАЦИЯ   ', bg='#F7D91E', fg='black', borderwidth=5, command=self.avtorizaciya)
        self.btn_avtorizaciya.place(x=60, y=180)






        lbl_req =Label(self.master, text='РЕГИСТРАЦИЯ')
        lbl_req.config(fg='#fff', bg='#000', font=('Montserrat,sans-serif;', 35))
        lbl_req.place(x=740, y=20)



        lbl_fam = Label(self.master,text= 'Фамилия  ')
        lbl_fam.config(fg='#fff', bg='#000', font=('Bahnschrift Light',10))
        lbl_fam.place(x=750, y=100)
        self.fam = ttk.Entry(self.master)
        self.fam.place(x=750, y=130)



        lbl_imya = Label(self.master, text='Имя * ')
        lbl_imya.config(fg='#fff', bg='#000', font=('Bahnschrift Light',10))
        lbl_imya.place(x=960, y=100)
        self.imya = ttk.Entry(self.master)
        self.imya.place(x=960, y=130)



        lbl_tel = Label(self.master, text='Телефон  ')
        lbl_tel.config(fg='#fff', bg='#000', font=('Bahnschrift Light',10))
        lbl_tel.place(x=750, y=200)

        def is_valid(newval):
            result = re.match("^\+{0,1}\d{0,12}$", newval) is not None
            if not result and len(newval) <= 12:
                errmsg.set("Номер телефона должен быть в формате +994xxxxxxxxx")
            else:
                errmsg.set("")
            return result

        errmsg = StringVar()
        check = (self.master.register(is_valid), "%P")

        self.tel = ttk.Entry(self.master,validate="key", validatecommand=check,width=55)
        self.tel.place(x=750, y=230)

        error_tel = ttk.Label(self.master, foreground="yellow",background='#000' ,textvariable=errmsg, wraplength=600)
        error_tel.place(x=750, y=260)



        lbl_email = Label(self.master, text='Email * ')
        lbl_email.config(fg='#fff', bg='#000', font=('Bahnschrift Light',10))
        lbl_email.place(x=750, y=300)
        self.email = ttk.Entry(self.master,width=55)
        self.email.place(x=750, y=330)


        lbl_parol = Label(self.master, text='Пароль * ')
        lbl_parol.config(fg='#fff', bg='#000', font=('Bahnschrift Light',10))
        lbl_parol.place(x=750, y=400)
        self.parol = ttk.Entry(self.master, show='*')
        self.parol.place(x=750, y=430)

        var = IntVar()

        def click_checkbutton():
            if var.get() == 1:
                self.parol['show'] = ''
                self.check.config(fg='#F7D91E', bg='#000')
            else:
                self.parol['show'] = '*'
                self.check.config(fg='black', bg='#fff')

        self.check = Checkbutton(self.master, text='показать пароль', variable=var,command=click_checkbutton)
        self.check.place(x=965, y=430)



        self.btn_req =Button(self.master, text='   ЗАРЕГИСТРИРОВАТЬСЯ   ', bg='#F7D91E', fg='black', borderwidth = 10,  command=self.req)
        self.btn_req.place(x=850, y=500)

        self.error_imya = Label(self.master, text='', foreground="yellow",background='#000', wraplength=150)
        self.error_imya.place(x=960, y=160)

        self.error_email = Label(self.master, text='', foreground="yellow", background='#000', wraplength=600)
        self.error_email.place(x=750, y=360)

        self.error_parol = Label(self.master, text='', foreground="yellow",background='#000', wraplength=600)
        self.error_parol.place(x=750, y=460)
    def req(self):
        a=1
        b=1
        c=1
        if self.imya.get() =='':
            self.error_imya['text'] ='Поле Имя обязательно для заполнения'
            a+=1
        else:
            self.error_imya['text']=''
            a=0

        if self.email.get() =='':
            self.error_email['text'] = 'Поле Email обязательно для заполнения'
            b+=1
        else:
            self.error_email['text']=''
            b=0

        if self.parol.get() =='':
            self.error_parol['text'] = 'Поле Пароль обязательно для заполнения'
            c+=1
        else:
            self.error_parol['text']=''
            c=0

        if a==0 and b==0 and c==0:
            req_login = r"file\login.txt"
            req_password = r"file\password.txt"
            with open(req_login, "a") as File:
                File.write(self.imya.get())
                File.write('\n')

            with open(req_password, "a") as File:
                File.write(self.parol.get())
                File.write('\n')




            self.btn_req.config(fg='#F7D91E', bg='#000')
            z = 'имя- ' + self.imya.get()+','+'фамилия- '+ self.fam.get()+ ','+'телефон- '+self.tel.get()+','+'почта- '+self.email.get()+','+ 'пароль- '+self.parol.get()+"\n"

            my_file_path = r"file\avtoprokat.txt"


            with open(my_file_path, "a") as File:
                File.write(z)
                File.write('\n')

            self.imya.delete(0, END)
            self.fam.delete(0, END)
            self.tel.delete(0, END)
            self.email.delete(0, END)
            self.parol.delete(0, END)

    def avtorizaciya(self):
        self.master.withdraw()
        self.new_InfoWindow = Toplevel(self.master)
        self.info_window = Avtorizaciya(self.new_InfoWindow)


class Avtorizaciya(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('АВТОПРОКАТ')
        self.master.iconbitmap(default=r'icon_and_image\racing.ico')
        self.master.config(bg='#000000')
        self.master.geometry('1150x680+120+10')
        self.master.resizable(False, False)
        self.create_widgets()



    def create_widgets(self):

        lbl_req = Label(self.master, text='АВТОРИЗАЦИЯ')
        lbl_req.config(fg='#fff', bg='#000', font=('Montserrat,sans-serif;', 35))
        lbl_req.place(x=380, y=100)


        lbl_imya = Label(self.master, text='Имя * ')
        lbl_imya.config(fg='#fff', bg='#000', font=('Bahnschrift Light',10))
        lbl_imya.place(x=380, y=200)
        self.imya = ttk.Entry(self.master,width=58)
        self.imya.place(x=380, y=230)

        lbl_parol = Label(self.master, text='Пароль * ')
        lbl_parol.config(fg='#fff', bg='#000', font=('Bahnschrift Light', 10))
        lbl_parol.place(x=380, y=300)
        self.parol = ttk.Entry(self.master, show='*')
        self.parol.place(x=380, y=330)

        var = IntVar()

        def click_checkbutton():
            if var.get() == 1:
                self.parol['show'] = ''
                self.check.config(fg='#F7D91E', bg='#000')
            else:
                self.parol['show'] = '*'
                self.check.config(fg='black', bg='#fff')

        self.check = Checkbutton(self.master, text='показать пароль', variable=var, command=click_checkbutton)
        self.check.place(x=610, y=330)



        self.error_imya = Label(self.master, text='', foreground="yellow", background='#000', wraplength=600)
        self.error_imya.place(x=380, y=260)

        self.error_parol = Label(self.master, text='', foreground="yellow", background='#000', wraplength=600)
        self.error_parol.place(x=380, y=360)


        def vxod():
            a = 1
            c = 1
            if self.imya.get() == '':
                self.error_imya['text'] = 'Поле Имя обязательно для заполнения'
                a += 1
            else:
                self.error_imya['text'] = ''
                a = 0


            if self.parol.get() == '':
                self.error_parol['text'] = 'Поле Пароль обязательно для заполнения'
                c += 1
            else:
                self.error_parol['text'] = ''
                c = 0

            if a == 0 and c == 0:
                self.btn_req.config(fg='black', bg='#F7D91E')

                self.count = 0

            req_l = r"file\login.txt"
            req_p = r"file\password.txt"
            with open(req_l, "r") as Filel:
                login = self.imya.get()+'\n'
                password = self.parol.get()+'\n'
                for i in Filel:
                    self.count += 1
                    if i==login:
                        with open(req_p, "r") as Filep:
                            for i in range(0,self.count):
                                a=Filep.readline()
                            if a==password:
                                self.master.withdraw()
                                self.new_InfoWindow = Toplevel(self.master)
                                self.info_window = InfoWindow(self.new_InfoWindow)

                                self.imya.delete(0, END)
                                self.parol.delete(0, END)
                            else:

                                showinfo(title='Неверные данные', message='Неправильный пароль')

                    else:
                        showinfo(title='Неверные данные', message='Неправильное имя пользователя или пароль')
                        self.imya.delete(0, END)
                        self.parol.delete(0, END)


        self.btn_req = Button(self.master, text='        ВХОД       ', bg='#F7D91E', fg='black', borderwidth=10,
                              command=vxod)
        self.btn_req.place(x=380, y=500)



        def str1():
            self.master.withdraw()
            self.new_InfoWindow = Toplevel(self.master)
            self.info_window = LoginWindow(self.new_InfoWindow)





        self.btn_req = Button(self.master, text='   ЗАРЕГИСТРИРОВАТЬСЯ   ', fg='#F7D91E', bg='#000', borderwidth=10,
                              command=str1)
        self.btn_req.place(x=560, y=500)


class InfoWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('АВТОПРОКАТ')
        self.master.iconbitmap(default=r'icon_and_image\racing.ico')
        self.master.config(bg='#000000')
        self.master.geometry('1150x680+120+10')
        self.master.resizable(False, False)
        self.create_widgit()



    def create_widgit(self):
        lbl_req = Label(self.master, text='hello')
        lbl_req.config(fg='#fff', bg='#000', font=('Montserrat,sans-serif;', 35))
        lbl_req.place(x=380, y=100)
        def str1():
            self.master.withdraw()
            self.new_InfoWindow = Toplevel(self.master)
            self.info_window = dobavit_delete(self.new_InfoWindow)

        self.btn_req = Button(self.master, text='   dobavit_delete   ', fg='#F7D91E', bg='#000', borderwidth=10,
                              command=str1)
        self.btn_req.place(x=560, y=500)


        def str2():
            self.master.withdraw()
            self.new_InfoWindow = Toplevel(self.master)
            self.info_window = pokaz(self.new_InfoWindow)

        self.btn_req = Button(self.master, text='   pokaz   ', fg='#F7D91E', bg='#000', borderwidth=10,
                              command=str2)
        self.btn_req.place(x=399, y=500)


class dobavit_delete(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('АВТОПРОКАТ')
        self.master.iconbitmap(default=r'icon_and_image\racing.ico')
        self.master.config(bg='#000000')
        self.master.geometry('1150x680+120+10')
        self.master.resizable(False, False)
        self.create_widgit()



    def create_widgit(self):




        # self.btn_req = Button(self.master2, text='   Добавить сделку   ', fg='#F7D91E', bg='#000', borderwidth=3)
        # self.btn_req.place(x=350, y=525)





        # определяем столбцы
        columns = ("marka", "nomer", "cvet",'qod','model','cena', 'fio','datav','data','denqi')

        tree = ttk.Treeview(self.master, columns=columns, show="headings")
        tree.place(x=30,y=30)


        tree.column("#1",width=120, anchor=CENTER)
        tree.column("#2",width=120,anchor=CENTER)
        tree.column("#3",width=120,anchor=CENTER)
        tree.column("#4",width=80,anchor=CENTER)
        tree.column("#5",width=80,anchor=CENTER)
        tree.column("#6",width=130,anchor=CENTER)
        tree.column("#7", width=120, anchor=CENTER)
        tree.column("#8", width=120, anchor=CENTER)
        tree.column("#9", width=120, anchor=CENTER)
        tree.column("#10", width=85, anchor=CENTER)


        # определяем заголовки
        tree.heading("marka", text="Марка автомобиля")
        tree.heading("nomer", text="Номер автомобиля")
        tree.heading("cvet", text="Цвет автомобиля")
        tree.heading("qod", text="Год выпуска")
        tree.heading("model", text="Модель")
        tree.heading("cena", text="Цена проката в сутки")
        tree.heading("fio", text="ФИО того, кто взял")
        tree.heading("datav", text="Дата, когда взяли")
        tree.heading("data", text="Дата, когда вернут")
        tree.heading("denqi", text="Общая цена")

        # определяем данные для отображения
        cars = []

        global count
        count = 0
        # добавляем данные
        for car in cars:
            tree.insert(parent='', index='end', iid=count, text='', values=(car[0], car[1], car[2], car[3], car[4], car[5],car[6],car[7],car[8],car[9]))

            count += 1


        marka = Label(self.master, text='Марка автомобиля')
        marka.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        marka.place(x=40, y=400)
        self.marka = ttk.Entry(self.master, width=22)
        self.marka.place(x=30, y=430)

        nomer = Label(self.master, text='Номер автомобиля')
        nomer.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        nomer.place(x=182, y=400)
        self.nomer = ttk.Entry(self.master, width=25)
        self.nomer.place(x=162, y=430)

        cvet = Label(self.master, text='Цвет автомобиля')
        cvet.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        cvet.place(x=335, y=400)
        self.cvet = ttk.Entry(self.master, width=25)
        self.cvet.place(x=315, y=430)

        qod = Label(self.master, text='Год выпуска')
        qod.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        qod.place(x=500, y=400)
        self.qod = ttk.Entry(self.master, width=22)
        self.qod.place(x=470, y=430)

        model = Label(self.master, text='Модель')
        model.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        model.place(x=628, y=400)
        self.model = ttk.Entry(self.master, width=23)
        self.model.place(x=600, y=430)


        cena = Label(self.master, text='Цена проката в сутки')
        cena.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        cena.place(x=730, y=400)
        self.cena = ttk.Entry(self.master, width=25)
        self.cena.place(x=720, y=430)

        fio = Label(self.master, text='ФИО того, кто взял')
        fio.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        fio.place(x=40, y=500)
        self.fio = ttk.Entry(self.master, width=22)
        self.fio.place(x=30, y=530)

        datav = Label(self.master, text='Дата, когда взяли')
        datav.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        datav.place(x=182, y=500)
        self.datav = ttk.Entry(self.master, width=25)
        self.datav.place(x=162, y=530)

        data = Label(self.master, text='Дата, когда вернут')
        data.config(fg='#F7D91E', bg='#000', font=('Montserrat,sans-serif;', 10))
        data.place(x=335, y=500)
        self.data = ttk.Entry(self.master, width=25)
        self.data.place(x=315, y=530)



        def input_record():

            if self.data.get()=='':
                tree.insert(parent='', index='end', text='',
                            values=(
                            self.marka.get(), self.nomer.get(), self.cvet.get(), self.qod.get(), self.model.get(),
                            self.cena.get()))

            else:
                global count
                count = 0
                a = self.cena.get()
                b = self.data.get()
                c = self.datav.get()
                d=int(a)*(int(b)-int(c))
                print(d)

                tree.insert(parent='', index='end', iid=count, text='',
                               values=(self.marka.get(), self.nomer.get(), self.cvet.get(),self.qod.get(),self.model.get(),self.cena.get(),self.fio.get(),self.datav.get(),self.data.get(),d))
                count += 1

            self.marka.delete(0, END)
            self.nomer.delete(0, END)
            self.cvet.delete(0, END)
            self.qod.delete(0, END)
            self.model.delete(0, END)
            self.cena.delete(0, END)
            self.fio.delete(0, END)
            self.datav.delete(0, END)
            self.data.delete(0, END)


        self.btn_req = Button(self.master, text='   Добавить информацию   ', fg='#F7D91E', bg='#000', borderwidth=3,command=input_record)
        self.btn_req.place(x=935, y=300)

        def select_record():
            # clear entry boxes
            self.marka.delete(0, END)
            self.nomer.delete(0, END)
            self.cvet.delete(0, END)
            self.qod.delete(0, END)
            self.model.delete(0, END)
            self.cena.delete(0, END)
            self.fio.delete(0, END)
            self.datav.delete(0, END)
            self.data.delete(0, END)


            # grab record
            selected = tree.focus()
            # grab record values
            values = tree.item(selected, 'values')
            # temp_label.config(text=selected)

            # output to entry boxes
            self.marka.insert(0, values[0])
            self.nomer.insert(0, values[1])
            self.cvet.insert(0, values[2])
            self.qod.insert(0, values[3])
            self.model.insert(0, values[4])
            self.cena.insert(0, values[5])
            self.fio.insert(0, values[6])
            self.datav.insert(0, values[7])
            self.data.insert(0, values[8])



        self.select_button = Button(self.master, text="   Выбрать информацию   ", fg='#F7D91E', bg='#000', borderwidth=3,command=select_record)
        self.select_button.place(x=935, y=350)

        def update_record():
            selected = tree.focus()
            if self.data.get()=='':
                tree.item(selected, text="", values=(
                self.marka.get(), self.nomer.get(), self.cvet.get(), self.qod.get(), self.model.get(), self.cena.get()))


            else:
                global count
                count = 0
                a = self.cena.get()
                b = self.data.get()
                c = self.datav.get()
                d=int(a)*(int(b)-int(c))
                print(d)

                tree.item(selected, text="", values=(
                self.marka.get(), self.nomer.get(), self.cvet.get(), self.qod.get(), self.model.get(), self.cena.get(),
                self.fio.get(), self.datav.get(), self.data.get(),d))
                count += 1




            # save new data

            # clear entry boxes
            self.marka.delete(0, END)
            self.nomer.delete(0, END)
            self.cvet.delete(0, END)
            self.qod.delete(0, END)
            self.model.delete(0, END)
            self.cena.delete(0, END)
            self.fio.delete(0, END)
            self.datav.delete(0, END)
            self.data.delete(0, END)


        self.edit_button = Button(self.master, text="   Изменить   ", fg='#F7D91E', bg='#000', borderwidth=3,
                                  command=update_record)
        self.edit_button.place(x=935, y=400)






        def search():
            if self.nomer.get()=='' and  self.cvet.get()=='' and  self.qod.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
                query = self.marka.get()
                print(query)
            elif self.marka.get()=='' and  self.cvet.get()=='' and  self.qod.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
                query = self.nomer.get()
            elif self.marka.get()=='' and  self.nomer.get()=='' and  self.qod.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
                query = self.cvet.get()
            elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
                query = self.qod.get()
            elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.qod.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
                query = self.model.get()
            elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.qod.get()=='' and  self.model.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
                query = self.cena.get()
            elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.qod.get()=='' and  self.model.get()=='' and  self.cena.get()=='' and self.datav.get()=='' and  self.data.get()=='':
                query = self.fio.get()



            selections = []
            for child in tree.get_children():
                if query in tree.item(child)['values']:
                    print(tree.item(child)['values'])
                    selections.append(child)
            print('search completed')
            tree.selection_set(selections)


        self.poisk_button = Button(self.master, text="   Поиск   ", fg='#F7D91E', bg='#000', borderwidth=3,command=search)
        self.poisk_button.place(x=935, y=450)






        def delete_record():
            item = tree.selection()[0]
            tree.delete(item)



        self.delete_button = Button(self.master, text="   Удалить   ", fg='#F7D91E', bg='#000', borderwidth=3, command=delete_record)
        self.delete_button.place(x=935, y=500)
        my_file = r"file\my_file.txt"

        def load_record():
            with open(my_file) as file:
                csvread = csv.reader(file, delimiter=',')

                for row in csvread:
                    print('load row:', row)
                    tree.insert("", 'end', values=row)

        self.load_button = Button(self.master, text="   Обновить   ", fg='#F7D91E', bg='#000', borderwidth=3,
                                  command=load_record)
        self.load_button.place(x=935, y=550)

        def save_record():

            # получаем все значения столбцов в виде отдельного списка
            with open(my_file, 'w',newline='') as file:
                csvwriter = csv.writer(file, delimiter=',')
                for row_id in tree.get_children():
                    row = tree.item(row_id)['values']
                    print('save row:', row)
                    csvwriter.writerow(row)

        self.save_button = Button(self.master, text="   Сохранить   ", fg='#F7D91E', bg='#000', borderwidth=3,
                                    command=save_record)
        self.save_button.place(x=935, y=600)


class pokaz(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('АВТОПРОКАТ')
        self.master.iconbitmap(default=r'icon_and_image\racing.ico')
        self.master.config(bg='#000000')
        self.master.geometry('1150x680+120+10')
        self.master.resizable(False, False)
        self.create_widgit()

    def create_widgit(self):

        # определяем столбцы
        columns = ("marka", "nomer", "cvet",'qod','model','cena', 'fio','datav','data','denqi')

        tree = ttk.Treeview(self.master, columns=columns, show="headings", height=29)
        tree.place(x=30,y=30)


        tree.column("#1",width=120, anchor=CENTER)
        tree.column("#2",width=120,anchor=CENTER)
        tree.column("#3",width=120,anchor=CENTER)
        tree.column("#4",width=80,anchor=CENTER)
        tree.column("#5",width=80,anchor=CENTER)
        tree.column("#6",width=130,anchor=CENTER)
        tree.column("#7", width=120, anchor=CENTER)
        tree.column("#8", width=120, anchor=CENTER)
        tree.column("#9", width=120, anchor=CENTER)
        tree.column("#10", width=85, anchor=CENTER)


        # определяем заголовки
        tree.heading("marka", text="Марка автомобиля")
        tree.heading("nomer", text="Номер автомобиля")
        tree.heading("cvet", text="Цвет автомобиля")
        tree.heading("qod", text="Год выпуска")
        tree.heading("model", text="Модель")
        tree.heading("cena", text="Цена проката в сутки")
        tree.heading("fio", text="ФИО того, кто взял")
        tree.heading("datav", text="Дата, когда взяли")
        tree.heading("data", text="Дата, когда вернут")
        tree.heading("denqi", text="Общая цена")

        # определяем данные для отображения
        cars = []

        global count
        count = 0
        # добавляем данные
        for car in cars:
            tree.insert(parent='', index='end', iid=count, text='', values=(car[0], car[1], car[2], car[3], car[4], car[5],car[6],car[7],car[8],car[9]))

            count += 1




        my_file = r"file\my_file.txt"

        with open(my_file) as file:
            csvread = csv.reader(file, delimiter=',')

            for row in csvread:
                print('load row:', row)
                tree.insert("", 'end', values=row)



if __name__ == '__main__':
    root =Tk()
    app = LoginWindow(root)
    app.mainloop()








