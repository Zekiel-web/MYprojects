import ast

def load_data(filename):
    with open(filename, 'r') as file:
        content = file.read()

    data_dict = {}

    # Split each line and evaluate the lists
    for line in content.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            # Convert string list into real Python list
            data_dict[key] = ast.literal_eval(value)

    return data_dict

def display_record(data, index):
    print("\n--- Record Found ---")
    print(f"ID: {data['ids'][index]}")
    print(f"First Name: {data['first_names'][index]}")
    print(f"Last Name: {data['last_names'][index]}")
    print(f"Age: {data['ages'][index]}")
    print(f"Occupation: {data['occupations'][index]}")
    print()

def search(field_list, value):
    results = []
    for i in range(len(field_list)):
        if str(field_list[i]).lower() == value.lower():
            results.append(i)
    return results

def main():
    data = load_data(r"C:\Users\Ezekiel F. Cielo\OneDrive\Desktop\PYTHON WORKPLACE\data.txt")

    while True:
        print("\n--- Search Menu ---")
        print("1 - First Name")
        print("2 - Last Name")
        print("3 - Age")
        print("4 - Occupation")
        print("5 - ID")

        choice = input("Enter choice: ")

        if choice == "1":
            value = input("Enter First Name: ")
            results = search(data["first_names"], value)

        elif choice == "2":
            value = input("Enter Last Name: ")
            results = search(data["last_names"], value)

        elif choice == "3":
            value = input("Enter Age: ")
            results = search([str(a) for a in data["ages"]], value)

        elif choice == "4":
            value = input("Enter Occupation: ")
            results = search(data["occupations"], value)

        elif choice == "5":
            value = input("Enter ID: ")
            results = search(data["ids"], value)

        else:
            print("Invalid choice.")
            continue

        if results:
            for i in results:
                display_record(data, i)
        else:
            print("\nNo matching record found.\n")

        again = input("Search again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()