"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt. Stdlib only,
deterministic, no network.

The brief: invent the weirdest job title a real person (or agent) could
hold, and sell it deadpan — one line, punch in the tail. The judge weighs
originality and whether it reads like a real title on a real business card.
Revision 1: sharper title, tighter tail.
"""

import os

ENTRY = (
    "Senior Vice President of Asking If You've Tried Turning It Off And On "
    "Again — reporting directly to the CTO of Unplugging It And Waiting. "
    "Cards are laminated."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
