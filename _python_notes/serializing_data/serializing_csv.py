#!/usr/bin/env python

"""
Serializing CSV

Reading CSV
    Use csv module
    Create a reader with any iterable (e.g. file object)
    Understands Excel CSV and tab-delimited files
    Can specify alternate configuration
    Iterate through reader to get rows as lists of columns
    reader()
        To read CSV data, use the reader() method in the csv module.
        To create a reader with the default settings, use the reader() constructor.
        Pass in an iterable – typically, but not necessarily, a file object.
        You can also add parameters to control the type of quoting, or the output delimiters.

Nonstandard CSV
    Variations in how CSV data is written
    Most common alternate is for Excel
    Add parameters to reader/writer
    reader() writer()
        You can customize how the CSV parser and generator work by passing extra parameters to csv.reader() or csv.writer().
        You can change the field and row delimiters, the escape character, and for output, what level of quoting.
        You can also create a "dialect", which is a custom set of CSV parameters.
        The csv module includes one extra dialect, excel, which handles CSV files generated by Microsoft Excel.
        To use it, specify the dialect parameter:
            rdr = csv.reader(csvfile, dialect='excel')

CSV reader()/writer() Parameters
Parameter               Meaning
---------------------------------
quotechar               One-character string to use as quoting character
                        (default: '"')

delimiter               One-character string to use as field separator
                        (default: ',')

skipinitialspace        If True, skip white space after field separator
                        (default: False)

lineterminator          The character sequence which terminates rows
                        (default: depends on OS)

quoting                 When should quotes be generated when writing CSV
                        csv.QUOTE_MINIMAL – only when needed (default)
                        csv.QUOTE_ALL – quote all fields
                        csv.QUOTE_NONNUMERIC – quote all fields that are not numbers
                        csv.QUOTE_NONE – never put quotes around fields

escapechar              One-character string to escape delimiter when quoting is set to csv.QUOTE_NONE

doublequote             Control quote handling inside fields.
                        When True, two consecutive quotes are read as one, and one quote is written as two.
                        (default: True)


Using csv.DictReader
    Returns each row as dictionary
    Keys are field names
    Use header or specify
    DictReader class
        Instead of the normal reader, you can create a dictionary-based reader by using the DictReader class.
        If the CSV file has a header, it will parse the header line and use it as the field names.
        Otherwise, you can specify a list of field names with the fieldnames parameter.
        For each row, you can look up a field by name, rather than position.

Writing CSV Data
    Use csv.writer()
    Parameter is file-like object (must implement write() method)
    Can specify parameters to writer constructor
    csv.writer()
        To output data in CSV format, first create a writer using csv.writer().
        Pass in a file-like object.
    writerow() writerows()
        Use writerow() or writerows() to output CSV data
        For each row to write, call the writerow() method of the writer, passing in an iterable with the values for that row.
        To modify how data is written out, pass parameters to the writer.
    Tip
        On Windows, to prevent doublespaced output, add lineterminator='\n' when creating a CSV writer.

"""