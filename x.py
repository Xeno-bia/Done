#モジュール
from tkinter import *
from tkinter import filedialog as tkfd
from tkinter import messagebox as tkmb
from tkinter import ttk
from datetime import *

#ウィンドウ
root = Tk()
root.title("タイトル")
root.state("zoomed")

#フレーム
frame = LabelFrame(root, text="フレーム")
frame.grid(column=0, row=0, sticky="nw")

#テキスト(1行)
label = Label(frame, text="テキスト(1行)")
label.grid(column=0, row=0, sticky="nw")

#テキスト(複数行)
message = Message(frame, text="テキスト\n(複数行)")
message.grid(column=0, row=1, sticky="nw")

#フォーム(1行)
entry = Entry(frame)
entry.grid(column=0, row=2, sticky="nw")

#フォーム(複数行)
text = Text(frame, width=30, height=3)
text.grid(column=0, row=3, sticky="nw")

#チェックボックス
check_var = BooleanVar()

checkbutton = Checkbutton(frame, text="チェックボックス", variable=check_var)
checkbutton.grid(column=0, row=4, sticky="nw")

#ラジオボタン
radio_var = StringVar()
radio_var.set("ラジオボタン1")

radiobutton1 = Radiobutton(frame, text="ラジオボタン1", value="ラジオボタン1", variable=radio_var)
radiobutton1.grid(column=0, row=5, sticky="nw")

radiobutton2 = Radiobutton(frame, text="ラジオボタン2", value="ラジオボタン2", variable=radio_var)
radiobutton2.grid(column=0, row=6, sticky="nw")

#ドロップダウン
option_var = StringVar()

optionmenu = OptionMenu(frame, option_var, "ドロップダウン1", "ドロップダウン2")
optionmenu.grid(column=0, row=7, sticky="nw")

#スピンボックス
spin_var = IntVar()

spinbox = Spinbox(frame, from_=0, to=100, textvariable=spin_var)
spinbox.grid(column=0, row=8, sticky="nw")

#スケール
scale_var = IntVar()

scale = Scale(frame, variable=scale_var, orient=HORIZONTAL, length=300, from_=0, to=100, tickinterval=10)
scale.grid(column=0, row=9, sticky="nw")

#ファイル
file_var = StringVar()

def filedialog():
    file_var.set(tkfd.askopenfilename(initialdir="C:", filetypes=[("Pythonファイル", "*.py")]))

file_button = Button(frame, text="ファイル選択", command=filedialog)
file_button.grid(column=0, row=10, sticky="nw")

#ダイアログ
def dialog():
    tkmb.showinfo("タイトル", "内容")

dialog_button = Button(frame, text="ダイアログ表示", command=dialog)
dialog_button.grid(column=0, row=11, sticky="nw")

#表
treeview = ttk.Treeview(frame, columns=[1, 2])

treeview.column("#0", width=0, stretch="no")
treeview.column(1, width=30)
treeview.column(2, width=200)

treeview.heading("#0", text="")
treeview.heading(1, text="ID", anchor="center")
treeview.heading(2, text="名前", anchor="center")

x = [
    (1, "太郎"),
    (2, "次郎")
]

for i in range(len(x)):
    if i % 2 == 0:
        treeview.insert("", "end", values=x[i])
    else:
        treeview.insert("", "end", values=x[i], tags="odd")
        treeview.tag_configure("odd", background="aqua")

treeview.grid(column=0, row=12, sticky="nw")

def action():
    datas = [entry.get(), text.get("1.0", "end"), check_var.get(), radio_var.get(), option_var.get(), spin_var.get(), scale_var.get(), file_var.get()]
    for data in datas:
        print(data)

    """
    act_label = Label(root, text=)
    act_label.grid(column=0, row=)
    """

button = Button(root, text="表示", command=action)
button.grid(column=1, row=0, sticky="sw")

root.mainloop()
