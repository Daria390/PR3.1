# Функція для виведення на екран усіх значень словника
def print_dictionary(data):
    if not data:
        print("Dictionary is empty!")
        return
    print("\nDictionary Content (Country: [Population, Area])")
    for country, info in data.items():
        print(f"{country} -> Population: {info[0]}M, Area: {info[1]} thousand km²")

# Функція для додавання нового запису
def add_record(data):
    country = input("Enter the name of the new country: ").strip()
    if country in data:
        print(f"Error: country '{country}' already exists in the dictionary!")
        return
    
    try:
        population = float(input("Enter population (in millions): "))
        area = float(input("Enter area (in thousand km²): "))
        if population < 0 or area <= 0:
            print("Error: values cannot be negative, and area cannot be zero.")
            return
        data[country] = [population, area]
        print(f"Country '{country}' successfully added!")
    except ValueError:
        print("Input error! Please enter numbers.")

# Функція видалення запису за ключом з обробкою винятку KeyError
def delete_record(data):
    country = input("Enter the name of the country to delete: ").strip()
    try:
        del data[country]
        print(f"Country '{country}' successfully deleted.")
    except KeyError:
        print(f"Error: country '{country}' does not exist in the dictionary!")

# Функція для перегляду за відсортованими ключами
def print_sorted_keys(data):
    if not data:
        print("Dictionary is empty!")
        return
    print("\nList Sorted by Country Names")
    sorted_keys = sorted(data.keys())
    for country in sorted_keys:
        info = data[country]
        print(f"{country} -> Population: {info[0]}M, Area: {info[1]} thousand km²")


# Розв'язання завдання. Варіант 15: держава з максимальною щільністю
def solve_variant(data):
    if not data:
        print("Dictionary is empty!")
        return
    
    max_density = -1
    max_country = ""
    
    for country, info in data.items():
        # Формула щільності: (населення в млн * 1 000 000) / (площа в тис. км² * 1 000)
        # Спрощується до: (info[0] / info[1]) * 1 000 осіб/км²
        density = (info[0] / info[1]) * 1000
        
        if density > max_density:
            max_density = density
            max_country = country
            
    print(f"\nCountry with maximum population density: {max_country}")
    print(f"Density is approximately {max_density:.2f} people/km²")