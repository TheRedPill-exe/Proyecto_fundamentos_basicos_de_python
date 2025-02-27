import pandas as pd
from sodapy import Socrata

def get_api_client():
    """
    Creates and returns a Socrata API client.
    """
    return Socrata("www.datos.gov.co", None)

def build_query(department):
    """
    Constructs the SoQL query to filter data by department.
    """
    return {"$where": f"departamento_nom='{department.upper()}'"}

def fetch_raw_data(client, query_params, record_limit):
    """
    Fetches raw data from the API using the given client, query parameters, and record limit.
    """
    try:
        return client.get("gt2j-8ykr", limit=record_limit, **query_params)
    except Exception as e:
        print(f"❌ Error fetching data from API: {e}")
        return []

def process_data(results):
    """
    Processes the raw API response into a structured Pandas DataFrame with only required columns.
    """
    if not results:
        print("⚠ No data returned from the API.")
        return []

    df = pd.DataFrame.from_records(results)

    # Define required columns
    required_columns = [
        "ciudad_municipio_nom",
        "departamento_nom",
        "edad",
        "fuente_tipo_contagio",
        "estado",
    ]

    # Add "pais_viajo_1_nom" if missing
    if "pais_viajo_1_nom" not in df.columns:
        df["pais_viajo_1_nom"] = "N/A"

    required_columns.append("pais_viajo_1_nom")

    # Keep only the columns that are available
    df = df[[col for col in required_columns if col in df.columns]]

    return df.to_dict(orient="records")

def fetch_data(department, record_limit):
    """
    Orchestrates the data fetching process from API to structured dictionary output.
    """
    client = get_api_client()
    query_params = build_query(department)
    raw_data = fetch_raw_data(client, query_params, record_limit)
    return process_data(raw_data)
