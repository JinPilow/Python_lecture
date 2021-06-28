from tkinter import *

root = Tk()
root.title("Pilow's GUI")
root.geometry("640x480")

txt = Text(root, width = 30, height = 5) # 여러줄 가능
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width = 30) # 한 줄만 가능
e.pack()
e.insert(0,"한 줄만 입력해요")


def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 처음부터 끝까지의 모든 텍스트 내용 가져오기/ "1.0" 에서 1은 라인1부터, 0은 0번째 컬럼부터 가져온다는 뜻
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop()