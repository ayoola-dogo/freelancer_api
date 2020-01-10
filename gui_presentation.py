import tkinter as tk
from tkinter import scrolledtext
from manipulation_data import output, number_projects, read_json
from projects_by_price_keyword import write_json
import re


class Note:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Note for presentation')
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        self.create_widgets()
        self.start = 0
        self.interval = 9

    def slice_obj(self, start, increment):
        _slice = slice(start, increment)
        return _slice

    def get_keyword(self):
        value = self.text_box.get(1.0, 'end')
        return value

    def search(self):
        pattern = re.compile(r'(.*)\s')
        check = self.scr.get(1.0, 'end')
        check = pattern.sub(r'\1', check)
        if not check:
            value = self.get_keyword()
            value = pattern.sub(r'\1', value)
            write_json(value)
            projects = read_json()
            number = number_projects(projects)
            self.scr.insert(tk.INSERT, '\n\n The number of projects found is {} '.format(number))
            self.project_contents = output(projects)
            self.start = 0
            self.interval = 9
        else:
            pass

    def next_write_scroll(self):
        if hasattr(self, 'project_contents'):
            r_slice = self.slice_obj(self.start, self.interval)
            content = self.project_contents[r_slice]
            self.scr.delete(1.0, 'end')
            if self.interval <= len(self.project_contents):
                for row in content:
                    self.scr.insert(tk.INSERT, row)
                    self.scr.insert(tk.INSERT, '\n')
                self.start += 10
                self.interval += 10
            else:
                self.start = 0
                self.interval = 9
        else:
            pass

    def previous_write_scroll(self):
        if hasattr(self, 'project_contents'):
            self.start -= 10
            self.interval -= 10
            p_slice = self.slice_obj(self.start, self.interval)
            self.scr.delete(1.0, 'end')
            content = self.project_contents[p_slice]
            for row in content:
                self.scr.insert(tk.INSERT, row)
                self.scr.insert(tk.INSERT, '\n')
        else:
            pass

    def clear(self):
        self.scr.delete(1.0, 'end')

    def create_widgets(self):
        scr_lf = tk.LabelFrame(self.main_frame, bg='deep sky blue')
        scr_lf.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.scr = scrolledtext.ScrolledText(scr_lf, width=90, height=27, wrap=tk.WORD, font=("Courier New", 11))
        self.scr.grid(column=0, row=0, padx=10, pady=10)
        # Button LabelFrame
        button_lf = tk.LabelFrame(self.main_frame, bg='deep sky blue')
        button_lf.pack(expand=1, fill=tk.BOTH, side=tk.BOTTOM)
        # Buttons
        self.previous = tk.Button(button_lf, text='Previous', bg='cornflower blue', font='Aerial 10 bold', width=12,
                                  command=self.previous_write_scroll)
        self.previous.grid(column=0, row=0, padx=15, pady=15)
        self.next = tk.Button(button_lf, text='Next', bg='cornflower blue', font='Aerial 10 bold', width=12,
                              command=self.next_write_scroll)
        self.next.grid(column=1, row=0, padx=15, pady=15)
        self.text_box = tk.Text(button_lf, font='Aerial 10 bold', width=30, height=2)
        self.text_box.grid(column=2, row=0, padx=30, pady=15)
        self.search_button = tk.Button(button_lf, text='Search', bg='cornflower blue', font='Aerial 10 bold', width=12,
                                       command=self.search)
        self.search_button.grid(column=3, row=0, padx=15, pady=15)
        self.clear_button = tk.Button(button_lf, text='Clear', bg='cornflower blue', font='Aerial 10 bold', width=12,
                                  command=self.clear)
        self.clear_button.grid(column=4, row=0, padx=15, pady=15)


if __name__ == '__main__':
    gui_window = Note()
    gui_window.root.mainloop()
