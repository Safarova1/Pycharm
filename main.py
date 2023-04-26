from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import re
from PIL import ImageTk, Image


class LoginWindow(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master= master
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
        self.info_window = avtorizaciya(self.new_InfoWindow)






class avtorizaciya(Frame):
    def __init__(self, master1=None):
        super().__init__(master1)
        self.master1 = master1
        self.master1.title('АВТОПРОКАТ')
        self.master1.iconbitmap(default=r'icon_and_image\racing.ico')
        self.master1.config(bg='#000000')
        self.master1.geometry('1150x680+120+10')
        self.master1.resizable(False, False)
        self.create_widgit()



    def create_widgit(self):
        lbl_req = Label(self.master1, text='АВТОРИЗАЦИЯ')
        lbl_req.config(fg='#fff', bg='#000', font=('Montserrat,sans-serif;', 35))
        lbl_req.place(x=380, y=100)


        lbl_imya = Label(self.master1, text='Имя * ')
        lbl_imya.config(fg='#fff', bg='#000', font=('Bahnschrift Light',10))
        lbl_imya.place(x=380, y=200)
        self.imya = ttk.Entry(self.master1,width=58)
        self.imya.place(x=380, y=230)

        lbl_parol = Label(self.master1, text='Пароль * ')
        lbl_parol.config(fg='#fff', bg='#000', font=('Bahnschrift Light', 10))
        lbl_parol.place(x=380, y=300)
        self.parol = ttk.Entry(self.master1, show='*')
        self.parol.place(x=380, y=330)

        var = IntVar()

        def click_checkbutton():
            if var.get() == 1:
                self.parol['show'] = ''
                self.check.config(fg='#F7D91E', bg='#000')
            else:
                self.parol['show'] = '*'
                self.check.config(fg='black', bg='#fff')

        self.check = Checkbutton(self.master1, text='показать пароль', variable=var, command=click_checkbutton)
        self.check.place(x=610, y=330)

        self.btn_vxod= Button(self.master1,text='           ВХОД         ' , bg='#F7D91E', fg='black', borderwidth=10,command=self.vxod)
        self.btn_vxod.place(x=380, y=500)

        self.btn_req = Button(self.master1, text='   ЗАРЕГИСТРИРОВАТЬСЯ   ',fg='#F7D91E', bg='#000', borderwidth=10,command=self.str1)
        self.btn_req.place(x=560, y=500)



        self.error_imya = Label(self.master1, text='', foreground="yellow", background='#000', wraplength=600)
        self.error_imya.place(x=380, y=260)

        self.error_parol = Label(self.master1, text='', foreground="yellow", background='#000', wraplength=600)
        self.error_parol.place(x=380, y=360)

    def vxod(self):
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

            count = 0

            req_l = r"file\login.txt"
            req_p = r"file\password.txt"
            with open(req_l, "r") as Filel:
                login = self.imya.get()+'\n'
                password = self.parol.get()+'\n'
                for i in Filel:
                    count += 1
                    if i==login:
                        with open(req_p, "r") as Filep:
                            for i in range(0,count):
                                a=Filep.readline()
                            if a==password:
                                self.master.withdraw()
                                self.new_InfoWindow = Toplevel(self.master)
                                self.info_window = InfoWindow(self.new_InfoWindow)
                            else:
                                showinfo(title='Wrong Data', message='Wrong password or login')

                            self.imya.delete(0, END)
                            self.parol.delete(0, END)






    def str1(self):
        self.master1.withdraw()
        self.new_InfoWindow = Toplevel(self.master1)
        self.info_window = LoginWindow(self.new_InfoWindow)


class InfoWindow(Frame):
    def __init__(self, master2=None):
        super().__init__(master2)
        self.master2 = master2
        self.master2.title('АВТОПРОКАТ')
        self.master2.iconbitmap(default=r'icon_and_image\racing.ico')
        self.master2.config(bg='#000000')
        self.master2.geometry('1150x680+120+10')
        self.master2.resizable(False, False)
        self.create_widgit()



    def create_widgit(self):
        lbl_req = Label(self.master2, text='АВТОРИЗАЦИЯ')
        lbl_req.config(fg='#fff', bg='#000', font=('Montserrat,sans-serif;', 35))
        lbl_req.place(x=380, y=100)



if __name__ == '__main__':
    root =Tk()
    app = LoginWindow(root)
    app.mainloop()








