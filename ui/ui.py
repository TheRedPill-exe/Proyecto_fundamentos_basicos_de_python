def get_user_input():
    """
    Asks the user for the department and the number of records to retrieve.
    """
    department = input("Enter the department name: ")

    while True:
        try:
            record_limit = int(input("Enter the number of records to retrieve: "))
            if record_limit > 0:
                break
            else:
                print("The number of records must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    return department, record_limit


def display_results(data):
    """
    Displays the retrieved data in a formatted table.
    """
    if not data:
        print("No data found for the given query.")
        return

    print("\nQuery Results:\n")
    print(f"{'City':<20} {'Department':<15} {'Age':<5} {'Type':<20} {'Status':<15} ")
    print("-" * 75)

    for record in data:
        print(f"{record.get('ciudad_municipio_nom', 'N/A'):<20} "
              f"{record.get('departamento_nom', 'N/A'):<15} "
              f"{record.get('edad', 'N/A'):<5} "
              f"{record.get('fuente_tipo_contagio', 'N/A'):<20} "
              f"{record.get('estado', 'N/A'):<15} ")
