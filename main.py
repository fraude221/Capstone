import pandas as pd
import customtkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    tab1 = "Graphs"
    tab2 = "Tables"

    # configure window
    self.title("COP Feature Extraction Tool")
    self.geometry(f"{1200}x{800}")

    # configure grid layout (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)

    # create sidebar frame with widgets
    self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(4, weight=1)

    self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="COP Feature Extraction Tool", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    self.sidebar_upload_button = customtkinter.CTkButton(self.sidebar_frame,text="Upload Excel File", width=250, height=50, command=self.upload_file)
    self.sidebar_upload_button.grid(row=1, column=0, padx=20, pady=10)

    self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
    self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"], command=self.change_appearance_mode_event)
    self.appearance_mode_option_menu.grid(row=8, column=0, padx=20, pady=(10, 20))

    # create tabview
    self.tabview = customtkinter.CTkTabview(self)
    self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
    self.tabview.grid_columnconfigure(0, weight=1)
    self.tabview.add(tab1)
    self.tabview.add(tab2)
    self.tabview.tab(tab1).grid_columnconfigure(0, weight=1)
    self.tabview.tab(tab1).grid_rowconfigure((0,1), weight=1)
    self.tabview.tab(tab2).grid_columnconfigure(0, weight=1)

    # create graph view
    self.tabview_graph_frame_up = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
    self.tabview_graph_frame_up.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

    self.tabview_graph_frame_down = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
    self.tabview_graph_frame_down.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

    # create scrollable frame
    self.tabview_scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab(tab2), height=800)
    self.tabview_scrollable_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

    # set default values
    self.appearance_mode_option_menu.set("Dark")

  def change_appearance_mode_event(self, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

  def upload_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("Excel file", "*.xlsx")])
    df = pd.read_excel(file_path)

    time = df['Time']
    x = df['COPx']
    y = df['COPy']

    self.generate_scatter_plot(x, y, time)
    self.generate_line_plot(x, y)
    self.generate_tables()

  def generate_scatter_plot(self, x, y, time):
    # Clear grid widgets
    for widget in self.tabview_graph_frame_up.winfo_children():
      widget.destroy()

    # Add the first scatter plot to the top left cell
    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=time, cmap='RdBu_r', edgecolor='black', linewidths=1, alpha=0.75)
    ax.set_title('Scatter Plot')
    ax.set_xlabel('COPx')
    ax.set_ylabel('COPy')
    fig.colorbar(sc, shrink=0.6, label='time')

    canvas = FigureCanvasTkAgg(fig, master=self.tabview_graph_frame_up)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="ns")
    self.tabview_graph_frame_up.grid_rowconfigure(0, weight=1)
    self.tabview_graph_frame_up.grid_columnconfigure(0, weight=1)
    canvas.draw()

  def generate_line_plot(self, x, y):
    # Clear grid widgets
    for widget in self.tabview_graph_frame_down.winfo_children():
      widget.destroy()

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Line Plot')

    canvas = FigureCanvasTkAgg(fig, master=self.tabview_graph_frame_down)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="ns")
    self.tabview_graph_frame_down.grid_rowconfigure(0, weight=1)
    self.tabview_graph_frame_down.grid_columnconfigure(0, weight=1)
    canvas.draw()

  def generate_tables(self):
    # Define the table data and column labels
    table_data_1 = [['Label 1', 'Value 1'], ['Label 2', 'Value 2'], ['Label 3', 'Value 3']]
    col_labels_1 = ['Label', 'Value']

    # Add the first table to the top right cell
    fig, ax = plt.subplots()
    table = ax.table(cellText=table_data_1, colLabels=col_labels_1, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
    ax.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=self.tabview_scrollable_frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    self.tabview_scrollable_frame.grid_rowconfigure(0, weight=1)
    self.tabview_scrollable_frame.grid_columnconfigure(0, weight=1)
    canvas.draw()


# Start the main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()