import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter


def generate_scatter_plot(frame, x, y, time, title, x_label, y_label):
    # Clear grid widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create The Scatter Plot Graph
    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=time, cmap='winter', alpha=0.75, s=0.75)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.colorbar(sc, shrink=0.6, label='time')

    # Draw Graph
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="ns")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    canvas.draw()


def generate_line_plot(frame, x, y, title, x_label, y_label):
    # Clear grid widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create The Line Plot Graph
    fig, ax = plt.subplots()
    ax.plot(x, y, color='black')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Draw Graph
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="ns")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    canvas.draw()


def generate_tables(frame, feature_labels, feature_values):
    # Create Header
    add_label_value_pair(frame, 0, "Label", "Value", 80, 40)

    # Create label value pairs
    for i in range(len(feature_labels)):
        add_label_value_pair(frame, i+1, feature_labels[i], feature_values[i], 50, 20)


def add_label_value_pair(frame, index, label, value, height, text_size):
    label_frame = customtkinter.CTkFrame(master=frame, corner_radius=10, border_color='white', border_width=1, height=height)
    label_frame.grid(row=index, column=0, padx=(20, 5), pady=(5, 5), sticky="ew")
    label_text = customtkinter.CTkLabel(label_frame, text=label, font=customtkinter.CTkFont(size=text_size, weight="bold"))
    label_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    value_frame = customtkinter.CTkFrame(master=frame, corner_radius=10, border_color='white', border_width=1, height=height)
    value_frame.grid(row=index, column=1, padx=(5, 20), pady=(5, 5), sticky="ew")
    value_text = customtkinter.CTkLabel(value_frame, text=value, font=customtkinter.CTkFont(size=text_size, weight="bold"))
    value_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
