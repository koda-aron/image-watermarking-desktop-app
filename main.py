from image_widgets import *
from PIL import Image, ImageTk
from menu import Menu


class App(ctk.CTk):
    def __init__(self):

        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Watermarker')
        self.minsize(1000, 600)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        self.image_import = ImageImport(self, self.import_image)

        self.mainloop()

    def import_image(self, path):
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self, self.add_watermark, self.export_image)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        self.event_width = event.width
        self.event_height = event.height
        canvas_ratio = self.event_width / self.event_height
        if canvas_ratio > self.image_ratio:
            self.image_height = int(self.event_height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(self.event_width)
            self.image_height = int(self.image_width / self.image_ratio)
        self.place_image()

    def add_watermark(self):
        watermark = Image.open('images/sample_watermark.png')
        self.image.paste(watermark, (0, 0), watermark)
        self.place_image()

    def export_image(self, name, path):
        export_str = f"{path}/{name}.jpg"
        self.image.save(export_str)

    def place_image(self):
        self.image_output.delete("all")
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.event_width / 2, self.event_height / 2, image=self.image_tk)


App()
