# Teaching Decks Duel

A two-player Magic: The Gathering game for learning the game with the Tensai88 Budget Beginner Teaching Decks (Green, Red, White, Black, Blue). Simplified stack-free rules, full turns, 31 blocking puzzles plus 6 turn puzzles.

Play: https://chris-chamberlain.github.io/teaching-decks-duel/

- Live play across two devices: one player hosts and shares the 4-letter code, the other joins. Uses a PeerJS peer-to-peer connection, so both devices need internet access.
- One device, take turns, is also available.
- On iPhone, use Share, then Add to Home Screen.

## Music

Two recorded tracks in `music/` play in turn (Oak Tankard Overture, Medieval Fantasy). The generated music is the fallback if a file will not load.

## Open items

- Music: choose a theme track for each deck (Green, Red, White, Black, Blue), starting from the Pixabay "renaissance fair" search (https://pixabay.com/music/search/renaissance%20fair/). Decide how tracks switch (per deck, per screen, or per turn), loop or crossfade behaviour, and check licences before adding files.

Card art is from the owner's own proxy sheets. Magic: The Gathering is a trademark of Wizards of the Coast. Fan project for personal, non-commercial use.

## Build rules
- After any substantive content or copy change, run `python3 tools/copycheck.py`, then read every user-facing string it lists and rewrite anything that sounds AI-written (taglines, stock words, dashes as punctuation, contrastive negation, label-colon openers, filler modifiers). Card text from Tensai88 is exempt. Fix what it flags before publishing.
