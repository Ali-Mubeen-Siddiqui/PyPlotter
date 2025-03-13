import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import os

def file_fetcher(filename):
    """
    Reads a file and returns a Pandas DataFrame.
    Supports CSV, XLSX, and XLSV formats.

    :param filename: Path to the file
    :return: Pandas DataFrame containing the file data
    :raises ValueError: If file format is unsupported
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    extension = os.path.splitext(filename)[1].lower()

    if extension == ".csv":
        return pd.read_csv(filename)
    elif extension in [".xlsx", ".xlsv"]:
        return pd.read_excel(filename, engine="openpyxl")  # Use openpyxl for modern Excel files
    else:
        raise ValueError("Unsupported file type. Only CSV, XLSX, and XLSV files are supported.")


def fetch_columns(data):
    return data.columns.tolist()


def cleaner(data):
    try:
        return data.fillna(0)
    except Exception as e:

        return data

def get_columns(data,X_label,Y_label):
    xcol = data[X_label]
    ycol = data[Y_label]
    return xcol,ycol


def generate_plot_map(x_axis, y_axis, x_label, y_label, title, marker, linestyle, color):
    plt.plot(x_axis, y_axis, marker=marker, linestyle=linestyle, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
