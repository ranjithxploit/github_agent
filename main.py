```python
import argparse

def process_to_uppercase(input_path, output_path):
    """
    Reads an input file, converts its entire content to uppercase,
    and writes the transformed content to a specified output file.
    Handles basic file I/O errors.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            file_content = infile.read()
        
        uppercase_content = file_content.upper()
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(uppercase_content)
        
        print(f"Successfully converted '{input_path}' to uppercase and saved to '{output_path}'.")
    except FileNotFoundError:
        print(f"Error: The input file '{input_path}' was not found.")
    except IOError as e:
        print(f"Error during file operation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line utility for basic text file processing.")
    subparsers = parser.add_subparsers(dest='selected_command', required=True, help='Available commands')

    # 'process' command parser
    process_parser = subparsers.add_parser('process', help='Converts the content of a text file to uppercase.')
    process_parser.add_argument('input_source_path', help='Path to the input text file for processing.')
    process_parser.add_argument('--output-destination-path', '-o', required=True, 
                                dest='output_destination_path', help='Path where the processed content will be saved.')
    
    args = parser.parse_args()

    if args.selected_command == 'process':
        process_to_uppercase(args.input_source_path, args.output_destination_path)

if __name__ == "__main__":
    main()
```