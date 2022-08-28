import json
import os
import pathlib
from tkinter import *
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
        with open('resources\\statistics.json','r') as f:
            file_data = json.loads(f.read())
        file_data['Config loaded'] += 1
        with open('resources\\statistics.json','w') as f:
            f.write(json.dumps(file_data,indent = 2))

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

        with open('resources\\statistics.json','r') as f:
            file_data = json.loads(f.read())
        file_data['Tracks loaded'] += 1
        with open('resources\\statistics.json','w') as f:
            f.write(json.dumps(file_data,indent = 2))

def statistics():

    root = Tk()
    root.geometry('400x200')
    root.title('Statistics')
    root.resizable(False,False)

    config_list = os.listdir('tracklists')
    dict_list = []
    for config in config_list:
        with open('tracklists\\'+config,'r') as f:
            dict_list.append(json.loads(f.read()))
    num_config = len(config_list)
    num_tracks = 0
    num_tracks_total = {}
    for sublist in dict_list:
        for track in sublist:
            if track in num_tracks_total:
                num_tracks_total[track] += sublist[track]
            else:
                num_tracks_total[track] = sublist[track]
            num_tracks += sublist[track]

    worst_track = min(num_tracks_total, key = num_tracks_total.get)
    best_track = max(num_tracks_total, key = num_tracks_total.get)

    with open('resources\\statistics.json','r') as f:
        config_loaded_num = json.loads(f.read())['Config loaded']
    with open('resources\\statistics.json','r') as f:
        tracks_loaded_num = json.loads(f.read())['Tracks loaded']

    label_num_configs = Label(root, text = 'Total tracklists: '+str(num_config), justify = CENTER, pady = 5, padx = 5)
    label_num_tracks = Label(root, text = 'Total tracks in tracklists: '+str(num_tracks), justify = CENTER, pady = 5, padx = 5)
    label_worst_track = Label(root, text = 'Worst track:\n'+worst_track, justify = CENTER, pady = 5, padx = 5)
    label_best_track = Label(root, text = 'Best track:\n'+best_track, justify = CENTER, pady = 5, padx = 5)
    label_loaded_config = Label(root, text = 'Loaded tracklists: '+str(config_loaded_num), justify = CENTER, pady = 5, padx = 5)
    label_loaded_track = Label(root, text = 'Loaded tracks: '+str(tracks_loaded_num), justify = CENTER, pady = 5, padx = 5)

    label_num_configs.place(x = 5, y = 5)
    label_num_tracks.place(x = 5, y = 35)
    label_loaded_config.place(x = 5, y = 65)
    label_loaded_track.place(x = 5, y = 95)
    label_worst_track.place(x = 250, y = 20)
    label_best_track.place(x = 250, y = 65)

    exit_button = Button(root, text = 'Exit', pady = 5, padx = 5, command = root.destroy)
    exit_button.place(x = 170, y = 150)

    root.mainloop()

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
    stats_button = Button(root, text = 'Statistics', pady = 5, padx = 5, command = statistics)
    random_track = Button(root, text = 'Random Track', pady = 5, padx = 5, command = get_random_track)
    current_tracklist = Label(root, textvariable = tracklist_status, padx = 5, pady = 5, justify = CENTER, font = ('Segoe UI',8))
    current_track = Label(root, textvariable = track_status, padx = 5, pady = 5, justify = CENTER, font = ('Segoe UI',8))

    track_list_manager_button.place(x = 40, y = 250)
    tracklist_load_button.place(x = 300, y = 250)
    exit_button.place(x = 180, y = 250)
    stats_button.place(x = 192, y = 200)
    current_tracklist.place(x = 100, y = 0, anchor = "n")
    current_track.place(x = 350, y = 0, anchor = 'n')
    random_track.place(x = 350, y = 40, anchor = "n")

    root.mainloop()

def main():
    main_window()

if __name__ == '__main__':
    main()