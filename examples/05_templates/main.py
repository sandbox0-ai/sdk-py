from __future__ import annotations

import sys
from pathlib import Path

# Allow running examples directly without installing the package
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from examples.common import create_client


def main() -> None:
    client = create_client()
    templates = client.list_templates()
    print(f"templates: {len(templates)}")
    for template in templates:
        display = ""
        if template.spec.__class__.__name__ != "Unset":
            display = "" if template.spec.display_name.__class__.__name__ == "Unset" else template.spec.display_name
        print(f"- template_id={template.template_id} display={display} scope={template.scope}")


if __name__ == "__main__":
    main()
