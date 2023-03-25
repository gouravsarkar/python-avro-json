# python-avro-json

avro-json-tokenization
To tokenize a binary Avro JSON file using Python, you can use the fastavro library.

This script uses the fastavro library to read the schema and records from the binary Avro JSON file. It then converts each record to a JSON string and tokenizes the string using the json library. You can modify the script to suit your needs, such as by modifying the tokenization process or saving the tokens to a file.


avro-json-filtering
Here's an example Python script that reads in binary Avro data, filters the records based on a condition, and outputs the filtered records as JSON

This script assumes that the Avro data is stored in a file named data.avro in the current directory. You can modify the filtering condition to suit your specific needs. The filtered records are stored in a list of JSON strings, which are then written to a file named filtered_data.json in the current directory.
