import tkinter as tk
import tkinter.font as tkFont
    
app = tk.Tk()

fontStyle = tkFont.Font(size=50)

labelExample = tk.Label(app, text="1", font=fontStyle)

def increase_label_font():
    fontsize = fontStyle['size']
    labelExample['text'] = fontsize+1
    fontStyle.configure(size=fontsize+1)

def decrease_label_font():
    fontsize = fontStyle['size']
    labelExample['text'] = fontsize-1
    fontStyle.configure(size=fontsize-1)
    
buttonExample1 = tk.Button(app, text="Increase", width=20,
                          command=increase_label_font)
buttonExample2 = tk.Button(app, text="Decrease", width=30,
                          command=decrease_label_font)

buttonExample1.pack(side=tk.LEFT)
buttonExample2.pack(side=tk.LEFT)
labelExample.pack(side=tk.RIGHT)
app.mainloop()
