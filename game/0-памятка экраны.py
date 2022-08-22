# Про сложные экраны типа мини-игр https://www.renpy.org/doc/html/cdd.html


# Действия: Return(True), Return(False), Notify("Message for user"), Hide("screen_name"), SetScreenVariable("n", 1), ToggleScreenVariable
# Действия описаны тут https://www.renpy.org/doc/html/screen_actions.html

# Экран с именем simple_screen
screen simple_screen():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "Это экран."
            textbutton "Ок":
                # Похоже, это то же, что и клик по диалогу
                action Return(True)


# Операторы работы со screen
show screen simple_screen

e "Первый — show screen, который показывает экран, а Ren'Py идёт дальше."
e "Экран будет показываться, пока его не спрячут."

hide screen simple_screen
e "Спрятать экран можно оператором hide screen."


# Вызов экрана и переход управления в этот экран до возврата экраном значения (например, с помощью Return)
# call screen simple_screen

# Экран с настраиваемыми параметрами
screen parameter_screen(message, okay=Return(True), cancel=Return(False)):
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "[message]"
            textbutton "Ок":
                action okay
            textbutton "Отмена":
                action cancel

show screen parameter_screen("Привет, мир.", cancel=Notify("Вы не можете это отменить."))


# Модальный экран не позволяет взаимодействовать с чем-то, кроме этого экрана
screen modal_example():
    modal True

    frame:
        xalign 0.5 ypos 50
        textbutton "Закрыть этот экран":
             action Hide("modal_example")
 
# Второй экран с тем же тегом автоматически заменит другой экран
screen a_tag_screen():
    # Тег берёт имя - то есть это имя не настраивается переменной
    tag tag_screen

    frame:
        xalign 0.33 ypos 50
        text "Тег-экран A"

screen b_tag_screen():
    tag tag_screen

    frame:
        xalign 0.66 ypos 50
        text "Тег-экран B"
 

# Наложения экранов друг на друга
# 100 будет вверху, 0 - внизу
screen zorder_100_screen():
    zorder 100
    frame:
        xalign 0.5 xoffset 50 ypos 70
        text "Zorder 100"

screen zorder_0_screen():
    frame:
        xalign 0.5 ypos 50
        text "Zorder 0"

show screen zorder_100_screen
show screen zorder_0_screen
 


# Выбор устройства
screen variant_screen():
    variant "small"
    frame:
        xalign 0.5 ypos 50
        text "Вы на маленьком устройстве."

screen variant_screen():
    frame:
        xalign 0.5 ypos 50
        text "Вы на большом устройстве."
 

# Стиль экрана
screen style_prefix_screen():
    style_prefix "red"

    frame:
        xalign 0.5 ypos 50
        text "Этот текст — красный."

style red_frame:
    background "#440000d9"

style red_text:
    color "#ffc0c0"
 
# Начальное значение переменной n
# В отличие от python-синтаксиса, n будет приравнено 1 раз за игру, в то время как в python-синтаксисе
# значение будет приравниваться каждый раз, когда показывается экран
screen default_screen():

    default n = 0

    frame:
        xalign 0.5 ypos 50
        vbox:
            text "n = [n]"
            textbutton "Увеличить" action SetScreenVariable("n", n + 1)
 

# Цикл
screen for_screen():

    $ landings = [ "Земля", "Луна", "Марс" ]

    frame:
        xalign 0.5 ypos 50

        vbox:
            for i in landings:
                textbutton "[i]" action Return(i)
 
# Аналогично можно использовать операторы if
# if flag:
#   text "Message"
#       xalign 1.0

# Отслеживание нажатия клавиш
screen on_key_screen():

    frame:
        xalign 0.5 ypos 50

        text "Теперь нажмите на английскую 'a'."

    on "show" action Notify("Только что появился экран!")

    key "a" action Notify("Вы нажали на клавишу 'a'.")
 


# Экран с параметром
screen duplicate_stats():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "Здоровье" xalign 0.5
            bar value StaticValue(90, 100) xalign 0.5 xsize 250

            null height 15

            text "Магия" xalign 0.5
            bar value StaticValue(42, 100) xalign 0.5 xsize 250


# Тот же экран, но выполненный однотипным способом с использованием вспомогательного экрана
screen using_stats():
    frame:
        xalign 0.5 ypos 50
        vbox:
            use stat("Здоровье", 90)
            null height 15
            use stat("Магия", 42)

screen stat(name, amount):

    text name xalign 0.5
    bar value StaticValue(amount, 100) xalign 0.5 xsize 250
 

