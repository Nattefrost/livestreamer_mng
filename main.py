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
        self.streams_urls = None
        self.all_statuses = None
        self.root = tk.Tk()
        self.root['bg'] = "#101235"
        self.root.windowIcon = tk.PhotoImage("photo", file="{}/ico.png".format(ACTIVE_DIR)) # setting icon
        self.root.tk.call('wm','iconphoto',self.root._w,self.root.windowIcon)
        self.root.title("Livestreamer manager")
        #self.root.geometry("600x500")
        # Styling config
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("custom.Horizontal.TProgressbar",  troughcolor ="VioletRed4", background='green yellow', foreground='white',thickness=18)
        # FRAMES
        self.button_frame = tk.Frame(self.root, relief=tk.RAISED,bd=7,bg="#101235")
        self.button_frame.grid(row=0,column=0,sticky=tk.W)
        self.frame = tk.Frame(self.root,relief=tk.FLAT,bg="#101235")
        self.frame.grid(row=1,column=0,columnspan=3)
        # Widgets
        self.progbar = ttk.Progressbar(self.button_frame, style="custom.Horizontal.TProgressbar",orient="horizontal", maximum=100, mode="determinate",length=100)
        self.progbar.grid(row=0,column=1,sticky=tk.W)
        self.refresh_btn = ttk.Button(self.button_frame, text="REFRESH (F5)",command=self.get_streams_status)
        self.refresh_btn.grid(row=0,column=0,sticky=tk.W)
        
        ysb = ttk.Scrollbar(self.frame)
        
        self.streams_box = tk.Listbox(self.frame, height=20,width=50,relief=tk.FLAT,fg="white",bg='#101235',font="Verdana 10 bold",selectbackground="firebrick",activestyle="underline")
        self.get_streams_status()
        
        self.root.bind('<Double-Button-1>', self.launch_stream )
        self.root.bind('<Escape>', self.quit )
        self.root.bind('<Return>', self.launch_stream )
        self.root.bind('<F5>', self.get_streams_status )
        self.streams_box.focus_set()
        ysb.pack(side=tk.RIGHT,fill=tk.Y)
        self.streams_box.pack(pady=10, anchor=tk.W,fill=tk.BOTH,expand=True)
        self.root.mainloop()
        

    def launch_stream(self,event=None):
        """ Sending system command to launch stream"""
        selected_idx = self.streams_box.curselection()
        item = self.streams_box.get(selected_idx[0])
        self.root.withdraw()
        print("##### OPENING STREAM ##### \n ===> %s " %item)
        current_stream = os.system("livestreamer {}".format(item) )
        self.root.deiconify()
        self.streams_box.focus_set()
        
    def read_streamlist(self):
        """ Reading streamlist from filesystem """
        with open("{}/streams.txt".format(ACTIVE_DIR), 'r') as f:
            content = f.readlines()
            return content

    def get_streams_status(self,event=None):
        """ Getting all qualities for each stream url """
        self.refresh_btn['state'] = 'disabled'
        self.streams_urls = self.read_streamlist()
        self.streams_box.delete(0,tk.END)
        self.progbar['value'] = 0
        self.root.update()
        size = len(self.streams_urls)
        delta = self.progbar['maximum']//size
        data = []
        for url in self.streams_urls:
            try:
                url = url[:-1] # ignore trailing space
                options = livestreamer.streams(url)
                data.append( ["{1} {0}".format(k,url) for k,v in options.items() if k == "medium" or k=="high" or k == "best" or k=="720p" or k =="480p" or k == "680p"])
                self.progbar.step(delta)
                self.root.update() # refresh display
            except:
                print("COULDNT LOAD {}".format(url) )
        self.progbar['value'] = self.progbar['maximum']
        self.all_statuses = data
        self.insert_streams()
        self.refresh_btn['state'] = 'normal'
        
    def insert_streams(self):
        for cmd in self.all_statuses:
            if cmd:
                for quality in cmd:
                    self.streams_box.insert(tk.END, quality)
            
    def quit(self, event=None):
        sys.exit(0)

if __name__ == '__main__':
    app = Monitor()

