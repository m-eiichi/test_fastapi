# generate_graphql_schema.py

import os
import glob

TYPES_DIR = "./types"
OUTPUT_FILE = "./schema.py"

def snake_to_pascal(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))

def generate_schema_file():
    type_files = glob.glob(os.path.join(TYPES_DIR, "*_type.py"))

    import_lines = [
        "import strawberry",
        "from typing import List",
        "import datetime",
    ]
    query_lines = [
        "@strawberry.type",
        "class Query:",
    ]

    for type_file in type_files:
        module_name = os.path.basename(type_file).replace(".py", "")
        class_name = snake_to_pascal(module_name.replace("_type", ""))
        import_lines.append(f"from types.{module_name} import {class_name}")
        query_lines.append(
            f"    @strawberry.field\n"
            f"    def all_{class_name.lower()}s(self) -> List[{class_name}]:\n"
            f"        return []  # TODO: 実装"
        )

    schema_line = "schema = strawberry.Schema(query=Query)"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(import_lines))
        f.write("\n\n")
        f.write("\n".join(query_lines))
        f.write("\n\n")
        f.write(schema_line)

    print(f"✅ Generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_schema_file()
