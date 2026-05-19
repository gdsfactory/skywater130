"""Post-process notebook markdown: convert MyST admonitions to Material style.

Usage: python docs/hooks.py docs/notebooks/*.md
"""

import re
import sys
from pathlib import Path


def process(markdown: str) -> str:
    """Apply all transformations to a markdown string."""
    return _myst_to_material_admonitions(markdown)


def _myst_to_material_admonitions(markdown: str) -> str:
    r"""Convert MyST ```{type}\n...\n``` to Material !!! type\n\n    ..."""

    def _replace(match: re.Match[str]) -> str:
        kind = match.group(1)
        body = match.group(2)
        lines = body.splitlines()
        title = ""
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and (m := re.match(r"^#+ +(.+)", lines[0])):
            title = m.group(1)
            lines.pop(0)
        non_empty = [line for line in lines if line.strip()]
        min_indent = min(
            (len(line) - len(line.lstrip()) for line in non_empty), default=0
        )
        out = []
        for line in lines:
            if line.strip():
                out.append("    " + line[min_indent:])
            else:
                out.append("")
        header = f'!!! {kind} "{title}"' if title else f"!!! {kind}"
        return header + "\n\n" + "\n".join(out).rstrip() + "\n"

    return re.sub(
        r"^```\{(\w+)\}\s*\n(.*?)^```\s*$",
        _replace,
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    )


if __name__ == "__main__":
    for path in sys.argv[1:]:
        p = Path(path)
        p.write_text(process(p.read_text()))
