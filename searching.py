from pathlib import Path
import json


def read_data(data_path, key):
    with open(data_path, 'r') as f:
        data = json.load(f)
    if key in data:
        return data[key]
    else:
        return None


def main():
    print(read_data('sequential.json', "unordered_numbers"))


if __name__ == "__main__":
    main()