# Списки экранов
# Здесь boilerplate вызывается как функция в месте вызова transclude
screen transclusion_example():

    use boilerplate():
        text "Не на что смотреть."

screen boilerplate():
    frame:
        xalign 0.5 ypos 50

        vbox:
            transclude
 

# ---------------------------------------------------------
#                    Экранные объекты
# ---------------------------------------------------------

# Выводит текст, перевёрнутый вверх ногами
screen at_example():
    frame:
        xalign 0.5 ypos 50
        text "И мир перевернулся вверх дном...":
            at rotated

transform rotated:
    rotate 180 rotate_pad False
 
# Применение стиля green_text
screen style_example():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "Закрытие дренажных клапанов." style "green_text"
            text "Наддув."
            text "Зажигание."
            text "Есть контакт!"

# Ещё один стиль, точнее, ссылка на две группы стилей с префиксом green и yellow
screen style_prefix_example():
    frame:
        xalign 0.5 ypos 50
        vbox:
            vbox:
                style_prefix "green"
                text "Закрытие дренажных клапанов."
                text "Наддув."

            vbox:
                style_prefix "yellow"
                text "Зажигание."
                text "Есть контакт!"
 
# Добавление объекта
screen add_image_example():
    frame:
        xalign 0.5 ypos 50
        add "logo base"
 
screen add_filename_example():
    frame:
        xalign 0.5 ypos 50
        add "images/logo base.png"
 
# Просто синий прямоугольник
screen add_displayable_example():
    frame:
        xalign 0.5 ypos 50
        add Solid("#0000ff", xsize=234, ysize=360)
 
screen add_at_transform_example():
    frame:
        xalign 0.5 ypos 50
        add "logo base" at unrotate

transform unrotate:
    zoom 0.7 rotate 43.21
#    linear 1.0 rotate 0



# Текст
screen text_interpolation_example():
    $ answer = 42

    frame:
        xalign 0.5 ypos 50
        text "Ответ: [answer]."
 
# Объекты располагаются в массиве в горизонтальном порядке
screen hbox_example():
    frame:
        xalign 0.5 ypos 50
        hbox:
            spacing 10
            text "1"
            text "2"
            text "3"
            text "4"
            text "5"
 
# То же, но объекты располагаются в вертикальном порядке (построчно, аналогично пунктам меню)
screen vbox_example():
    frame:
        xalign 0.5 ypos 50
        vbox:
            spacing 10
            text "1"
            text "2"
            text "3"
            text "4"
            text "5"
 
# Решётка (таблица) из объектов. 3 по горизонтали в одной строке и всего 2 строки
# Все ячейки таблицы - одинакового размера
screen grid_example():
    frame:
        xalign 0.5 ypos 50
        grid 3 2:
            spacing 10
            # transpose True - с этим таблица будет заполняться сначала не по строкам, а по столбцам
            text "1"
            text "2"
            text "3"
            text "4"
            text "5"
            null
 

# Объект показывает объекты просто путём фиксации их на пиксельных координатах
screen fixed_example():
    frame:
        xalign 0.5 ypos 50
        fixed:
            xsize 400 ysize 300
            text "1" xpos 41 ypos 184
            text "2" xpos 135 ypos 177
            text "3" xpos 92 ypos 3
            text "4" xpos 359 ypos 184
            text "5" xpos 151 ypos 25
 
# Экономия места на отступах: has hbox говорит о том, что ниже следуют элементы hbox
screen hbox_example():
    frame:
        xalign 0.5 ypos 50

        has hbox spacing 10

        text "1"
        text "2"
        text "3"
        text "4"
        text "5"

# frame создаёт фон, позволяя элементам не сливаться с фоном игровых изображений
screen frame_example():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "Это экран."
            textbutton "Ок":
                action Return(True)
 
# Кнопки
screen button_example():
    frame:
        xalign 0.5 ypos 50
        button:
            action Notify("Вы кликнули на кнопку.")
            text "Кликните на меня." style "button_text"

# Ещё кнопка
screen button_hover_example():
    frame:
        xalign 0.5 ypos 50
        button:
            action Notify("Вы кликнули на кнопку.")
            hovered Notify("Вы навелись на кнопку.")
            unhovered Notify("Вы отвелись от кнопки.")
            text "Кликните на меня." style "button_text"
 

# "Лечение"
screen button_heal_example():
    default health = 42

    frame:
        xalign 0.5 ypos 50
        button:
            action SetScreenVariable("health", 100)
            hbox:
                spacing 10
                text "Лечиться" style "button_text" yalign 0.5
                bar value AnimatedValue(health, 100, 1.0) yalign 0.5 xsize 200
 
