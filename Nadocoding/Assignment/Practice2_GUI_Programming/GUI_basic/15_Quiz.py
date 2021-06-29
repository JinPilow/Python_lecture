# Quiz) tkinter를 이용한 메모장 프로그램을 만드시오
#
# [GUI 조건]
# 1. title : 제목 없음 - Windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+400+100")

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding = "utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding = "utf8") as file:
        file.write(txt.get("1.0", END))

menu = Menu(root)
# 파일 메뉴
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "새로 만들기(N)")
menu_file.add_command(label = "새 창(W)")
menu_file.add_command(label = "열기(O)...", command = open_file)
menu_file.add_command(label = "저장(S)", command = save_file)
menu_file.add_command(label = "다른 이름으로 저장(A)...")
menu_file.add_separator()
menu_file.add_command(label = "페이지 설정(U)...")
menu_file.add_command(label = "인쇄(P)...")
menu_file.add_separator()
menu_file.add_command(label = "끝내기(X)", command = root.quit)

menu.add_cascade(label = "파일(F)", menu = menu_file)

# 편집 메뉴
menu_edit = Menu(menu, tearoff = 0)
menu_edit.add_command(label = "실행 취소(U)", state = "disable")
menu_edit.add_separator()
menu_edit.add_command(label = "잘라내기(T)", state = "disable")
menu_edit.add_command(label = "복사(C)", state = "disable")
menu_edit.add_command(label = "붙여넣기(P)")
menu_edit.add_command(label = "삭제(L)", state = "disable")
menu_edit.add_separator()
menu_edit.add_command(label = "Bing으로 검색(S)...", state = "disable")
menu_edit.add_command(label = "찾기(F)...", state = "disable")
menu_edit.add_command(label = "다음 찾기(N)", state = "disable")
menu_edit.add_command(label = "이전 찾기(V)", state = "disable")
menu_edit.add_command(label = "바꾸기(R)...")
menu_edit.add_command(label = "이동(G)...", state = "disable")
menu_edit.add_separator()
menu_edit.add_command(label = "모두 선택(A)")
menu_edit.add_command(label = "시간/날짜(D)")

menu.add_cascade(label = "편집(E)", menu = menu_edit)

# 서식 메뉴
menu_form = Menu(menu, tearoff = 0)
menu_form.add_checkbutton(label = "자동 줄 바꿈(W)")
menu_form.add_command(label = "글꼴(F)...")

menu.add_cascade(label = "서식(O)", menu = menu_form)

# 보기 메뉴
menu_view = Menu(menu, tearoff = 0)
menu_view.add_command(label = "확대하기/축소하기")
menu_view.add_checkbutton(label = "상태 표시줄(S)")

menu.add_cascade(label = "보기(V)", menu = menu_view)

# 도움말 메뉴
menu_help = Menu(menu, tearoff = 0)
menu_help.add_command(label = "도움말 보기(H)")
menu_help.add_command(label = "피드백 보내기(F)")
menu_help.add_separator()
menu_help.add_command(label = "메모장 정보(A)")

menu.add_cascade(label = "도움말(H)", menu = menu_help)


# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")

# 메모장 본문
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side = "left", fill = "both", expand = True)

scrollbar.config(command = txt.yview)

root.config(menu = menu)
root.mainloop()