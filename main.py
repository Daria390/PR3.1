# Імпортуємо модуль 
import task1

def main():
    # Початковий словник (10 держав: ключ — назва, значення — [населення в млн, площа в тис. км²])
    countries_data = {
        "Ukraine": [38.0, 603.6],
        "Poland": [37.7, 312.7],
        "Germany": [84.3, 357.0],
        "France": [68.0, 551.7],
        "Italy": [59.0, 301.3],
        "Canada": [38.5, 9984.7],
        "Japan": [124.5, 377.9],
        "Egypt": [104.2, 1010.4],
        "Lithuania": [2.8, 65.3],
        "Switzerland": [8.7, 41.3]
    }

    while True:
        print("\nMENU")
        print("1. Print all dictionary values")
        print("2. Add a new record")
        print("3. Delete a record by key")
        print("4. View content by sorted keys")
        print("5. Solve variant task (maximum density)")
        print("0. Exit")
        
        choice = input("Choose menu option: ").strip()
        
        if choice == '1':
            task1.print_dictionary(countries_data)
        elif choice == '2':
            task1.add_record(countries_data)
        elif choice == '3':
            task1.delete_record(countries_data)
        elif choice == '4':
            task1.print_sorted_keys(countries_data)
        elif choice == '5':
            task1.solve_variant(countries_data)
        elif choice == '0':
            break
        else:
            print("Error: this menu option does not exist. Try again.")

if __name__ == "__main__":
    main()
