# cc_csv
# CSV File Editing Operations

## Overview
This repository contains Python functions for editing CSV files. The provided functions allow users to extract headers from CSV files and keep only specified columns in a new CSV file. This README provides an overview of the functions available and instructions on how to use them.

## Dependencies
- Python 3.x
- `csv` module
- `typing` module

## Installation
1. Clone this repository to your local machine:
    ```
    git clone https://github.com/CrisMik2020/cc_csv
    ```
2. Navigate to the project directory:
    ```
    cd csv-file-editing
    ```

## Usage
### 1. `get_header_csv`
This function retrieves the header of a CSV file and returns it as a list of strings.

#### Arguments
- `file_csv`: Path to the CSV file.
- `encoding` (optional): Encoding of the CSV file. Default is "utf-8".
- `delimiter` (optional): Delimiter used in the CSV file. Default is ",".

#### Example
```python
from csv_utils import get_header_csv

header = get_header_csv("example.csv")
print(header)
```

## Usage
### 1. `keep_specified_columns`
The `keep_specified_columns` function is part of the CSV File Editing Operations project. This function creates a new CSV file with only the specified columns from the original CSV file. It is particularly useful when you need to extract specific data columns from a large dataset or perform data filtering operations.

## Usage
### Arguments
- `original_file`: Path to the original CSV file.
- `new_file`: Path to the new CSV file to be created.
- `list_columns`: List of strings representing the columns to keep.
- `encoding` (optional): Encoding of the CSV files. Default is "utf-8".
- `delimiter` (optional): Delimiter used in the CSV files. Default is ",".

### Example
```python
from csv_utils import keep_specified_columns

# Keep only "Name" and "Age" columns from the original.csv file
keep_specified_columns("original.csv", "new.csv", ["Name", "Age"])
```
