from tkinter import *

root = Tk()
root.title("Pilow's GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode = "extended", height = 3)
# selectmode는 single과 extended / 단일선택과 복수선택의 차이
# height는 한 번에 보여지는 목록의 수, 0일 때 전부 보여짐
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # # 삭제
    # listbox.delete(END) # 맨 뒤 항목을 삭제

    # # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")
    #
    # # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목 : ", listbox.curselection())
    print("선택된 항목 : ", listbox.get(listbox.curselection()))

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop()