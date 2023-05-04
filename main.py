import pandas as pd
import customtkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid_spec
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    tab1 = "Graphs"
    tab2 = "Tables"

    # configure window
    self.title("CustomTkinter complex_example.py")
    self.geometry(f"{1100}x{580}")

    # configure grid layout (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2), weight=1)

    # create sidebar frame with widgets
    self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(4, weight=1)
    self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="COP Feature Extraction Tool",
                                             font=customtkinter.CTkFont(size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Upload Excel File", width=250, height=50, command=self.upload_file)
    self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
    self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
    self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                   values=["Light", "Dark"],
                                                                   command=self.change_appearance_mode_event)
    self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    # create tabview
    self.tabview = customtkinter.CTkTabview(self, width=800)
    self.tabview.grid(row=0, column=1, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
    self.tabview.add(tab1)
    self.tabview.add(tab2)
    self.tabview.tab(tab1).grid_columnconfigure(0, weight=1)
    self.tabview.tab(tab2).grid_columnconfigure(0, weight=1)

    # create scrollable frame
    self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab(tab2), height=800)
    self.scrollable_frame.grid(row=0, column=0,rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
    self.scrollable_frame.grid_columnconfigure(0, weight=1)

    # set default values
    self.appearance_mode_optionemenu.set("Dark")

  def change_appearance_mode_event(self, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

  def upload_file(self):
    fig = plt.figure(constrained_layout=True)
    fig.set_size_inches(8,6)

    file_path = filedialog.askopenfilename(filetypes=[("Excel file", "*.xlsx")])
    print(file_path)
    df = pd.read_excel(file_path)

    time1 = df['Time']
    x1 = df['COPx']
    y1 = df['COPy']

    # Define the table data and column labels
    table_data_1 = [['Label 1', 'Value 1'], ['Label 2', 'Value 2'], ['Label 3', 'Value 3']]
    col_labels_1 = ['Label', 'Value']

    # Clear the previous figure and create a new 2x2 grid layout
    fig.clear()
    grid = grid_spec.GridSpec(nrows=2, ncols=1, figure=fig)
    grid2 = grid_spec.GridSpecFromSubplotSpec(nrows=1, ncols=2, subplot_spec=grid[0])

    # Add the first scatter plot to the top left cell
    ax1 = fig.add_subplot(grid2[0])
    sc = ax1.scatter(x1, y1, c=time1, cmap='RdBu_r', edgecolor='black', linewidths=1, alpha=0.75)
    ax1.set_title('Scatter Plot 1')
    ax1.set_xlabel('COPx')
    ax1.set_ylabel('COPy')

    fig.colorbar(sc, shrink=0.6, label='time')

    ax2 = fig.add_subplot(grid2[1])
    ax2.plot(x1, y1)
    ax2.set_title('Scatter Plot 2')

    # Add the first table to the top right cell
    ax3 = fig.add_subplot(grid[1])
    table1 = ax3.table(cellText=table_data_1, colLabels=col_labels_1, loc='center')
    table1.auto_set_font_size(False)
    table1.set_fontsize(12)
    table1.scale(1, 1.5)
    ax3.axis('off')

    # Redraw the canvas with the updated figure

    canvas = FigureCanvasTkAgg(fig, master=self.tabview.tab("Graphs"))
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.06, rely=0)

# Start the main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()