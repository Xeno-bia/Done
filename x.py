#モジュール
from tkinter import *
from tkinter import filedialog as tkfd
from tkinter import messagebox as tkmb
from tkinter import ttk
from datetime import *

#ウィンドウ
w = Tk()
w.title("タイトル")
w.geometry("1000x700")

#メニューバー
mb = Menu(w)
w.config(menu=mb)

m1 = Menu(mb, tearoff=False)
mb.add_cascade(label="見出し1", menu=m1)
m1.add_command(label="項目1")
m1.add_command(label="項目2")

m2 = Menu(mb, tearoff=False)
mb.add_cascade(label="見出し2", menu=m2)
m2.add_command(label="項目1")
m2.add_command(label="項目2")

#フレーム
lf = LabelFrame(w, text="フレーム")
lf.grid(column=0, row=0)

#テキスト(1行)
l = Label(lf, text="テキスト(1行)")
l.grid(column=0, row=0)

#テキスト(複数行)
m = Message(lf, text="テキスト\n(複数行)")
m.grid(column=0, row=1)

#フォーム(1行)
e = Entry(lf)
e.grid(column=0, row=2)

e_b = Button(lf, text="入力内容表示", command=lambda: print(e.get()))
e_b.grid(column=1, row=2)

#フォーム(複数行)
t = Text(lf, width=30, height=3)
t.grid(column=0, row=3)

t_b = Button(lf, text="入力内容表示", command=lambda: print(t.get("1.0", "end")))
t_b.grid(column=1, row=3)

#チェックボックス
bv = BooleanVar()
bv.set(True)

cb = Checkbutton(lf, text="チェックボックス", variable=bv)
cb.grid(column=0, row=4)

cb_b = Button(lf, text="チェック有無表示", command=lambda: print(bv.get()))
cb_b.grid(column=1, row=4)

#ラジオボタン
iv = IntVar()
iv.set(1)

rb1 = Radiobutton(lf, text="ラジオボタン1", value=1, variable=iv)
rb1.grid(column=0, row=5)

rb2 = Radiobutton(lf, text="ラジオボタン2", value=2, variable=iv)
rb2.grid(column=0, row=6)

rb_b = Button(lf, text="選択内容表示", command=lambda: print(iv.get()))
rb_b.grid(column=1, row=6)

#ドロップダウン
sv = StringVar()
sv.set("ドロップダウン1")

om = OptionMenu(lf, sv, "ドロップダウン1", "ドロップダウン2")
om.grid(column=0, row=7)

om_b = Button(lf, text="選択内容表示", command=lambda: print(sv.get()))
om_b.grid(column=1, row=7)

# スピンボックス
varspinbox = IntVar()

sb = Spinbox(lf, from_=0, to=10, textvariable=varspinbox)
sb.grid(column=0, row=8)

sb_b = Button(lf, text="選択内容表示", command=lambda: print(varspinbox.get()))
sb_b.grid(column=1, row=8)

#スケール
scale_var = IntVar()
s = Scale(lf, variable=scale_var, orient=HORIZONTAL, length=300, from_=0, to=100, tickinterval=10)
s.grid(column=0, row=9)

#ノートブック

# ファイル
def fd():
    fp = tkfd.askopenfilename(initialdir="C:", filetypes=[("Pythonファイル", "*.py")])
    print(fp)
fd_b = Button(lf, text="ファイル選択", command=fd)
fd_b.grid(column=0, row=10)

#ダイアログ
def d():
    tkmb.showinfo("ダイアログ", "内容")
d_b = Button(lf, text="ダイアログ表示", command=d)
d_b.grid(column=0, row=11)

# 表
col_num = [1, 2]
x = [(1, "太郎"), (2, "次郎")]
tv = ttk.Treeview(lf, columns=col_num, height=len(x))

tv.column("#0", width=0, stretch="no")
tv.column(1, width=50)
tv.column(2, width=100)

tv.heading("#0", text="")
tv.heading(1, text="ID", anchor="center")
tv.heading(2, text="名前", anchor="center")

for i in range(len(x)):
    if i % 2 == 0:
        tv.insert("", "end", values=x[i])
    else:
        tv.insert("", "end", values=x[i], tags="odd")
        tv.tag_configure("odd", background="aqua")

tv.grid(column=0, row=12)

w.mainloop()
