import fastavro
import json

# Open the binary Avro JSON file
with open('file.avro', 'rb') as f:
    # Parse the schema
    schema = fastavro.schemaless_reader(f).schema

    # Iterate over the records and tokenize each one
    for record in fastavro.reader(f, schema):
        # Convert the record to a JSON string
        json_string = json.dumps(record)

        # Tokenize the JSON string
        tokens = json.loads(json_string)

        # Do something with the tokens, such as print them
        print(tokens)

