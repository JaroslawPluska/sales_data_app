import csv
from collections import defaultdict
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)
CSV_PATH = Path(__file__).with_name("sales_data.csv")


def load_sales_by_region() -> dict[str, int]:
    sales_by_region: dict[str, int] = defaultdict(int)

    with CSV_PATH.open(newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            sales_by_region[row["region"]] += int(row["sales"])

    return dict(sales_by_region)


@app.get("/total_revenue")
def total_revenue():
    sales_by_region = load_sales_by_region()
    return jsonify(total_revenue=int(sum(sales_by_region.values())))


@app.get("/highest_region")
def highest_region():
    sales_by_region = load_sales_by_region()
    if not sales_by_region:
        return jsonify(error="No sales data available"), 404

    region, total_sales = max(sales_by_region.items(), key=lambda item: item[1])
    return jsonify(region=region, total_sales=int(total_sales))


if __name__ == "__main__":
    app.run(debug=True)
