#モジュール
from tkinter import *
from tkinter import filedialog as tkfd
from tkinter import messagebox as tkmb
from datetime import *

#ウィンドウ
w = Tk()
w.title("タイトル")
w.geometry("800x400")

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

e_b = Button(lf, text="表示", command=lambda: print(e.get()))
e_b.grid(column=1, row=2)

#フォーム(複数行)
t = Text(lf, width=30, height=3)
t.grid(column=0, row=3)

t_b = Button(lf, text="表示", command=lambda: print(t.get("1.0", "end")))
t_b.grid(column=1, row=3)

"""
#チェックボックス
bv = BooleanVar()
bv.set(True)
cb = Checkbutton(lf, text="チェックボックス", command=lambda: print("チェック機能"), variable=bv)
cb.pack()

#ラジオボタン
iv = IntVar()
iv.set(1)
rb1 = Radiobutton(lf, text="ラジオボタン1", command=lambda: print("ラジオ機能1"), value=1, variable=iv)
rb2 = Radiobutton(lf, text="ラジオボタン2", command=lambda: print("ラジオ機能2"), value=2, variable=iv)
rb1.pack()
rb2.pack()

#ドロップダウン
sv = StringVar()
sv.set("ドロップダウン1")
om = OptionMenu(lf, sv, "ドロップダウン1", "ドロップダウン2")
om.pack()

# スピンボックス
varspinbox = StringVar()
sb = Spinbox(lf, from_=0, to=10, textvariable=varspinbox)
sb.pack()

# ファイル
fd = tkfd.askopenfilename(initialdir="C:", filetypes=[("○○ファイル", "*.py")])

#ダイアログ
tkmb.showinfo("ダイアログ", "内容")

#ボタン
b = Button(lf, text="ボタン", command=lambda: print(e.get()))
b.pack()
"""

w.mainloop()

#スケール
#ツリービュー
#プログレスバー
#ノートブック