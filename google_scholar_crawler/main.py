from datetime import datetime
import json
import os

from scholarly import ProxyGenerator, scholarly


def require_scholar_id() -> str:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise SystemExit(
            "GOOGLE_SCHOLAR_ID is not set. Add the secret before running the Google Scholar crawler."
        )
    return scholar_id


def main() -> None:
    scholar_id = require_scholar_id()

    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    author["updated"] = str(datetime.now())
    author["publications"] = {item["author_pub_id"]: item for item in author["publications"]}

    print(json.dumps(author, indent=2, default=str))
    os.makedirs("results", exist_ok=True)

    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False, default=str)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"]),
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
