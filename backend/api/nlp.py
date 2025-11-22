import re

def extract_query_info(text, area_list):
    text = text.lower()

    # 1. detect multiple areas for comparison
    for a in area_list:
        for b in area_list:
            if a != b and a.lower() in text and b.lower() in text:
                return {
                    "type": "compare",
                    "areas": [a, b],
                }

    # 2. detect single area analysis
    for a in area_list:
        if a.lower() in text:
            return {
                "type": "single",
                "areas": [a],
            }

    return {"type": "unknown"}
