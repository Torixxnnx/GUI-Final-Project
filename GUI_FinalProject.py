"""
Program:
Author:
Descrption:
"""



from breezypythongui import EasyFrame

class HelpChoosingColors(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Help Choosing Colors Based on Room Type")
        self.addLabel(text="Select what kind of room are you choosing colors for?", row=0, column=0, columnspan=2)
        self.addButton(text="Living Room", row=1, column=0, command=self.livingRoom)
        self.addButton(text="Bedroom", row=1, column=1, command=self.bedroom)
        self.addButton(text="Kitchen", row=2, column=0, command=self.kitchen)
        self.addButton(text="Bathroom", row=2, column=1, command=self.bathroom)
        self.addButton(text="Exit", row=3, column=0, columnspan=2, command=self.quit)

    def livingRoom(self):
        self.addLabel(text="For a living room, consider...", row=4, column=0, columnspan=2)

    def bedroom(self):
        self.addLabel(text="For a bedroom, consider...", row=4, column=0, columnspan=2)

    def kitchen(self):
        self.addLabel(text="For a kitchen, consider...", row=4, column=0, columnspan=2)

    def bathroom(self):
        self.addLabel(text="For a bathroom, consider...", row=4, column=0, columnspan=2)

        self.addLabel(text="Select a specific option to get color suggestions:", row=0, column=0, columnspan=2)
        self.addButton(text="Room Size", row=1, column=0, command=self.roomSize)
        self.addButton(text="Natural Light", row=1, column=1, command=self.naturalLight)
        self.addButton(text="Desired Mood", row=2, column=0, command=self.desiredMood)

    def roomSize(self):
        self.addLabel(text="For small rooms, consider...", row=4, column=0, columnspan=2)
        self.addLabel(text="For large rooms, consider...", row=5, column=0, columnspan=2)

    def naturalLight(self):
        self.addLabel(text="For rooms with lots of natural light, consider...", row=4, column=0, columnspan=2)
        self.addLabel(text="For rooms with little natural light, consider...", row=5, column=0, columnspan=2)
    
    def desiredMood(self):
        self.addLabel(text="For a calm and relaxing mood, consider...", row=4, column=0, columnspan=2)
        self.addLabel(text="For a vibrant and energetic mood, consider...", row=5, column=0, columnspan=2)

def main():
    HelpChoosingColors().mainloop()
if __name__ == "__main__":
    main()

main()
