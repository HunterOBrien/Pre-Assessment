import easygui
import os
import PIL
import time

# Right click on import PIl and install it to your device

# Dictionary that stores the different combos available
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
    # Finds where the image is in the user's files
    logo_image = os.environ['USERPROFILE'] + "\\Downloads\\burger logo.jpg"
    # Welcome and logo
    easygui.msgbox("WELCOME TO TRUMP'S BURGER TRUCK!", "Trump's burgers", image=logo_image)
    # Displays the different options for the combos
    menu_choices = easygui.buttonbox("Pick one of the below options for the Burger Menu", "Burger Menu Options",
                                     choices=("View Menu", "Add Combo", "Remove Combo", "Change Combo", "Exit Menu"))
    # If the user wants to exit the combos menu it waits 0.75sec then goes to main menu
    if menu_choices == "Exit Menu":
        time.sleep(0.75)
        welcome()


welcome()
