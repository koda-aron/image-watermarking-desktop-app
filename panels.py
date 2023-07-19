from tkinter import filedialog
import customtkinter as ctk
from settings import *


class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(fill='x', pady=4, ipady=8)


class WatermarkPanel(Panel):
    def __init__(self, parent, watermark_func):
        super().__init__(parent=parent)

        ctk.CTkButton(self, command=watermark_func, text='add watermark').pack(expand=True)


class FileNamePanel(Panel):
    def __init__(self, parent, name_string):
        super().__init__(parent=parent)
        self.file_name = name_string

        ctk.CTkLabel(self, text='File name').pack(expand=True)
        ctk.CTkEntry(self, textvariable=self.file_name).pack(expand=True, fill='both', padx=5, pady=5)


class FilePathPanel(Panel):
    def __init__(self, parent, path_string):
        super().__init__(parent=parent)
        self.file_path = path_string

        ctk.CTkLabel(self, text='File path').pack(expand=True)
        ctk.CTkEntry(self, textvariable=self.file_path).pack(expand=True, fill='both', padx=5, pady=5)
        ctk.CTkButton(self, text='select folder', command=self.open_file_dialog).pack(pady=5)

    def open_file_dialog(self):
        self.file_path.set(filedialog.askdirectory())


class ExportPanel(Panel):
    def __init__(self, parent, name, path, export_func):
        super().__init__(parent=parent)
        self.export = export_func
        self.name = name
        self.path = path

        ctk.CTkButton(self, text='export image', command=self.save).pack(pady=10)

    def save(self):
        self.export(self.name.get(), self.path.get())
        ctk.CTkLabel(self, text='Image Saved!', text_color=GREEN).pack(pady=10)
