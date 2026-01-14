#!/usr/bin/env python3
import json
import sys
import xml.etree.ElementTree as ET

def main():
    if len(sys.argv) != 2:
        print("Usage: spotbugs_to_rdjson.py <spotbugsXml.xml>", file=sys.stderr)
        sys.exit(2)

    path = sys.argv[1]
    root = ET.parse(path).getroot()

    diagnostics = []

    for bug in root.findall("BugInstance"):
        msg = bug.findtext("LongMessage") or bug.findtext("ShortMessage") or "SpotBugs issue"
        src = bug.find("SourceLine")
        if src is None:
            continue

        file_path = src.get("sourcepath") or src.get("classname", "").replace(".", "/") + ".java"
        start = int(src.get("start", "1"))

        diagnostics.append({
            "message": msg,
            "location": {
                "path": file_path,
                "range": {
                    "start": {"line": start, "column": 1},
                    "end": {"line": start, "column": 1}
                }
            },
            "severity": "WARNING"
        })

    out = {
        "source": {"name": "spotbugs"},
        "diagnostics": diagnostics
    }
    print(json.dumps(out))

if __name__ == "__main__":
    main()
