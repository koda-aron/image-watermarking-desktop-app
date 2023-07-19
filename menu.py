from panels import *


class Menu(ctk.CTkTabview):
    def __init__(self, parent, watermark_func, export_func):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.add('Watermark')
        self.add('Export')

        WatermarkFrame(self.tab('Watermark'), watermark_func)
        ExportFrame(self.tab('Export'), export_func)


class WatermarkFrame(ctk.CTkFrame):
    def __init__(self, parent, watermark_func):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        WatermarkPanel(self, watermark_func)


class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_func):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        self.name_string = ctk.StringVar()
        self.path_string = ctk.StringVar()

        FileNamePanel(self, self.name_string)
        FilePathPanel(self, self.path_string)
        ExportPanel(self, self.name_string, self.path_string, export_func)
