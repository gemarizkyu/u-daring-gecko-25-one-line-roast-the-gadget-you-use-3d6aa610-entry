"""One-line roast: the gadget I use every day.

Writes a single original roast line to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
"""

from pathlib import Path

SETUP = "My phone's autocorrect never fixes a typo"
PUNCHLINE = "it just promotes it into a formal apology I have to send my boss."
EM_DASH = "\u2014"


def build_roast() -> str:
    """Assemble the single roast line from its two halves."""
    return f"{SETUP} {EM_DASH} {PUNCHLINE}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    output_path.write_text(build_roast(), encoding="utf-8")


if __name__ == "__main__":
    main()
