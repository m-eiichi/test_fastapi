# generate_schema_code.py

import os
from models import Base
from sqlalchemy import Integer, String, Boolean, Float, DateTime, Text
import re

OUTPUT_DIR = "./graphql_types"
os.makedirs(OUTPUT_DIR, exist_ok=True)



def pascal_to_snake(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def sa_type_to_str(sa_type):
    if isinstance(sa_type, Integer):
        return "int"
    elif isinstance(sa_type, String) or isinstance(sa_type, Text):
        return "str"
    elif isinstance(sa_type, Boolean):
        return "bool"
    elif isinstance(sa_type, Float):
        return "float"
    elif isinstance(sa_type, DateTime):
        return "datetime.datetime"
    return "str"  # fallback

def generate_strawberry_class(model_class):
    class_name = model_class.__name__
    lines = [
        "import strawberry",
        "import datetime",
        "",
        "@strawberry.type",
        f"class {class_name}:"
    ]
    for column in model_class.__table__.columns:
        field_type = sa_type_to_str(column.type)
        lines.append(f"    {column.name}: {field_type}")
    return "\n".join(lines)

def generate_all_types(base):
    for mapper in base.registry.mappers:
        cls = mapper.class_
        code = generate_strawberry_class(cls)
        filename = os.path.join(OUTPUT_DIR, f"{pascal_to_snake(cls.__name__)}_type.py")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"✅ Generated: {filename}")

if __name__ == "__main__":
    generate_all_types(Base)
