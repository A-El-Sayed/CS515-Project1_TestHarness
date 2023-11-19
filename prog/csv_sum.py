import sys
import csv
import argparse

def sum_columns(data, columns):
    total = {column: 0 for column in columns}

    for row in data:
        for column in columns:
            try:
                total[column] += float(row[column])
            except (ValueError, KeyError):
                print(f"Error: Unable to sum column '{column}' ")
                sys.exit(1)

    return total

def main():
    parser = argparse.ArgumentParser(description='Sum specified columns in a CSV file')
    parser.add_argument('filename', nargs="?", type=argparse.FileType('r'), default=sys.stdin, help='CSV file (default is STDIN)')
    parser.add_argument('-c', '--columns', nargs='+', required=True, type=str, help='Columns to sum (one or more column names)')
    
    args = parser.parse_args()

    try:
        if not sys.stdin.isatty():
            input_data = csv.DictReader(sys.stdin)
        else:
            input_data = csv.DictReader(args.filename)

        result = sum_columns(input_data, args.columns)

        print("Sum of specified columns:")
        for col, total in result.items():
            print(f"{col}: {total}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main()