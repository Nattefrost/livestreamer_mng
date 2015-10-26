#!/usr/bin/python3
# ui to monitor your favourite livestreams
# Autumn 2015 
# Nattefrost: escande.d at gmail dot com

import livestreamer
import tkinter as tk
from tkinter import ttk
import os
import sys


ACTIVE_DIR = sys.path[0]

class Monitor:
    def __init__(self):
        """ Mostly GUI stuff"""
        self.streams_urls = self.read_streamlist()
        self.all_statuses = self.get_streams_status()
        self.root = tk.Tk()
        self.root.windowIcon = tk.PhotoImage("photo", file="./ico.png") # setting icon
        self.root.tk.call('wm','iconphoto',self.root._w,self.root.windowIcon)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.root.title("Livestreamer manager")
        self.root.geometry("600x500")
        self.frame = tk.Frame(self.root,relief=tk.FLAT,bd=4)
        self.frame.pack(fill=tk.BOTH,expand=True)
        ysb = ttk.Scrollbar(self.frame)
        ysb.pack(side=tk.RIGHT,fill=tk.Y)
        self.streams_box = tk.Listbox(self.frame, height=15,bg="#101235",relief=tk.FLAT,fg="white",font="Verdana 10 bold",selectbackground="firebrick",activestyle="underline")
        self.streams_box.pack(fill=tk.BOTH,expand=True)
        
        self.insert_streams()
        self.root.bind('<Double-Button-1>', self.launch_stream )
        self.root.bind('<Escape>', self.quit )
        self.root.bind('<Return>', self.launch_stream ) 
        self.streams_box.focus_set()
        self.root.mainloop()

    def launch_stream(self,event=None):
        """ Sending system command to launch stream"""
        selected_idx = self.streams_box.curselection()
        item = self.streams_box.get(selected_idx[0])
        self.root.withdraw()
        print("TRYING TO READ STREAM \n ===> %s " %item)
        current_stream = os.system("livestreamer {}".format(item) )
        self.root.deiconify()
        self.streams_box.focus_set()
        
    def read_streamlist(self):
        """ Reading streamlist from filesystem """
        with open("./streams.txt", 'r') as f:
            content = f.readlines()
            return content

    def get_streams_status(self):
        """ Getting all qualities for each stream url """
        data = []
        for url in self.streams_urls:
            try:
                url = url[:-1]
                options = livestreamer.streams(url)
                data.append( ["{1} {0}".format(k,url) for k,v in options.items() if k == "medium" or k=="high" or k == "best" or k=="720p" or k =="480p" or k == "680p"])
            except Warning:
                print("COULDNT LOAD {}".format(url) )
        return data
        
    def insert_streams(self):
        for cmd in self.all_statuses:
            if cmd:
                for quality in cmd:
                    self.streams_box.insert(tk.END, quality)
            
    def quit(self, event=None):
        sys.exit(0)

if __name__ == '__main__':
    app = Monitor()

