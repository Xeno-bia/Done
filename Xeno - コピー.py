# Tkinter
import tkinter as tk
import tkinter.scrolledtext as tksc
import tkinter.ttk as ttk

# 設定
root = tk.Tk()
root.title("タイトル")
root.geometry("1000x500")

# フレーム
frame = tk.LabelFrame(root, text="フレーム", foreground="black", labelanchor="n")
frame.pack()

# ラベル
lb = tk.Label(text="文字")
lb.pack()
lb = tk.Label(text="文字色", fg="blue")
lb.pack()
lb = tk.Label(text="背景色", bg="blue")
lb.pack()
lb = tk.Label(text="枠", relief="ridge", bd=3)
lb.pack()
lb = tk.Label(bitmap="question")
lb.pack()

# エントリー
en = tk.Entry()
en.pack()
en.focus_set()
def entry():
    x = en.get()
    print(x)
    en.delete(0, tk.END)

# テキスト
tx = tk.Text(width=50, height=5)
tx.pack()
tx.focus_set()

# スクロールテキスト
sc = tksc.ScrolledText(width=50, height=5)
sc.pack()
sc.focus_set()

# チェックボックス
boolvar = tk.BooleanVar()
def checkbutton():
    if boolvar.get():
        print("チェック済")
    else:
        print("未チェック")
ck = tk.Checkbutton(text="チェックボックス", variable=boolvar)
ck.pack()

# ラジオボタン
intvar = tk.IntVar()
intvar.set(0)
def radiobutton():
    print(intvar.get())
rb1 = tk.Radiobutton(frame, text="ラジオボタン1", value=1, variable=intvar)
rb1.pack()
rb2 = tk.Radiobutton(frame, text="ラジオボタン2", value=2, variable=intvar)
rb2.pack()

# リストボックス
strvar = tk.StringVar()
strvar.set(["A", "B", "C"])
lb = tk.Listbox(root, listvariable=strvar, selectmode="multiple", height=3)
lb.pack()
def listbox():
    print(lb.curselection())
    print(lb.get(lb.curselection()))

# コンボボックス
comb = ttk.Combobox(root, values=("A", "B", "C"))
comb.pack()
def combobox():
    print(comb.get())

# スピンボックス
varspinbox = tk.StringVar()
sb = tk.Spinbox(root, from_=0, to=10, increment=1, textvariable=varspinbox)
sb.pack()
def spinbox():
    print(varspinbox.get())

# ファイルダイアログ

# メッセージボックス

# レイアウト

# 格子配置

# キーボード取得

# ボタン
bt = tk.Button(text="ボタン", command=spinbox)
bt.pack()

# 実行
root.mainloop()

"""

タートル
入出力
分岐・ループ
四則演算
変数
ランダム
型変換
比較演算
リスト
長さ
GUI
API

"""