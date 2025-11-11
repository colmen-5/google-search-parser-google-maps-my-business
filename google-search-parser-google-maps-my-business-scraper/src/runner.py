thonimport json
from extractors.google_parser import GoogleParser
from outputs.exporters import Exporter

def main():
    # Example input query
    query = "Staycation Co Miami FL"

    # Extract data using the GoogleParser
    parser = GoogleParser(query)
    extracted_data = parser.extract_business_info()

    # Export the data using Exporter
    exporter = Exporter(extracted_data)
    exporter.export_to_json('output.json')

if __name__ == '__main__':
    main()