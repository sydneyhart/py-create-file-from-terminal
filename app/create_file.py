import argparse
import os
from datetime import datetime
from pathlib import Path


def create_file(file_path: Path) -> None:
    separator = ""
    if file_path.exists() and file_path.stat().st_size > 0:
        with file_path.open("rb") as existing_file:
            existing_file.seek(-1, os.SEEK_END)
            ends_with_newline = existing_file.read(1) == b"\n"
        separator = "\n" if ends_with_newline else "\n\n"

    with file_path.open("a", encoding="utf-8") as output_file:
        output_file.write(separator)
        output_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            output_file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and append timestamped file content."
    )
    parser.add_argument(
        "-d", nargs="+", metavar="DIRECTORY", help="Separate directory names"
    )
    parser.add_argument("-f", metavar="FILE", help="File name")
    args = parser.parse_args()

    if args.d is None and args.f is None:
        parser.error("Provide -d, -f, or both.")

    directory = Path(".")
    if args.d is not None:
        directory = Path(os.path.join(*args.d))
        os.makedirs(directory, exist_ok=True)

    if args.f is not None:
        create_file(directory / args.f)


if __name__ == "__main__":
    main()
