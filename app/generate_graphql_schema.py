# generate_graphql_schema.py

import os
import glob
# from typing import List

TYPES_DIR = "./graphql_types"
OUTPUT_FILE = "./graphql_schema.py"

def snake_to_pascal(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))

def generate_schema_file():
    type_files = glob.glob(os.path.join(TYPES_DIR, "*_type.py"))

    import_lines = [
        "import strawberry",
        "from typing import List",
        "import datetime",
        "import asyncpg",  # asyncpgをインポート
        "import os",
        "from dotenv import load_dotenv",
    ]
    query_lines = [
        "@strawberry.type",
        "class Query:",
    ]

    for type_file in type_files:
        module_name = os.path.basename(type_file).replace(".py", "")
        class_name = snake_to_pascal(module_name.replace("_type", ""))

        # インポート文を追加
        import_lines.append(f"from graphql_types.{module_name} import {class_name}")

        # 非同期関数の生成
        query_lines.append(
            f"    @strawberry.field"
            f"\n    async def {class_name.lower()}s(self) -> List[{class_name}]:"
            f"\n        return await fetch_{class_name.lower()}s()  # asyncpgでデータを取得"
        )

        # 非同期関数を生成（asyncpgを使用してデータを取得）
        query_lines.append(
            f"\n"
            f"\nasync def fetch_{class_name.lower()}s():"
            f"\n    conn = await asyncpg.connect("
            f"\n        user=os.getenv('DB_USER'),"
            f"\n        password=os.getenv('DB_PASSWORD'),"
            f"\n        database=os.getenv('DB_NAME'),"
            f"\n        host=os.getenv('DB_HOST'),"
            f"\n        ssl=True"
            f"\n    )"
            f"\n    rows = await conn.fetch('SELECT id, name FROM {class_name.lower()}')"
            f"\n    await conn.close()"
            f"\n    return [{class_name}(id=row['id'], name=row['name']) for row in rows]"
        )


    schema_line = "schema = strawberry.Schema(query=Query)"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(import_lines))
        f.write("\n\n")
        f.write("\nload_dotenv()")
        f.write("\n\n")
        f.write("\n".join(query_lines))
        f.write("\n\n")
        f.write(schema_line)

    print(f"✅ Generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_schema_file()
