import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter
import numpy as np


def generate_poincare_plot(frame, values, title, x_label, y_label):
    # Clear grid widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Make frame fit to grid
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    interval_list = create_interval_list(values)
    x_values = get_odd_index_values(interval_list)
    y_values = get_even_index_values(interval_list)

    if len(y_values) > len(x_values):
        y_values.pop()

    # Create The Scatter Plot Graph
    fig, ax = plt.subplots()
    sc = ax.scatter(x_values, y_values, c=get_time_values(len(x_values)), cmap='winter', alpha=0.75, s=0.75)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.colorbar(sc, shrink=0.6, label='Time (sec)')

    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.85, top=0.85)

    # Draw Graph
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    canvas.draw()


def create_interval_list(input_list):
    interval_list = []
    for i in range(1, len(input_list)):
        difference = input_list[i] - input_list[i - 1]
        interval_list.append(difference)
    return interval_list


def get_odd_index_values(input_list):
    new_list = []
    for i in range(len(input_list)):
        if i % 2 == 1:  # Check if the index is odd
            new_list.append(input_list[i])
    return new_list


def get_even_index_values(input_list):
    new_list = []
    for i in range(len(input_list)):
        if i % 2 == 0:  # Check if the index is even
            new_list.append(input_list[i])
    return new_list


def generate_scatter_plot(frame, x, y, title, x_label, y_label):
    # Clear grid widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Make frame fit to grid
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Create The Scatter Plot Graph
    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=get_time_values(len(x)), cmap='winter', alpha=0.75, s=0.75)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.colorbar(sc, shrink=0.6, label='Time (sec)')

    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.85, top=0.85)

    # Draw Graph
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    canvas.draw()


def generate_line_plot(frame, x, y, title, x_label, y_label):
    # Clear grid widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Make frame fit to grid
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Create The Line Plot Graph
    fig, ax = plt.subplots()
    ax.plot(x, y, color='black')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.85, top=0.85)

    # Draw Graph
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
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


def get_time_values(max_value):
    seq_list = range(max_value)
    time_list = [num * 0.001 for num in seq_list]
    return time_list