# Кнопки-изображения
screen imagebutton_example():
    frame:
        xalign 0.5 ypos 50
        imagebutton:
            idle "logo bw"
            hover "logo base"

            action Notify("Вы кликнули на кнопку.")
 

# Кнопка имеет разный фон для idle и hover
# Проигрывает звук при наведении
screen button_inline_style_example():
    frame:
        xalign 0.5 ypos 50
        textbutton "Кликните на меня.":
            idle_background Frame("button glossy idle", 12, 12)
            hover_background Frame("button glossy hover", 12, 12)
            xpadding 20
            ypadding 10
            xmargin 5
            ymargin 5

            hover_sound "pong_beep.opus"

            text_idle_color "#c0c0c0"
            text_hover_color "#ffffff"

            action Notify("Вы кликнули на кнопку.")


# Кнопка со стилями
screen button_style_example():
    frame:
        xalign 0.5 ypos 50

        has vbox

        textbutton "Кликните на меня.":
            style "custom_button"
            action Notify("Вы кликнули на кнопку.")

        textbutton "Или на меня.":
            style "custom_button"
            action Notify("Вы кликнули на другую кнопку.")

style custom_button:
    idle_background Frame("button glossy idle", 12, 12)
    hover_background Frame("button glossy hover", 12, 12)
    xpadding 20
    ypadding 10
    xmargin 5
    ymargin 5
    size_group "custom_button"

    hover_sound "pong_beep.opus"

style custom_button_text:
    idle_color "#c0c0c0"
    hover_color "#ffffff"
 

# Полосы прогресса
# Перечень полос https://www.renpy.org/doc/html/screen_actions.html#bar-values
screen bar_example():
    frame:
        xalign 0.5 ypos 50
        xsize 500
        bar:
            value StaticValue(66, 100)

# Ещё полосы прогресса
screen bars_example():
    default n = 66

    frame:
        xalign 0.5 ypos 50
        xsize 500

        vbox:
            spacing 10

            bar value AnimatedValue(n, 100, 0.5) style ". Полоса настройки"
            bar value ScreenVariableValue("n", 100) style "slider"
            bar value ScreenVariableValue("n", 100) style "scrollbar"
 
# Верхняя заполнена на 66 из 100
# Средняя предлагает тащить за ползунок
# Нижняя также имеет ползунок (похоже, просто пошире, чем средняя)

# Вертикально расположенные полосы прогресса
screen vbars_example():
    default n = 66

    frame:
        xalign 0.5 ypos 50
        ysize 300

        hbox:
            spacing 10

            vbar value AnimatedValue(n, 100, 0.5)
            vbar value ScreenVariableValue("n", 100) style "vslider"
            vbar value ScreenVariableValue("n", 100) style "vscrollbar"
 

# Порт просмотра - предназначен для того, чтобы показывать то, что не умещается на экран
screen viewport_screen():

    viewport:
        xalign 0.5 ypos 50 xysize (700, 300)

        draggable True
        mousewheel True
        arrowkeys True

        add "bg band"
 

# Прокрутка при достижении краёв изображения курсором мышки
screen edgescroll_viewport_screen():

    viewport:
        xalign 0.5 ypos 50 xysize (700, 300)

        edgescroll (150, 500)
        mousewheel True
        arrowkeys True

        add "bg band"
 
# Имеем полосы прокрутки
screen scrollbar_viewport_screen():

    viewport:
        xalign 0.5 ypos 50 xysize (700, 300)

        scrollbars "both"
        spacing 5

        draggable True
        mousewheel True
        arrowkeys True

        add "bg band"
 

# Объекты, которые нанесены на изображение
screen volume_imagemap_example():
    imagemap:
        xalign 0.5 ypos 50
        idle "imagemap volume idle"
        hover "imagemap volume hover"
        selected_idle "imagemap volume selected_idle"
        selected_hover "imagemap volume selected_hover"
        insensitive "imagemap volume insensitive"

        hotspot (237, 171, 126, 50) action Return(True)
        hotbar (51, 96, 498, 52) value Preference("громкость музыки")

# То же, только auto работает, декларируя изображения по шаблону автоматически
screen volume_imagemap_auto_example():
    imagemap:
        xalign 0.5 ypos 50
        auto "imagemap volume %s"

        # Координаты объектов
        hotspot (237, 171, 126, 50) action Return(True)
        hotbar (51, 96, 498, 52) value Preference("громкость музыки")
 


