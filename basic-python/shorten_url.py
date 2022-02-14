import pyshorteners
import tkinter as tk

def show_url():
    url = e1.get()
    shorten_url = pyshorteners.Shortener().tinyurl.short(url)
    tk.Label(root,text="Shorten URL: ").grid(row=9, column=0, sticky=tk.W, pady=4)
    tk.Label(root,text=shorten_url).grid(row=9, column=1, sticky=tk.W, pady=4)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("URL Shortener")
    tk.Label(root, text="Enter URL Here").grid(row=0)
    e1 = tk.Entry(root,width=40)
    e1.grid(row=0, column=1)
    tk.Button(root, text='Show', command=show_url).grid(row=3, column=1, sticky=tk.W)
    tk.Button(root, text='Quit', command=quit).grid(row=6, column=1, sticky=tk.W)
    root.mainloop()
