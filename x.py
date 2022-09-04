#モジュール
from tkinter import *
from tkinter import filedialog as tkfd
from tkinter import messagebox as tkmb

#ウィンドウ
w = Tk()
w.title("タイトル")
w.geometry("800x400")

m = Menu(w) 

#メニューバーを画面にセット 
w.config(menu=m) 

#メニューに親メニュー（ファイル）を作成する 
menu_file = Menu(w)
m.add_cascade(label="ファイル", menu=menu_file) 

#親メニューに子メニュー（開く・閉じる）を追加する 
def open_file():
    pass
def close_disp():
    pass
menu_file.add_command(label="内容1")
menu_file.add_separator() 
menu_file.add_command(label="内容2")

#フレーム
lf = LabelFrame(w, text="フレーム")
lf.pack()

#テキスト(1行)
l = Label(lf, text="テキスト(1行)")
l.pack()

#テキスト(複数行)
m = Message(lf, text="テキスト\n(複数行)")
m.pack()

#フォーム(1行)
e = Entry(lf)
e.pack()

#フォーム(複数行)
t = Text(lf, width=30, height=3)
t.pack()

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
sb = Spinbox(lf, from_=0, to=10, increment=1, textvariable=varspinbox)
sb.pack()

# ファイル
fd = tkfd.askopenfilename(initialdir="C:", filetypes=[("○○ファイル", "*.py")])

#ダイアログ
tkmb.showinfo("ダイアログ", "内容")

#ボタン
b = Button(lf, text="ボタン", command=lambda: print("ボタン機能"))
b.pack()

w.mainloop()

#スケール
#ツリービュー
#プログレスバー
#ノートブック