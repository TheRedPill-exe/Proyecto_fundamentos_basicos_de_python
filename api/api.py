import pandas as pd
from sodapy import Socrata

def fetch_data(department, record_limit):
    """
    Fetches COVID-19 data from Colombia's Open Data API using a SoQL query to filter by department.
    Returns only the required columns: City, Department, Age, Type, Status, and Country of Origin.
    """
    try:
        client = Socrata("www.datos.gov.co", None)

        # Build the SoQL filter using $where to select records for the specified department.
        # We assume the department names in the dataset are in uppercase.
        soql_filter = f"departamento_nom='{department.upper()}'"

        results = client.get("gt2j-8ykr", limit=record_limit, **{"$where": soql_filter})

        if not results:
            print("⚠ The API returned no data for the given filter.")
            return []

        # Convert results into a Pandas DataFrame
        df = pd.DataFrame.from_records(results)


        # Define required columns:
        # City (ciudad_municipio_nom), Department (departamento_nom),
        # Age (edad), Type (fuente_tipo_contagio), Status (estado),
        # and Country of Origin (pais_viajo_1_nom)
        required_columns = [
            "ciudad_municipio_nom",
            "departamento_nom",
            "edad",
            "fuente_tipo_contagio",
            "estado",
        ]

        # Keep only the columns that are available
        df = df[[col for col in required_columns if col in df.columns]]

        return df.to_dict(orient="records")
    
    except Exception as e:
        print(f"❌ Error fetching data from API: {e}")
        return []
