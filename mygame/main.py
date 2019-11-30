import pygame # импортирую библиотеку pygame

# создаю функцию расчитывающую попадание
def hit(x1, y1, x2, y2, db1, db2):
    if x2 > x1 - db1 and x2 < x1 + db2 and y1 > y2 - db1 and y1 < y2 + db2:
        return 1
    else:
        return 0

pygame.init() # иницилизрую библиотеку pygame

window = pygame.display.set_mode((400, 400)) # создаю окно

background = pygame.Surface((400, 400)) # создаю переменную backgound

player = pygame.Surface ((40, 40)) # создаю переменную Игрок

target = pygame.Surface ((40, 10)) # создаю переменную Цель

arrow = pygame.Surface ((5, 10)) # создаю переменную Стрела

count = 0 # создаю переменную Счет 

player.set_colorkey(0, 0)
target.set_colorkey(0, 0)

img_background = pygame.image.load('background.png') # забираю картинку под переменную background
img_arrow = pygame.image.load('arrow.png') # забираю картинку под переменную Стрела
img_target = pygame.image.load('target.png') # забираю картинку под переменную Цель
img_player = pygame.image.load('player.png') # забираю картинку под Игрок

my_font = pygame.font.SysFont('monospace', 15) # задаю переменную отвечающую за шрифт вывода Счета

x_player = 0 # координата Игрока по оси X
y_player = 360 # координата Игорока по оси Y

x_target = 0 # координата Цели по оси X
y_target = 0 # координата Цели по оси Y

x_arrow = 1000 # координата Стрелы по оси X
y_arrow = 1000 # координата Стрелы по оси Y

done = False # логическая переменная для выхода из игры

right = True # логическая переменная для движения Цели

shoot = False # логическая переменная для Выстрела

while done == False: # создаю игровой цикл
    
    # движение Цели
    if right:
        x_target += 0.2
        if x_target > 370:
            x_target -= 0.2
            right = False
    else:
        x_target -= 0.2
        if x_target < 0:
            x_target += 0.2
            right = True

    # выход из игры по нажатию крестика    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dоne == True
        
        # действия Игрока
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s: # передвижение Игрока вниз при нажатии клавиши S
            y_player += 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w: # передвижение Игрока вверх при нажатии клавиши W
            y_player -= 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d: # передвижение Игрока вправо при нажатии клавиши D
            x_player += 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a: # передвижение Игрока влево при нажатии клавиши A
            x_player -= 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # выстрел при нажатии клавиши SPACE
            if shoot == False:
                shoot = True # Одиночный выстрел
                x_arrow = x_player + 22 # координаты появления Стрелы при Выстреле
                y_arrow = y_player - 0.5

    if shoot: # поведение Стрелы при Выстреле 
        y_arrow -= 5
        if y_arrow < 0:
            shoot = False
            y_arrow = 1000
            x_arrow = 1000
        
    if hit(x_arrow, y_arrow, x_target, y_target, 40, 10): # собыия при попадании
        count += 1
        shoot = False
        y_arrow = 1000
        x_arrow = 1000

    string = my_font.render('Очков: ' + str(count), 0, (255, 0, 0)) # задаю переменную отвечающую за ведение Счета и цвет вывода на background
    
    background.blit(img_background, (0, 0))
    arrow.blit(img_arrow, (0,0))
    target.blit(img_target, (0, 0))
    player.blit(img_player, (0, 0))
    background.blit(string, (0, 50))
    background.blit(arrow, (x_arrow, y_arrow)) # отоброжение Стрелы
    background.blit(player, (x_player, y_player)) # отоброжение Игрока на backgound
    background.blit(target, (x_target, y_target)) # отоброжение Цели на backgound
    window.blit(background, (0, 0)) # отображаю backgound на экран
    pygame.display.update()

pygame.quit()