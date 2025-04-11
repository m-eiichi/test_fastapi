import os
import glob
import re
from dotenv import load_dotenv

load_dotenv()

TYPES_DIR = "./graphql_types"
OUTPUT_FILE = "./graphql_schema.py"

def snake_to_pascal(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))

def extract_fields(filepath: str) -> list[str]:
    """ファイルからすべてのフィールドを抽出"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return re.findall(r"^\s*(?!class\b|def\b)(\w+)\s*:\s*[\w\[\]\.]+", content, re.MULTILINE)

def generate_schema_file():
    type_files = glob.glob(os.path.join(TYPES_DIR, "*_type.py"))

    import_lines = [
        "import strawberry",
        "from typing import List, Optional",
        "import datetime",
        "import asyncpg",
        "import os",
        "from dotenv import load_dotenv",
    ]
    query_lines = []
    schema_lines = [
        "@strawberry.type",
        "class Query:",
    ]

    for type_file in type_files:
        module_name = os.path.basename(type_file).replace(".py", "")
        remove_type_name = module_name.replace("_type", "")
        class_name = snake_to_pascal(remove_type_name)

        # すべてのフィールドを抽出
        fields = extract_fields(type_file)

        import_lines.append(f"from graphql_types.{module_name} import {class_name}")

        # クエリ関数の定義（引数付き）
        query_lines.append(f"\nasync def fetch_{class_name.lower()}s({', '.join([f'{f}: Optional[int] = None' for f in fields])}):")
        query_lines.append("    conn = await asyncpg.connect(")
        query_lines.append("        user=os.getenv('DB_USER'),")
        query_lines.append("        password=os.getenv('DB_PASSWORD'),")
        query_lines.append("        database=os.getenv('DB_NAME'),")
        query_lines.append("        host=os.getenv('DB_HOST'),")
        query_lines.append("        ssl=True")
        query_lines.append("    )")

        # 条件句の組み立て
        query_lines.append("    query = 'SELECT * FROM " + remove_type_name + "'")
        query_lines.append("    conditions = []")
        query_lines.append("    values = []")

        for field in fields:
            query_lines.append(f"    if {field} is not None:")
            query_lines.append(f"        conditions.append(f\"{field} = ${{len(values) + 1}}\")")
            query_lines.append(f"        values.append({field})")

        query_lines.append("    if conditions:")
        query_lines.append("        query += ' WHERE ' + ' AND '.join(conditions)")

        query_lines.append("    rows = await conn.fetch(query, *values)")
        query_lines.append("    await conn.close()")
        query_lines.append(f"    return [{class_name}(**dict(row)) for row in rows]")

        # スキーマ定義（引数付き）
        field_args = ', '.join([f"{f}: Optional[int] = None" for f in fields])
        call_args = ', '.join([f"{f}={f}" for f in fields])
        schema_lines.append(f"\n    @strawberry.field")
        schema_lines.append(f"    async def {class_name.lower()}s(self, {field_args}) -> List[{class_name}]:")
        schema_lines.append(f"        return await fetch_{class_name.lower()}s({call_args})")

    schema_line = "schema = strawberry.Schema(query=Query)"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(import_lines))
        f.write("\n\nload_dotenv()\n\n")
        f.write("\n".join(query_lines))
        f.write("\n\n")
        f.write("\n".join(schema_lines))
        f.write("\n\n")
        f.write(schema_line)

    print(f"✅ Generated: {OUTPUT_FILE}")
    
if __name__ == "__main__":
    generate_schema_file()



    
