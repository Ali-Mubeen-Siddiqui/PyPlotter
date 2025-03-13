# Py-Plotter

**Py-Plotter** is a Python-based data visualization tool that allows users to open CSV, XLSX, and XLSV files, select columns, and generate plots with customizable styles.

## Features

- Supports CSV, XLSX, and XLSV file formats.
- User-friendly GUI built with Tkinter.
- Allows selection of X and Y axes for plotting.
- Customizable line styles, markers, and colors.
- Handles missing values by replacing them with zeros.

## Installation

### **Prerequisites**

Make sure you have Python installed (Python 3.7+ recommended).

### **Required Libraries**

Install the required dependencies using pip:

```bash
pip install pandas numpy matplotlib openpyxl
```

## Usage

1. Run the `main.py` script to launch the Py-Plotter GUI.
2. Open a CSV, XLSX, or XLSV file using the "File > Open" menu.
3. Select the desired X and Y columns.
4. Choose line styles, markers, and colors.
5. Click **"Generate"** to visualize the data.

## File Structure

```
Py-Plotter/
│── main.py          # Main application file
│── process.py       # Data processing functions
│── App.py           # GUI implementation file
│── README.md        # Project documentation
```

## Troubleshooting

- If the application does not open, ensure all dependencies are installed.
- If the plot does not generate, check that valid columns are selected.
- Only supported file formats should be used (CSV, XLSX, XLSV).

## License

This project is open-source and available under the MIT License.

## Author

**Ali Mubeen Siddiqui**

