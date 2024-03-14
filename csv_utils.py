"""
File: csv_utils.py
Author: Cristian Cominelli
Date: 3/14/2024.
Description: This file contains functions for CSV file editing operations.
Dependencies: csv, typing 
"""

import csv
from typing import List
import logging
import datetime

def get_header_csv(file_csv: str, encoding: str="utf-8", delimiter: chr=';') -> List[str]:
    """
    Generates a list of strings representing the header of a CSV file.

    Args:
        file_csv (str): The path to the CSV file.
        encoding (str, optional): The encoding of the CSV file. Defaults to "utf-8".
        delimiter (chr, optional): The delimiter used in the CSV file. Defaults to ';'.
        
    Returns:
        List[str]: A list representing the header of the CSV file.
    """
    logging.info(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info("Called function: get_header_csv")
    logging.info(f"Opening file: {file_csv}")
    logging.info(f"Encoding: {encoding}")
    logging.info(f"Delimiter: {delimiter}")

    header = []

    try:
        with open(file_csv, 'r', newline='', encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            header = next(reader)
    except Exception as e:
        logging.error(f"Error reading file: {e}")

    logging.info(f"Header: {header}")
    logging.info(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info("End function: get_header_csv")

    return header

def keep_specified_columns(original_file: str, output_file: str, list_columns: List[str], encoding: str="utf-8", delimiter: str=';'):
    """
    Keep only the specified columns in a CSV file.

     Args:
        original_file (str): The path to the original CSV file.
        output_file (str): The path to the new CSV file.
        list_columns (list): A list of strings representing the columns to keep.
        encoding (str, optional): The encoding of the CSV file. Defaults to "utf-8".
        delimiter (chr, optional): The delimiter used in the CSV file. Defaults to ';'.

    Returns:
        None
    """
    logging.info(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info("Called function: keep_specified_columns")
    logging.info(f"Original file: {original_file}")
    logging.info(f"Output file: {output_file}")
    logging.info(f"Columns to keep: {list_columns}")
    logging.info(f"Encoding: {encoding}")
    logging.info(f"Delimiter: {delimiter}")

    try:
        with open(original_file, 'r', newline='', encoding=encoding) as csvfile_originale, \
                open(output_file, 'w', newline='', encoding=encoding) as csvfile_modificato:

            reader = csv.DictReader(csvfile_originale, delimiter=delimiter)
            header_modificato = [col for col in reader.fieldnames if col in list_columns]

            writer = csv.DictWriter(csvfile_modificato, fieldnames=header_modificato, delimiter=delimiter)
            writer.writeheader()

            for row in reader:
                nuova_riga = {col: row[col].replace(delimiter, f'\\{delimiter}') for col in header_modificato}
                writer.writerow(nuova_riga)
    except Exception as e:
        logging.error(f"Error processing file: {e}")

    logging.info(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info("End function: keep_specified_columns")
    print(f"New file created: {output_file}")
