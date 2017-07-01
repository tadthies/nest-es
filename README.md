# nest-es

Nest Thermostat meet Elasticsearch.

## Requirements

 * pip install python-nest
 * pip install elasticsearch

## Using

 * Visit https://developers.nest.com and create new Product
   * Should have at least read access to Thermostat
 * Grab Product ID and Product Secret
 * Run: nest --client-id <Product ID> --client-secret <Product Secret> --token-cache token.json show
   * When typing in PIN, be sure to put it in double quotes
 * Edit vars in the script.
