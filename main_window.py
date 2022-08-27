import json
import os
import pathlib
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from track_list_manager import tracklist_manager
import random

os.chdir(pathlib.Path(__file__).parent.absolute())

def load_tracklist_main(root):

    global tracklist_status
    global current_dict
    global num_tracks_in_tracklist
    global counter
    global track_status

    Files = [('JSON File','*.json')]
    file = askopenfile(filetypes = Files, initialdir = '/tracklists')
    if file is not None:

        temp_dict = json.loads(file.read())
        current_dict = [track_name for track_name in temp_dict if temp_dict[track_name] == 1]
        random.shuffle(current_dict)
        tracklist_status.set(f"Loaded tracklist:\n{os.path.basename(file.name)}")
        counter = 1
        num_tracks_in_tracklist = len(current_dict)
        track_status.set(value = 'Click Random Track')

def get_random_track():

    global track_status
    global num_tracks_in_tracklist
    global current_dict
    global counter

    if counter - 1 == num_tracks_in_tracklist:

        track_status.set('No more tracks!')

    else:

        track_status.set(f'Next track ({counter}\{num_tracks_in_tracklist}):\n{current_dict.pop()}')

        counter = counter + 1

def main_window():

    global tracklist_status
    global track_status
    global current_dict
    global num_tracks_in_tracklist
    global counter

    root = Tk()
    root.geometry('450x300')
    root.title('MK8D Tracklist Tool')
    root.resizable(False,False)

    tracklist_status = StringVar(value = 'No tracklist loaded')
    track_status = StringVar(value = 'No track available')
    current_dict = {}
    num_tracks_in_tracklist = 0
    counter = 1

    track_list_manager_button = Button(root, text = 'Tracklist Manager', pady = 5, padx = 5, command = tracklist_manager)
    tracklist_load_button = Button(root, text = 'Load a tracklist', pady = 5, padx = 5, command = lambda: load_tracklist_main(root))
    exit_button = Button(root, text = 'Exit the script', pady = 5, padx = 5, command = root.destroy)
    random_track = Button(root, text = 'Random Track', pady = 5, padx = 5, command = get_random_track)
    current_tracklist = Label(root, textvariable = tracklist_status, padx = 5, pady = 5, justify = CENTER, font = ('Segoe UI',8))
    current_track = Label(root, textvariable = track_status, padx = 5, pady = 5, justify = CENTER, font = ('Segoe UI',8))

    track_list_manager_button.place(x = 40, y = 250)
    tracklist_load_button.place(x = 300, y = 250)
    exit_button.place(x = 180, y = 250)
    current_tracklist.place(x = 100, y = 0, anchor = "n")
    current_track.place(x = 350, y = 0, anchor = 'n')
    random_track.place(x = 350, y = 40, anchor = "n")

    root.mainloop()

def main():
    main_window()

if __name__ == '__main__':
    main()