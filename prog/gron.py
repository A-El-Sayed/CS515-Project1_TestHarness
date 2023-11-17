import json
import sys
import argparse


def print_gron(data,base_obj='json', indent=0, parent=""):
    if isinstance(data, dict):
        if not parent:
            print(f'{base_obj} = {{}};')
        for key, value in data.items():
            if isinstance(value, dict):
                print(f'{base_obj}.{key} = {{}};')
                print_gron(value, f'{base_obj}.{key}', indent + 1, parent=f'{base_obj}.{key}')
            elif isinstance(value, list):
                print(f'{base_obj}.{key} = [];')
                for i, item in enumerate(value):
                    print(f'{base_obj}.{key}[{i}] = {{}};')
                    print_gron(item, f'{base_obj}.{key}[{i}]', indent + 1, parent=f'{base_obj}.{key}[{i}]')
            else:
                print(f'{base_obj}.{key} = {json.dumps(value)};')


def main():
    parser =  argparse.ArgumentParser(description='Gron Flattening JSOn Program')
    # parser.add_argument('filename', nargs="?", type=argparse.FileType('r'), default = sys.stdin, help='include file (default is STD)')
    parser.add_argument('filename', type=str, help='include file (default is STD)')
    parser.add_argument('--obj', metavar='base_object', default="json", help='new base object (default is "json")')
    args = parser.parse_args()

    try:
        data = json.load(open(args.filename))
        print_gron(data, base_obj = args.obj)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    sys.exit(0)

if __name__ == '__main__':
    main()