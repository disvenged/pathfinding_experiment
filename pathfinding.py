# /usr/bin/python3

import tkinter as tk
root = tk.Tk()


class Grid(tk.Frame):
    def __init__(self):
        super().__init__()

        self.canvasWidth = 1080
        self.canvasHeight = 1080

        self.canvas = tk.Canvas(
            root, width=self.canvasWidth, height=self.canvasHeight)

        self.width = 20
        self.height = 20

        self.xScale = self.canvasWidth / self.width
        self.yScale = self.canvasHeight / self.height

        self.initUI()

    def initUI(self):
        self.buttons = []
        self.nodes = []
        for x in range(self.width):
            tempButtons = []
            tempNodes = []
            for y in range(self.height):
                tempButtons.append(self.canvas.create_rectangle(
                    x*self.xScale,
                    y*self.yScale,
                    (x + 1)*self.xScale,
                    (y + 1)*self.yScale,
                    fill="red", tags=f"button{x}{y}")
                )
                tempNodes.append(0)

                self.canvas.tag_bind(
                    f"button{x}{y}", "<Button-1>", self.clicked)
            self.buttons.append(tempButtons)
            self.nodes.append(tempNodes)
        self.canvas.pack()

    def clicked(self, *args):
        pos = (int(args[0].x // self.xScale), int(args[0].y // self.yScale))
        buttonId = self.buttons[pos[0]][pos[1]]
        if self.nodes[pos[0]][pos[1]] == 0:
            self.canvas.itemconfig(buttonId, fill="black")
            self.nodes[pos[0]][pos[1]] = 1
        else:
            self.canvas.itemconfig(buttonId, fill="red")
            self.nodes[pos[0]][pos[1]] = 0


if __name__ == "__main__":
    grid = Grid()
    root.mainloop()
