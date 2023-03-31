from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from avro.schema import Parse

# Open the Avro data file in binary mode
with open('data.avro', 'rb') as f:
    # Create a reader object
    reader = DataFileReader(f, DatumReader())

    # Define the filtering condition
    filter_condition = lambda record: record['age'] >= 18

    # Parse the schema from a separate file
    schema = Parse(open('schema.avsc', 'r').read())

    # Create a writer object with the parsed schema
    writer = DataFileWriter(open('filtered_data.avro', 'wb'), DatumWriter(), schema)

    # Iterate through each record in the Avro file
    for record in reader:
        # Check if the record satisfies the filtering condition
        if filter_condition(record):
            # Write the filtered record to the output Avro file
            writer.append(record)

    # Close the reader and writer objects
    reader.close()
    writer.close()
