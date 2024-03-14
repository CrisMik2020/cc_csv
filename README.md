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
    git clone https://github.com/your-username/csv-file-editing.git
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
