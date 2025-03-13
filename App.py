import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from process import file_fetcher, fetch_columns, get_columns, cleaner, generate_plot_map

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Py-Plotter')
        self.geometry('700x500')
        self.configure(bg='#f4f4f4')

        self.file = None  # Stores selected file path
        self.data = None  # Stores fetched data

        self.create_widgets()

    def create_widgets(self):
        self.create_nav()
        self.build_labels()
        self.file_label = ttk.Label(self, text="No file selected", foreground="gray")
        self.file_label.pack(pady=5)
        self.selector_frame = ttk.Frame(self)
        self.selector_frame.pack(pady=10)

        self.plot_config()
        self.build_text()
        self.generate_button()

    def create_nav(self):
        nav = tk.Menu(self)
        file_menu = tk.Menu(nav, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_file_view)
        nav.add_cascade(menu=file_menu, label='File')
        self.config(menu=nav)

    def open_file(self):
        file_name = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xlsv")])
        if not file_name:
            return None  # No file selected

        extension = os.path.splitext(file_name)[1]
        if extension not in ['.csv', '.xlsv', '.xlsx']:
            messagebox.showerror('Error', 'Invalid file type. Only CSV, XLSX, and XLSV files are supported.')
            return None
        return file_name

    def open_file_view(self):
        file = self.open_file()
        if file:
            self.file = file
            self.file_label.config(text=f"Loaded: {os.path.basename(file)}", foreground="black")

            try:
                self.data = file_fetcher(file)
                self.selectors_build()
            except Exception as e:
                messagebox.showerror('Error', f'Error fetching data: {str(e)}')

    def build_labels(self):
        head = ttk.Label(self, text="Open a CSV, XLSX, or XLSV file to visualize", font=("Arial", 12, "bold"))
        head.pack(pady=10)

    def selectors_build(self):
        for widget in self.selector_frame.winfo_children():
            widget.destroy()

        columns = fetch_columns(self.data)
        if not columns:
            messagebox.showerror("Error", "No columns found in the file.")
            return

        ttk.Label(self.selector_frame, text="Select X-Axis:").pack(anchor="w")
        self.selected_x_opt = tk.StringVar()
        ttk.Combobox(self.selector_frame, textvariable=self.selected_x_opt, values=columns).pack(pady=5, fill='x')

        ttk.Label(self.selector_frame, text="Select Y-Axis:").pack(anchor="w")
        self.selected_y_opt = tk.StringVar()
        ttk.Combobox(self.selector_frame, textvariable=self.selected_y_opt, values=columns).pack(pady=5, fill='x')

    def plot_config(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10)

        styles = ['-', '--', '-.', ':']
        markers = ['o', 'v', '^', '<', '>', 's', 'p', '*', '+', 'x', 'D', '|', '_']
        colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

        ttk.Label(frame, text="Line Style:").grid(row=0, column=0, padx=5, pady=2)
        self.selected_style = tk.StringVar()
        ttk.Combobox(frame, textvariable=self.selected_style, values=styles).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Marker:").grid(row=1, column=0, padx=5, pady=2)
        self.selected_marker = tk.StringVar()
        ttk.Combobox(frame, textvariable=self.selected_marker, values=markers).grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Color:").grid(row=2, column=0, padx=5, pady=2)
        self.selected_color = tk.StringVar()
        ttk.Combobox(frame, textvariable=self.selected_color, values=colors).grid(row=2, column=1, padx=5, pady=2)

    def build_text(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10)

        ttk.Label(frame, text="X-Axis Label:").grid(row=0, column=0, padx=5, pady=2)
        self.x_legend_value = tk.StringVar()
        ttk.Entry(frame, textvariable=self.x_legend_value).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Y-Axis Label:").grid(row=1, column=0, padx=5, pady=2)
        self.y_legend_value = tk.StringVar()
        ttk.Entry(frame, textvariable=self.y_legend_value).grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Plot Title:").grid(row=2, column=0, padx=5, pady=2)
        self.title_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.title_var).grid(row=2, column=1, padx=5, pady=2)

    def generate_button(self):
        ttk.Button(self, text="Generate Plot", command=self.generate_plot).pack(pady=10)

    def generate_plot(self):
        try:
            if not self.file:
                messagebox.showerror('Error', 'No file selected!')
                return

            self.data = cleaner(self.data)
            self.x_axis, self.y_axis = get_columns(self.data, self.selected_x_opt.get(), self.selected_y_opt.get())

            if self.x_axis.empty or self.y_axis.empty:
                messagebox.showerror('Error', 'Please select valid X and Y axes.')
                return

            generate_plot_map(self.x_axis, self.y_axis, self.x_legend_value.get(), self.y_legend_value.get(),
                              self.title_var.get(), self.selected_marker.get(), self.selected_style.get(),
                              self.selected_color.get())

            messagebox.showinfo('Success', 'Plot generated successfully!')
        except Exception as e:
            messagebox.showerror('Error', f'Error processing data check you have filled all fields:')