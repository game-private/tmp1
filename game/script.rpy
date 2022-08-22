# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character(_('Эйлин'), color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    e "Вы создали новую игру Ren'Py."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    show eileen happy:
        xalign 0.0
        yalign 1.0

    show hero main:
        xalign 1.0
        yalign 1.0

    "Незнакомец" "\"AAA\""

    transform CT:
        xalign 0.25
        yalign 0.5
 
    show hero main at CT

    return
