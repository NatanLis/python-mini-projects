import csv
import json
import os

# Function to convert csv to json
def csv_to_json(file_name): 
    with open(file_name , 'r') as csv_file:
        csv_data=csv.DictReader(csv_file)
        data_list=[row for row in csv_data]
        json_data = json.dumps(data_list, indent=4)

        json_name = file_name[:-4]
    with open(f'{json_name}.json','w') as json_file:
        json_file.write(json_data)

def print_centered(text):
    # color text in red
    red_start = "\033[31m"
    reset = "\033[0m"
    # Get the terminal size
    rows, columns = os.popen('stty size', 'r').read().split()
    # Convert string dimensions to integers
    rows = int(rows)
    columns = int(columns)
    # Calculate the starting column to center the text
    start_col = (columns - len(text)) // 4
    # Print the text starting from the calculated column
    print(f"❗️" * start_col + " " + red_start + text.upper() + reset + " " + "❗️" * start_col)

def help():
    print_centered("warning")
    print("To converter to work fille to convert should be in the same directory what main program \n")
    print("Give name of a file to concert from csv to json format:")

# main function
def main():
    help()
    file_name=input()
    csv_to_json(file_name)

# if __name__ == '__main__':
    main()