from avro.datafile import DataFileReader
from avro.io import DatumReader
import json

# Open the Avro data file in binary mode
with open('data.avro', 'rb') as f:
    # Create a reader object
    reader = DataFileReader(f, DatumReader())

    # Define the filtering condition
    filter_condition = lambda record: record['age'] >= 18

    # Iterate through each record in the Avro file
    filtered_records = []
    for record in reader:
        # Check if the record satisfies the filtering condition
        if filter_condition(record):
            # Convert the record to a JSON string
            json_record = json.dumps(record)
            # Append the JSON string to the list of filtered records
            filtered_records.append(json_record)

    # Close the reader object
    reader.close()

# Write the filtered records to a JSON file
with open('filtered_data.json', 'w') as f:
    f.write('\n'.join(filtered_records))
