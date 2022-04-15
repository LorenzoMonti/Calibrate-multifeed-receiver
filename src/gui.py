#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Dec 17, 2021 11:46:39 AM CET  platform: Linux

import sys, os
import pkg_resources
from tkinter import Radiobutton
from tkinter.constants import DISABLED
from typing import Text
from matplotlib.pyplot import text
import ctypes

from numpy.lib.function_base import insert, select
from src import Anritsu_MS2830A as SPA
from src import Utils
from src.tabs import measure_tab, configuration_tab, connect_tab

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from src import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    
    Utils.create_home_directory()

    global val, w, root
    root = tk.Tk()
    # Simply set the theme
    root.tk.call("source", Utils.HOME_DIRECTORY + "azure.tcl")
    root.tk.call("set_theme", "light")
    top = UserInterface (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_UserInterface(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_UserInterface(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = UserInterface(w)
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_UserInterface():
    global w
    w.destroy()
    w = None

class UserInterface:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        

        top.geometry("1600x800")
        top.minsize(200, 100)
        top.maxsize(3825, 2130)
        top.resizable(1,  2)
        top.title("Multifeed receiver measure")

        #############################
        # ANRITSU CONFIGURATION
        #############################
        config_interface = Utils.read_config_file(Utils.HOME_DIRECTORY + 'config_interface.json')
        config_file = Utils.read_config_file(Utils.HOME_DIRECTORY + 'config_MS2830A.json')
        ##############################
        
        #############################
        # NOTEBOOK CREATION
        #############################
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.017, rely=0.014, relheight=0.969
                , relwidth=0.953)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        
        #############################
        # TABS CREATION
        #############################
        connect_tab.connect(self, self.TNotebook1, config_interface)
        configuration_tab.configuration(self, self.TNotebook1, config_interface, config_file)
        measure_tab.measure(self,self.TNotebook1)
        
        self.TNotebook1.tab(2, state=DISABLED)

