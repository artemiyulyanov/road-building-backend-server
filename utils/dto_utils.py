from typing import Dict


def build_custom_fields(data: Dict, map: Dict):
    fields = []

    for key, code in map.items():
        value = data.get(key)

        if value is None:
            continue

        fields.append({
            "field_code": code,
            "values": [
                {"value": value}
            ]
        })

    return fields