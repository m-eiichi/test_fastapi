import inspect
from typing import get_args, get_origin, List
from sqlalchemy.orm import DeclarativeMeta, RelationshipProperty
from sqlalchemy.orm import registry
import models  # ← モデルファイルをインポート（適宜変更）

mapper_registry: registry = models.Base.registry

def snake_to_pascal(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))

def is_relationship(attr) -> bool:
    return isinstance(attr, RelationshipProperty)

def generate_strawberry_type(model_class: DeclarativeMeta) -> str:
    class_name = model_class.__name__
    fields = []
    for attr_name, attr in model_class.__mapper__.all_orm_descriptors.items():
        # 通常のカラムかリレーションか
        if hasattr(attr, "property"):
            prop = attr.property
            if isinstance(prop, RelationshipProperty):
                related_class = prop.mapper.class_.__name__
                if prop.uselist:
                    fields.append(f"    {attr_name}: List[{related_class}Type]")
                else:
                    fields.append(f"    {attr_name}: Optional[{related_class}Type]")
            else:
                field_type = prop.columns[0].type.__class__.__name__
                if field_type == "INTEGER":
                    fields.append(f"    {attr_name}: int")
                elif field_type == "VARCHAR":
                    fields.append(f"    {attr_name}: str")
                elif field_type == "DATETIME":
                    fields.append(f"    {attr_name}: datetime.datetime")
                else:
                    fields.append(f"    {attr_name}: str  # Unknown type")
    
    result = [f"@strawberry.type", f"class {class_name}Type:"]
    if fields:
        result.extend(fields)
    else:
        result.append("    pass")
    return "\n".join(result)

# モデル一覧から自動生成
for mapper in mapper_registry.mappers:
    model_class = mapper.class_
    print(generate_strawberry_type(model_class))
    print()

