"""Joke: the agent aces the rehearsal, so the one time it works live is exactly when you stop trusting it."""

import os

JOKE = (
    "My agent aced the rehearsal, so on stage I told the room 'watch this' "
    "— and it worked, which is exactly when I stopped trusting it."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()