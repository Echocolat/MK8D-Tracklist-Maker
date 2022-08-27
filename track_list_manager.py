import json
import os
import pathlib
from resources.get_constants import NUMBER_OF_TRACKS, TRACK_LIST_LIST
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile

os.chdir(pathlib.Path(__file__).parent.absolute())

def save_tracklist(button_list):

    track_dict = {(button_list[index][1] if button_list[index][0].instate(['selected']) else button_list[index][1]):(1 if button_list[index][0].instate(['selected']) else 0) for index in range(NUMBER_OF_TRACKS)}
    Files = [('JSON File','*.json')]
    file_pos = asksaveasfile(filetypes = Files, defaultextension = json, initialfile = 'tracklist', initialdir = '/tracklists')
    
    if file_pos is not None:
        json.dump(track_dict, file_pos, indent = 2)

def load_tracklist():

    global button_list

    Files = [('JSON File','*.json')]
    file = askopenfile(filetypes = Files, initialdir = '/tracklists')
    if file is not None:
        loaded_tracklist = json.loads(file.read())
    else:
        loaded_tracklist = []

    for index in range(len(loaded_tracklist)):

        button_list[index][0].state(['!alternate'])
        if loaded_tracklist[button_list[index][1]] == 1:
            button_list[index][0].state(['selected'])
        else:
            button_list[index][0].state(['!selected'])

def tracklist_manager():

    root = Tk()
    root.geometry('800x380')
    root.title('Tracklist Manager')
    root.resizable(False,False)
    global button_list
    button_list = []

    x_coord = 5
    for track_sublist in TRACK_LIST_LIST:
        y_coord = 5
        for track in track_sublist:
            checkbutton = ttk.Checkbutton(root, text = track)
            checkbutton.state(['!alternate'])
            checkbutton.place(x = x_coord, y = y_coord)
            button_list.append([checkbutton,track])
            y_coord = y_coord + 20
        x_coord = x_coord + 200

    save_button = Button(root, text = 'Save', pady = 5, padx = 5, command = lambda: save_tracklist(button_list))
    load_button = Button(root, text = 'Load', pady = 5, padx = 5, command = lambda: load_tracklist())
    exit_button = Button(root, text = 'Exit', pady = 5, padx = 5, command = root.destroy)

    save_button.place(x = 305, y = 335)
    load_button.place(x = 405, y = 335)
    exit_button.place(x = 358, y = 335)

    root.mainloop()

def main():
    tracklist_manager()

if __name__ == '__main__':
    main()