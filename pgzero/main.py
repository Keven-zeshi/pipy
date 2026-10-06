import pgzrun  # <-- Adicione isso na linha 1

# O resto do seu código continua igual aqui embaixo...
WIDTH = 800
HEIGHT = 600

heroi = Actor('heroi')
heroi.pos = (400, 300)

def draw():
    screen.clear()
    screen.fill((30, 30, 50))
    heroi.draw()

def update():
    if keyboard.left:
        heroi.x -= 5
    if keyboard.right:
        heroi.x += 5
    if keyboard.up:
        heroi.y -= 5
    if keyboard.down:
        heroi.y += 5

pgzrun.go()  # <-- Adicione isso na ÚLTIMA linha do arquivo
