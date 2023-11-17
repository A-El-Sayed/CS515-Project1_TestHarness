import sys
import argparse

def count_of_input(text):
    lines = text.split('\n')
    num_of_lines = len(lines)
    num_of_words = sum(len(line.split()) for line in lines)
    num_of_chars = sum(len(line) for line in lines)

    return num_of_lines, num_of_words, num_of_chars

     
def wc(files, args):
    total_lines = 0
    total_words = 0
    total_chars = 0

    for filename in files:
        try:
            with open(filename, 'r') as file:
                file_contents = file.read()
        except (FileNotFoundError, IOError) as e:
            print(f"Error: {e}")
            sys.exit[1]

        num_of_lines, num_of_words, num_of_chars = count_of_input(file_contents)

        total_lines += num_of_lines
        total_words += num_of_words
        total_chars += num_of_chars

        output = ""
        if args.lines:
            output += f"\t{num_of_lines}"
        if args.words:
            output += f"\t{num_of_words}"
        if args.characters:
            output += f"\t{num_of_chars}"
        if not args.lines and not args.characters and not args.words:
            output += f"\t{num_of_lines}\t{num_of_words}\t{num_of_chars}"
        print(f"{output} {filename}")

    if len(files) > 1:
        output_total = ""
        if args.lines:
            output_total += f"\t{total_lines}"
        if args.words:
            output_total += f"\t{total_words}"
        if args.characters:
            output_total += f"\t{total_chars}"
        if args.lines is False and args.characters is False and args.words is False:
            output_total += f"\t{total_lines}\t{total_words}\t{total_chars}"
        print(f"{output_total} total")


def main():
    parser =  argparse.ArgumentParser(description="Word Count Program")
    parser.add_argument("files", nargs="*", type=str, help="Files included")
    parser.add_argument("-l", "--lines", action = "store_true", help="Count lines only")
    parser.add_argument("-w", "--words", action = "store_true", help="Count words only")
    parser.add_argument("-c", "--characters", action = "store_true", help="Count characters only")


    args = parser.parse_args()
    wc(args.files, args)
    sys.exit(0)
if __name__ == "__main__":
    main()
