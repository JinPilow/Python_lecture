import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Bouncing_Ball_Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\xibyu\\PycharmProjects\\Python lecture\\Nadocoding\\Assignment\\Practice1_Bouncing_Ball_Game\\pygame_basic\\background.png")

# 캐릭터(sprite) 불러오기
character = pygame.image.load("C:\\Users\\xibyu\\PycharmProjects\\Python lecture\\Nadocoding\\Assignment\\Practice1_Bouncing_Ball_Game\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 지점에 위치 (가로 위치)
character_y_pos = screen_height - character_height # 화면 세로 최하단에 위치 (세로 위치)


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생했는가?
            running = False  # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임 화면을 다시 그리기. 이 작업을 해줘야 계속해서 나타남

# pygame 종료
pygame.quit()