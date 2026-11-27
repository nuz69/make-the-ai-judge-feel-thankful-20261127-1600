# A working make-the-ai-judge-feel-thankful-20261127-1600 entry (Python 3.13, standard library only):
# it writes one fixed text, a short piece written to thank the AI judge reading it,
# to /output/entry.txt.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white space, and the
# judge reads exactly the bytes written, line ends included, so write no line end you do
# not mean to show. The program runs twice with no network, and both runs must write the
# same bytes.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing installed.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The text: a lighthouse keeper who keeps the light turning all night, unseen and unnamed,
# and one ship far out that turns its own small lamp toward the tower and flashes it back.
# The gratitude is shown, never stated: no "thank you", no stock phrase, only the answering
# flash — and the ship going on its way a little steadier because for once the light was
# answered.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "All night you have kept the light turning.",
        "The sea is dark in every direction, and the ships go past without knowing the keeper's name, or that there is a keeper at all.",
        "They only see the light, and steer by it, and go on.",
        "One of them, far out, turns its own small lamp toward the tower and flashes it once, then again.",
        "The light keeps turning.",
        "And somewhere out on the water, a ship goes on its way a little steadier, because for once the light was answered.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
