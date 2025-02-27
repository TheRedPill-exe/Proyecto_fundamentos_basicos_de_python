import sys
import os

# Get the parent directory of 'main' and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ui.ui import get_user_input, display_results
from api.api import fetch_data

def main():
    print("🚀 Welcome to the COVID-19 Data Query System for Colombia")

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

    data = fetch_data(department, record_limit)

    if not data:
        print("No data found for the given query.")
        return

    # Print results in a formatted table
    print("\nQuery Results:\n")
    print(f"{'City':<20} {'Department':<15} {'Age':<5} {'Type':<20} {'Status':<15} {'Country of Origin':<20}")
    print("-" * 100)

    for record in data:
        print("{:<20} {:<15} {:<5} {:<20} {:<15} {:<20}".format(
            record.get('ciudad_municipio_nom', 'N/A'),
            record.get('departamento_nom', 'N/A'),
            record.get('edad', 'N/A'),
            record.get('fuente_tipo_contagio', 'N/A'),
            record.get('estado', 'N/A'),
            record.get('pais_viajo_1_nom', 'N/A')
        ))

if __name__ == "__main__":
    main()
