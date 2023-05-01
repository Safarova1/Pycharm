from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import re
from PIL import ImageTk, Image
import csv


class sdelki(Frame):

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


        def str2():
            self.master.withdraw()
            self.new_InfoWindow = Toplevel(self.master)
            self.info_window = user(self.new_InfoWindow)

        self.btn_req = Button(self.master, text='<-', fg='#F7D91E', bg='#000',
                              command=str2)
        self.btn_req.place(x=0, y=0)


        # определяем столбцы
        columns = ("marka", "nomer", "cvet",'qod','model','cena', 'fio','datav','data','denqi')

        tree = ttk.Treeview(self.master, columns=columns, show="headings")
        tree.place(x=30,y=30)


        tree.column("#1",width=120, anchor=CENTER)
        tree.column("#2",width=120,anchor=CENTER)
        tree.column("#3",width=120,anchor=CENTER)
        tree.column("#4",width=80,anchor=CENTER)
        tree.column("#5",width=80,anchor=CENTER)
        tree.column("#6",width=125,anchor=CENTER)
        tree.column("#7", width=125, anchor=CENTER)
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
                 self.qod.get(), self.model.get(), self.cena.get()))


            else:
                global count
                count = 0
                a = self.cena.get()
                b = self.data.get()
                c = self.datav.get()
                d=int(a)*(int(b)-int(c))
                print(d)

                tree.item(selected, text="", values=(self.fio.get(), self.datav.get(), self.data.get(),d))
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






        # def search():
        #     if self.nomer.get()=='' and  self.cvet.get()=='' and  self.qod.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
        #         query = self.marka.get()
        #         print(query)
        #     elif self.marka.get()=='' and  self.cvet.get()=='' and  self.qod.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
        #         query = self.nomer.get()
        #     elif self.marka.get()=='' and  self.nomer.get()=='' and  self.qod.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
        #         query = self.cvet.get()
        #     elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.model.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
        #         query = self.qod.get()
        #     elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.qod.get()=='' and  self.cena.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
        #         query = self.model.get()
        #     elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.qod.get()=='' and  self.model.get()=='' and  self.fio.get()=='' and self.datav.get()=='' and  self.data.get()=='':
        #         query = self.cena.get()
        #     elif self.marka.get()=='' and  self.nomer.get()=='' and  self.cvet.get()=='' and self.qod.get()=='' and  self.model.get()=='' and  self.cena.get()=='' and self.datav.get()=='' and  self.data.get()=='':
        #         query = self.fio.get()
        #
        #
        #
        #     selections = []
        #     for child in tree.get_children():
        #         if query in tree.item(child)['values']:
        #             print(tree.item(child)['values'])
        #             selections.append(child)
        #     print('search completed')
        #     tree.selection_set(selections)
        #
        #
        # self.poisk_button = Button(self.master, text="   Поиск   ", fg='#F7D91E', bg='#000', borderwidth=3,command=search)
        # self.poisk_button.place(x=935, y=450)





        # my_file = r"file\my_file.txt"
        #
        #
        #
        # def save_record():
        #
        #     # получаем все значения столбцов в виде отдельного списка
        #     with open(my_file, 'w',newline='') as file:
        #         csvwriter = csv.writer(file, delimiter=',')
        #         for row_id in tree.get_children():
        #             row = tree.item(row_id)['values']
        #             print('save row:', row)
        #             csvwriter.writerow(row)
        #
        # self.save_button = Button(self.master, text="   Сохранить   ", fg='#F7D91E', bg='#000', borderwidth=3,
        #                             command=save_record)
        # self.save_button.place(x=935, y=600)







if __name__ == '__main__':
    root =Tk()
    app = sdelki(root)
    app.mainloop()
