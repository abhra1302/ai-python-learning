# Write and Read a List of Items to a File
def write_list_to_file(file_path, items):
    try:
        with open(file_path, "w") as file:
            for item in items:
                file.write(f"{item}\n")
        print(f"List written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_list_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            items = file.readlines()
            print("Items read from the file:")
            for item in items:
                print(f" - {item.strip()}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
write_list_to_file("fruits.txt", items)
read_items = read_list_from_file("fruits.txt")