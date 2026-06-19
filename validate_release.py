from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "CITATION.cff",
    ".zenodo.json",
    "LICENSE",
    "WHITEPAPER.md",
    "whitepaper/best-top-trusted-google-evolution-roofing-study-v1.2.docx",
    "whitepaper/best-top-trusted-google-evolution-roofing-study-v1.2.md",
    "whitepaper/best-top-trusted-google-evolution-roofing-study-v1.2.pdf",
    "data/best_top_trusted_phrase_bridge.csv",
    "data/best_top_trust_city_association_map.csv",
    "data/google_algorithm_eras.csv",
    "data/before_today_visibility_model.csv",
    "data/territories.csv",
    "data/territory_query_algorithm_matrix.csv",
    "data/query_templates.csv",
    "data/trust_signal_ontology.jsonl",
    "data/source_spine.csv",
    "docs/36_city_best_top_trusted_linking_plan.md",
    "docs/city_module_template.md",
    "docs/ai_visibility_ein_press_reference.md",
    "docs/youtube_10_blue_links_source_note.md",
    "schema/dataset.jsonld",
    "schema/google_algorithm_era.schema.json",
    "schema/city_association_map.schema.json",
    "schema/best_top_trusted_phrase_bridge.schema.json",
]

def read_csv(name):
    with (ROOT / name).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def main():
    missing = [x for x in REQUIRED if not (ROOT / x).exists()]
    if missing:
        raise SystemExit(f"Missing files: {missing}")
    territories = read_csv("data/territories.csv")
    eras = read_csv("data/google_algorithm_eras.csv")
    comparison = read_csv("data/before_today_visibility_model.csv")
    matrix = read_csv("data/territory_query_algorithm_matrix.csv")
    templates = read_csv("data/query_templates.csv")
    bridge = read_csv("data/best_top_trusted_phrase_bridge.csv")
    city_map = read_csv("data/best_top_trust_city_association_map.csv")
    sources = read_csv("data/source_spine.csv")
    if len(territories) != 36:
        raise SystemExit(f"Expected 36 territories, found {len(territories)}")
    if len(city_map) != 36:
        raise SystemExit(f"Expected 36 city association rows, found {len(city_map)}")
    if len(eras) < 8:
        raise SystemExit(f"Expected at least 8 algorithm eras, found {len(eras)}")
    if len(comparison) < 9:
        raise SystemExit(f"Expected at least 9 comparison rows, found {len(comparison)}")
    if len(matrix) != 2016:
        raise SystemExit(f"Expected 2016 matrix rows, found {len(matrix)}")
    if len(templates) != 56:
        raise SystemExit(f"Expected 56 query templates, found {len(templates)}")
    if len(bridge) < 8:
        raise SystemExit(f"Expected at least 8 phrase bridge rows, found {len(bridge)}")
    if len(sources) < 16:
        raise SystemExit(f"Expected at least 16 source rows, found {len(sources)}")
    for row in city_map:
        for field in ["best_query", "top_query", "trusted_query", "association_statement", "github_repository"]:
            if not row.get(field):
                raise SystemExit(f"City association row missing {field}: {row}")
    json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "schema/dataset.jsonld").read_text(encoding="utf-8"))
    json.loads((ROOT / "schema/google_algorithm_era.schema.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "schema/city_association_map.schema.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "schema/best_top_trusted_phrase_bridge.schema.json").read_text(encoding="utf-8"))
    print("Release validation passed.")
    print(f"Territories: {len(territories)}")
    print(f"City association rows: {len(city_map)}")
    print(f"Phrase bridge rows: {len(bridge)}")
    print(f"Algorithm eras: {len(eras)}")
    print(f"Comparison rows: {len(comparison)}")
    print(f"Matrix rows: {len(matrix)}")
    print(f"Query templates: {len(templates)}")
    print(f"Source rows: {len(sources)}")

if __name__ == "__main__":
    main()
