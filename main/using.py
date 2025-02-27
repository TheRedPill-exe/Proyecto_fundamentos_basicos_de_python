import sys
import os

# Get the parent directory of 'main' and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ui.ui import get_user_input, display_results
from api.api import fetch_data

def main():
    #callig the function get_user_input
    department, record_limit = get_user_input()
    #calling the function fetch_data
    data = fetch_data(department, record_limit)
    #calling the function display_results
    display_results(data)
    
    

if __name__ == "__main__":
    main()
