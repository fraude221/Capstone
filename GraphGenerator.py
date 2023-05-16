import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generate_scatter_plot(frame, x, y, time, title, x_label, y_label):
    # Clear grid widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create The Scatter Plot Graph
    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=time, cmap='RdBu_r', edgecolor='black', linewidths=1, alpha=0.75)
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
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Draw Graph
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="ns")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    canvas.draw()

def generate_tables(frame):
    # Define the table data and column labels
    table_data_1 = []
    col_labels_1 = ['Label', 'Value']

    for i in range(0,100):
        table_data_1.append(['Lab', 'Val'])

    # Create The Table
    fig, ax = plt.subplots()
    table = ax.table(cellText=table_data_1, colLabels=col_labels_1, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
    ax.axis('off')

    # Draw Table
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    frame.grid_columnconfigure(0, weight=1)
    canvas.draw()
