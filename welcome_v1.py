import easygui
import os
import PIL

# Right click on import PIl and install it to your device

combos = {
    "VALUE":
        {"Beef burger": "5.69",
         "Fries": "1.00",
         "Fizzy drink": "1.00"
         },
    "CHEEZY":
        {"Cheeseburger": "6.69",
         "Fries": "1.00",
         "Fizzy drink": "1.00"
         },
    "SUPER":
        {"Cheeseburger": "6.69",
         "Large fries": "2",
         "Smoothie": "2"
         }
}


def welcome():
    logo_image = os.environ['USERPROFILE'] + "\\Downloads\\burger logo.jpg"
    easygui.msgbox("WELCOME TO TRUMP'S BURGER TRUCK!", "Trump's burgers", image=logo_image)
    menu_choices = easygui.buttonbox("Pick one of the below options for the Burger Menu", "Burger Menu Options",
                                     choices=("View Menu", "Add Combo", "Remove Combo", "Change Combo"))


welcome()
