import os
import tempfile
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", help="Key of saved data")
    parser.add_argument("-v", "--val", help="Value of saved data")
    args = parser.parse_args()
    return args.key, args.val

def read_data(storage_path):
    try:
        with open(storage_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    return data

def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        json.dump(data, f)

def get_data(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])

def put_data(storage_path, key, value):
    data = read_data(storage_path)
    if key not in data:
        data[key] = []
    data[key].append(value)
    write_data(storage_path, data)

def main():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    key, value = parse_args()

    if key and value:
        put_data(storage_path, key, value)
        print("Stored!")
    elif key:
        value_list = get_data(storage_path, key)
        if value_list:
            print(", ".join(value_list))
    else:
        print("Something went wrong!")


if __name__ == "__main__":
    main()