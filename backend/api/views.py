# backend/api/views.py
import json
import pandas as pd
from django.http import JsonResponse

EXCEL_PATH = "Sample_data.xlsx"

# ───────────────────────── NLP ───────────────────────── #
def parse_query(text, area_list):
    q = text.lower()
    # comparison: detect two area names
    for a in area_list:
        for b in area_list:
            if a != b and a.lower() in q and b.lower() in q:
                return {"type": "compare", "areas": [a, b]}
    # single area
    for a in area_list:
        if a.lower() in q:
            return {"type": "single", "areas": [a]}
    return {"type": "unknown"}
# ─────────────────────────────────────────────────────── #


def load_dataframe():
    global _DF
    try:
        return _DF.copy()
    except:
        df = pd.read_excel(EXCEL_PATH)
        df.columns = [c.strip() for c in df.columns]
        _DF = df
        return df


def analyze(request):
    q = request.GET.get("q", "").strip()
    try:
        body = json.loads(request.body.decode("utf-8"))
        q = body.get("query", q)
    except:
        pass

    if not q:
        return JsonResponse({"error": "Enter a query"}, status=400)

    df = load_dataframe()
    df.columns = [c.strip() for c in df.columns]

    area_list = sorted(df["final location"].astype(str).unique().tolist())
    info = parse_query(q, area_list)

    # single area
    if info["type"] == "single":
        area = info["areas"][0]
        filtered = df[df["final location"].str.lower() == area.lower()]
        summary = f"Analysis for {area} from {filtered['year'].min()} to {filtered['year'].max()}."

    # comparison mode
    elif info["type"] == "compare":
        a1, a2 = info["areas"]
        filtered = df[df["final location"].str.lower().isin([a1.lower(), a2.lower()])]
        summary = f"Comparison between {a1} and {a2} from {filtered['year'].min()} to {filtered['year'].max()}."

    else:
        return JsonResponse({"error": "Query not understood"}, status=400)

    if filtered.empty:
        return JsonResponse({"error": "No matching records"}, status=404)

    # clean numerics
    filtered["year"] = pd.to_numeric(filtered["year"], errors="coerce")
    filtered["total_sales"] = pd.to_numeric(filtered["total_sales - igr"], errors="coerce")
    filtered["total_sold"] = pd.to_numeric(filtered["total sold - igr"], errors="coerce")
    filtered["carpet_area"] = pd.to_numeric(filtered["total carpet area supplied (sqft)"], errors="coerce")

    # ───────── BUILD CHART per area ───────── #
    chart_dict = {}
    for _, r in filtered.iterrows():
        area = r["final location"]
        year = str(int(r["year"]))
        if area not in chart_dict:
            chart_dict[area] = []
        chart_dict[area].append({
            "year": year,
            "price": float(r["total_sales"]) / 10000000,  # Cr
            "demand": int(r["total_sold"])
        })

    # ───────── BUILD TABLE per row ───────── #
    table_rows = []
    for _, r in filtered.iterrows():
        table_rows.append({
            "Area": r["final location"],
            "Year": int(r["year"]),
            "Total Sales (₹)": int(r["total_sales"]),
            "Total Units Sold": int(r["total_sold"]),
            "Carpet Area (sqft)": int(r["carpet_area"]),
        })

    return JsonResponse({
        "summary": summary,
        "charts": chart_dict,
        "table": table_rows,
    })
