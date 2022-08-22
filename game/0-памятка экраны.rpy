return

# Экран
screen simple_screen():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "Это экран."
            textbutton "Ок":
                action Return(True)
 

