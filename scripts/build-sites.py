
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "schools-data"
TEMPLATE_FILE = ROOT / "template" / "index.html"
OUTPUT_DIR = ROOT / "dist" / "schools"

def main():
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for config_file in sorted(DATA_DIR.glob("*.json")):
        school = json.loads(config_file.read_text(encoding="utf-8"))
        school_id = school.get("school_id", "")

        if not re.fullmatch(r"[a-z0-9-]+", school_id):
            raise ValueError(f"Invalid school ID: {school_id!r}")

        html = template
        html = html.replace(
            "Telangana Model School",
            school.get("school_name", "Telangana Model School")
        )
        html = html.replace(
            "Telangana, India",
            ", ".join(filter(None, [
                school.get("village", ""),
                school.get("mandal", ""),
                school.get("district", ""),
                school.get("state", "")
            ]))
        )
        html = html.replace(
            "School address will be added here.",
            ", ".join(filter(None, [
                school.get("village", ""),
                school.get("mandal", ""),
                school.get("district", ""),
                school.get("state", "")
            ]))
        )

        destination = OUTPUT_DIR / school_id / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(html, encoding="utf-8")
        print(f"Generated: {destination.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
      
