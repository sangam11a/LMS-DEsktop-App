# from tkinter import *
# from tkinter import ttk

# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x300')
# ws['bg']='#fb0'

# tv = ttk.Treeview(ws)
# tv['columns']=('Rank', 'Name', 'Badge')
# tv.column('#0', width=0, stretch=NO)
# tv.column('Rank', anchor=CENTER, width=80)
# tv.column('Name', anchor=CENTER, width=80)
# tv.column('Badge', anchor=CENTER, width=80)

# tv.heading('#0', text='', anchor=CENTER)
# tv.heading('Rank', text='Id', anchor=CENTER)
# tv.heading('Name', text='rank', anchor=CENTER)
# tv.heading('Badge', text='Badge', anchor=CENTER)

# # tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
# # tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
# # tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
# # tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
# # tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
# # tv.insert(parent='', index=5, iid=5, text='', values=('1','Vineet','Alpha'))
# # tv.insert(parent='', index=6, iid=6, text='', values=('2','Anil','Bravo'))
# # tv.insert(parent='', index=7, iid=7, text='', values=('3','Vinod','Charlie'))
# # tv.insert(parent='', index=8, iid=8, text='', values=('4','Vimal','Delta'))
# # tv.insert(parent='', index=9, iid=9, text='', values=('5','Manjeet','Echo'))
# # tv.insert(parent='', index=10, iid=10, text='', values=('1','Vineet','Alpha'))
# # tv.insert(parent='', index=11, iid=11, text='', values=('2','Anil','Bravo'))
# # tv.insert(parent='', index=12, iid=12, text='', values=('3','Vinod','Charlie'))
# # tv.insert(parent='', index=13, iid=13, text='', values=('4','Vimal','Delta'))
# # tv.insert(parent='', index=14, iid=14, text='', values=('5','Manjeet','Echo'))
# # tv.insert(parent='', index=15, iid=15, text='', values=('1','Vineet','Alpha'))
# # tv.insert(parent='', index=16, iid=16, text='', values=('2','Anil','Bravo'))
# # tv.insert(parent='', index=17, iid=17, text='', values=('3','Vinod','Charlie'))
# # tv.insert(parent='', index=3, iid=18, text='', values=('4','Vimal','Delta'))
# tv.pack()


# ws.mainloop()
from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title("PythonGuides")

tv = ttk.Treeview(ws, columns=(1, 2, 3), show='headings', height=8)
tv.pack()

tv.heading(1, text="name")
tv.heading(2, text="eid")
tv.heading(3, text="Salary")

def update_item():
    selected = tv.focus()
    temp = tv.item(selected, 'values')
    sal_up = float(temp[2]) + float(temp[2]) * 0.05
    tv.item(selected, values=(temp[0], temp[1], sal_up))

tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=1, iid=1, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=2, iid=2, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=3, iid=3, values=("Shanti", "e14", 22000.00))

Button(ws, text='Increment Salary', command=update_item).pack()

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()