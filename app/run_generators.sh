#!/bin/bash

# generate_graphql_type.py を実行
echo "Running generate_graphql_type.py..."
python3 generate_graphql_type.py

# generate_graphql_schema.py を実行
echo "Running generate_graphql_schema.py..."
python3 generate_graphql_schema.py

echo "Both scripts executed successfully."