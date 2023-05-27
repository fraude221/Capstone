import pandas as pd
import customtkinter
from tkinter import filedialog
import GraphGenerator

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        tab1 = "Graphs"
        tab2 = "Tables"

        # Configure Window
        self.title("COP Feature Extraction Tool")
        self.geometry(f"{1600}x{800}")

        # Configure Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create Sidebar Frame With Widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="COP Feature Extraction Tool",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_upload_button = customtkinter.CTkButton(self.sidebar_frame, text="Open Excel File", width=250,
                                                             height=50, command=self.upload_file)
        self.sidebar_upload_button.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Create Tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.grid_columnconfigure(0, weight=1)
        self.tabview.add(tab1)
        self.tabview.add(tab2)
        self.tabview.tab(tab1).grid_columnconfigure((0, 1), weight=1)
        self.tabview.tab(tab1).grid_rowconfigure((0, 1), weight=1)
        self.tabview.tab(tab2).grid_columnconfigure(0, weight=1)
        self.tabview.tab(tab2).grid_rowconfigure(0, weight=1)

        # Create Graph Frames
        self.tabview_graph_frame_left_up = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_left_up.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.tabview_graph_frame_left_down = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_left_down.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.tabview_graph_frame_right_up = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_right_up.grid(row=0, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew")

        # Create Scrollable Frame
        self.tabview_scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab(tab2))
        self.tabview_scrollable_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.tabview_scrollable_frame.grid_columnconfigure(1, weight=2)

        # Set Default Values
        self.appearance_mode_option_menu.set("Dark")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def upload_file(self):
        # Get File Path
        file_path = filedialog.askopenfilename(filetypes=[("Excel file", "*.xlsx")])

        # Get Data From Excel
        measurement_df = pd.read_excel(file_path, "Measurement Data")
        feature_df = pd.read_excel(file_path, "Feature Data")

        x = measurement_df['COPx']
        y = measurement_df['COPy']
        time = range(0, len(x))

        feature_labels = feature_df.columns.tolist()
        feature_values = feature_df.iloc[0].tolist()

        # Create Graphs
        GraphGenerator.generate_scatter_plot(self.tabview_graph_frame_right_up, x, y, time, 'COP Over Time Scatter Plot', 'COPx', 'COPy')
        GraphGenerator.generate_line_plot(self.tabview_graph_frame_left_up, time, x, 'Mediolateral Line Plot', 'Time', 'COPx')
        GraphGenerator.generate_line_plot(self.tabview_graph_frame_left_down, time, y, 'Anteroposterior Line Plot', 'Time', 'COPy')

        GraphGenerator.generate_tables(self.tabview_scrollable_frame, feature_labels, feature_values)


# Start the main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
