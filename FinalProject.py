"""
Program:Help Picking a Room Color
Author:Toriahnna Caldwell
Description:This program has the user choose which type of room they are wanting to paint and then shows them information about that specific type of room and what kinds of colors it should be painted and why."
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage 


#Defining the primary class for the GUI window       
class PickingColor(EasyFrame):

    def __init__(self,):
        #Setting up the main frame
        EasyFrame.__init__(self, title="Help Picking a Room Color")
        self.setResizable(False)
        self.setSize(500, 800)

        #Label for main window at the top of the frame
        self.addLabel(text = "What kind of room are you looking to paint?", row=1, column=0, sticky="NEW", font="Cambria" )
        #Label for main window above the 2 images decribing them.
        self.addLabel(text="Here are some examples of cool, neutral, and warm colors.", row=2 , column=0, sticky="NSEW", font="Cambria")
        
        #Buttons for the room options.
        self.addButton(text="Living Room", row=5, column=0, command = self.livingroom)
        self.addButton(text="Kitchen", row=6, column=0, command = self.kitchen)
        self.addButton(text="Bedroom", row=7, column=0, command = self.bedroom)
        self.addButton(text="Bathroom", row=8, column=0, command = self.bathroom)
        self.addButton(text="Exit", row=9, column=0, command=self.quit)

        #Calling the images in the __init__
        self.image()
        self.image_cool() 


    #Image for the 3 main color types image that labels which color group is which in the photo below it
    def image_cool(self):
        imageLabel_2 = self.addLabel(text = "", row=3 ,column=0, sticky= "NSEW" )
        self.image_2 = PhotoImage(file= "cool.png")
        imageLabel_2["image"] = self.image_2


    #Image of the 3 main color types for the main window 
    def image(self):
        imageLabel_1 = self.addLabel(text = "", row=4, column=0, sticky="NSEW")
        self.image_1 = PhotoImage(file="images.png")
        imageLabel_1["image"] = self.image_1


    """ Functions for all of the room option buttons """
    #Pop up message windows for each button, that provide information on colors that work for each room.
    def livingroom(self):
        self.messageBox(message="For a versatile and inviting livingroom, consider neautral colors like white, gray, or beige.\n"
                        "For a touch of warmth, consider colors like ivory, peach, or a light beige.\n"
                        "If you prefer a more vibrant look, blue, green, or yellow can create a calming and inviting atmosphere.", title="Living Rooms")
    
    def kitchen(self):
        self.messageBox(message="For kitchens, neutral colors like white, gray, beige are timeless options.\n"
                        "However, bolder choices like blues, greens, and reds, can also work well, especially when used as accent colors like on cabinets for example.",title="Kitchens")

    def bedroom(self):
        self.messageBox(message="For a relaxing and tranquil bedroom, consider painting the walls with soft, muted colors like gentle blues, greens, and neutrals.\n"
                        "These colors are less likely to stimulate the brain and can promote a restful environment.\n"
                        "Alternatively, lighter shades of white, gray, or beige can create a clean and inviting atmosphere.", title="Bedrooms")
    
    def bathroom(self):
        self.messageBox(message="For a calming and versatile bathroom, consider painting the walls light gray, light blue, off-white, or a soft green.\n"
                        "These colors create a relaxing spa-like atmosphere and are popular choices for bathrooms.", title="Bathrooms")


#Main function that calls for the class holding all the functions.
def main():
    PickingColor().mainloop()
if __name__ == "__main__":  
    main()



#Cited Research:
#Breezy Website Tutorial:https://lambertk.academic.wlu.edu/breezypythongui/tutorial-for-breezypythongui/
#Our books breezy examples were helpful.
#W3Schools:https://www.w3schools.com/python/python_classes.asp
#https://www.w3schools.com/python/python_functions.asp
#I also got some help from the free tutor for help.. with getting my images to display in the GUI.
