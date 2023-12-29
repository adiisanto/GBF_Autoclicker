import tkinter as tk
from tkinter import ttk
from getVisibleWindow import get_visible_windows
from getPIDFromName import get_pid_by_window_title

def Select_Click(select, active_window):
    print(active_window)
    select = get_pid_by_window_title(select)
    print(select)
    return select
if __name__ == '__main__':
    visible= get_visible_windows()

    root = tk.Tk()
    root_width = 600
    root_height = 400
    root_offset_x = int((root.winfo_screenwidth()-root_width)/2)
    root_offset_y = int((root.winfo_screenheight()-root_height)/2)
    root.geometry(f'{root_width}x{root_height}+{root_offset_x}+{root_offset_y}')
    root.title('GB Auto Tracker')

    title = ttk.Label(root, text='GB Auto Tracker')
    title.config(background='blue', foreground='white',width=600, font=('Verdana', 14), justify='center', anchor='center')
    title.pack()

    active_window_label = ttk.Label(root, text='Select Active Window')
    active_window_label.pack()

    active_window_option = get_visible_windows()

    active_window_combo = ttk.Combobox(root, values=active_window_option)
    active_window_combo.pack()

    PID = ''
    Select_button = ttk.Button(root, text='Select', command=lambda: Select_Click(PID, active_window_combo.get()))
    Select_button.pack()

    PID_label = ttk.Label(root)
    PID_label['text'] = PID
    PID_label.pack()

    root.mainloop()
