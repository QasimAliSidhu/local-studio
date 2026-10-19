"""Implement your text reporting CLI here. See course 03's local brief."""
import argparse

def main():
    parser = argparse.ArgumentParser(description="Text report practice")
    parser.add_argument("file", help="UTF-8 input file")
    args = parser.parse_args()
    raise NotImplementedError("Read args.file and generate a word-frequency report")

if __name__ == "__main__":
    main()
