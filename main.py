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
        self.geometry(f"{1600}x{1000}")

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

        self.sidebar_upload_xls_button = customtkinter.CTkButton(self.sidebar_frame, text="Open Excel File", width=250,
                                                             height=50, command=self.upload_file)
        self.sidebar_upload_xls_button.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_upload_csv_button = customtkinter.CTkButton(self.sidebar_frame, text="Open CSV File", width=250,
                                                             height=50, command=self.upload_csv_file)
        self.sidebar_upload_csv_button.grid(row=2, column=0, padx=20, pady=10)

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
        self.tabview.tab(tab1).grid_rowconfigure((0, 1, 2), weight=1)
        self.tabview.tab(tab2).grid_columnconfigure(0, weight=1)
        self.tabview.tab(tab2).grid_rowconfigure(0, weight=1)

        # Create Graph Frames
        self.tabview_graph_frame_left_up = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_left_up.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.tabview_graph_frame_left_down = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_left_down.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.tabview_graph_frame_right_up = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_right_up.grid(row=0, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.tabview_graph_frame_right_down = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_right_down.grid(row=1, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.tabview_graph_frame_down = customtkinter.CTkFrame(self.tabview.tab(tab1), corner_radius=0)
        self.tabview_graph_frame_down.grid(row=2, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

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

    def upload_csv_file(self):
        # Get File Path
        file_path = filedialog.askopenfilename(filetypes=[("CSV File", "*.csv")])

        # Get Data From Excel
        try:
            df = pd.read_csv(file_path)
        except:
            return

        try:
            # Convert data to list
            x = df['COPx']
            y = df['COPy']

            # Create Graphs
            self.generate_graphs(x, y)
        except:
            try:
                # Convert data to list
                feature_labels = df.columns.tolist()
                feature_values = df.iloc[0].tolist()

                # Create Tables
                self.generate_tables(feature_labels, feature_values)
            except:
                return

    def upload_file(self):
        # Get File Path
        file_path = filedialog.askopenfilename(filetypes=[("Excel file", "*.xlsx")])

        # Get Data From Excel
        try:
            measurement_df = pd.read_excel(file_path, "Measurement Data")
            feature_df = pd.read_excel(file_path, "Feature Data")
        except:
            try:
                measurement_df = pd.read_excel(file_path)
                feature_df = None
            except:
                return

        if measurement_df is not None:
            # Convert data to list
            x = measurement_df['COPx']
            y = measurement_df['COPy']

            # Create Graphs
            self.generate_graphs(x, y)

        if feature_df is not None:
            # Convert data to list
            feature_labels = feature_df.columns.tolist()
            feature_values = feature_df.iloc[0].tolist()

            # Create Tables
            self.generate_tables(feature_labels, feature_values)

    def generate_graphs(self, x, y):
        GraphGenerator.generate_poincare_plot(self.tabview_graph_frame_right_up, x, 'COPx Poincare Plot', 'RRn', 'RRn+1')
        GraphGenerator.generate_poincare_plot(self.tabview_graph_frame_right_down, y, 'COPy Poincare Plot', 'RRn', 'RRn+1')
        GraphGenerator.generate_line_plot(self.tabview_graph_frame_left_up, GraphGenerator.get_time_values(len(x)), x, 'Mediolateral Line Plot', 'Time (sec)','COPx')
        GraphGenerator.generate_line_plot(self.tabview_graph_frame_left_down, GraphGenerator.get_time_values(len(y)), y, 'Anteroposterior Line Plot','Time (sec)', 'COPy')
        GraphGenerator.generate_scatter_plot(self.tabview_graph_frame_down, x, y, 'COP Over Time Scatter Plot', 'COPx', 'COPy')

    def generate_tables(self, feature_labels, feature_values):
        GraphGenerator.generate_tables(self.tabview_scrollable_frame, feature_labels, feature_values)

# Start the main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
