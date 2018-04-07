"""
Python data analysis Week 3 assignment

"""
import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    table_field = []
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        table_field = next(csvreader)
    return(table_field)

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    dict_list = []
    with open(filename, "rt", newline='') as csvfile:
        csvreader=csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            dict_list.append(row)
    return dict_list

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    dict_d = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader=csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            dict_d[row[keyfield]] = row
    return dict_d
def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, "wt", newline='') as csvfile:
        csvwriter=csv.DictWriter(csvfile, delimiter=separator, quotechar=quote,
                                quoting=csv.QUOTE_NONNUMERIC, fieldnames = fieldnames)
        csvwriter.writeheader()
        for row in table:
            csvwriter.writerow(row)
