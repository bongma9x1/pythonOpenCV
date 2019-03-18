import tkinter as tk
import requests


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="PyMi.vn checker")
        self.label.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.entrythingy['textvariable'] = self.contents
        self.entrythingy.bind('<Key-Return>', self.check_site)

        self.hi_there = tk.Button(self)
        self.hi_there['text'] = 'Check site'
        self.hi_there['command'] = self.check_site
        self.hi_there.pack()

        self.quit = tk.Button(self, text='QUIT', command=root.destroy)
        self.quit.pack()

    def check_site(self, event=None):
        url = self.contents.get().strip() or 'https://pymi.vn'
        if not url.startswith('http'):
            url = 'http://{}'.format(url)

        resp = requests.get(url)
        print("{} response: {}".format(url, resp.status_code))


root = tk.Tk()
app = Application(master=root)
app.master.title('My checker app')
app.master.minsize(300, 200)
app.mainloop()