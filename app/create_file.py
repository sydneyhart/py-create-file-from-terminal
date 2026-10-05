import sys
import os
from datetime import datetime

def main():
    args = sys.argv[1:]
    
    # Parse arguments
    directories = []
    filename = None
    
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i][0] != "-":
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            filename = args[i + 1]
            i += 2
        else:
            i += 1
    
    # Create directory hierarchy if specified
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."
    
    # Create/append to file if filename is specified
    if filename:
        file_path = os.path.join(dir_path, filename) if directories else filename
        
        # Check if file exists
        file_exists = os.path.exists(file_path)
        
        # Collect content lines
        lines = []
        line_number = 1
        
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            lines.append(f"{line_number} {content}")
            line_number += 1
        
        # Write to file
        if lines:
            with open(file_path, "a") as f:
                if file_exists:
                    f.write("\n\n")  # Blank line separator for appending
                else:
                    f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                
                f.write("\n".join(lines))

if __name__ == "__main__":
    main()
