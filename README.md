# The World Today — Tuesday, 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/khususcrypto0000-coder/news-image-20261124-makefun/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/khususcrypto0000-coder/news-image-20261124-makefun/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world's news of **Tuesday, 24 November 2026**,
drawn as a newspaper front page: masthead *THE WORLD TODAY*, the date in
full, and six stories from across regions and fields, each with a short
factual summary and a simple geometric illustration (no photographs).

## The six stories

1. **Ukraine peace talks (lead)** — Abu Dhabi trilateral talks end; US
   envoys Jared Kushner and Steve Witkoff fly on to Moscow, then Dublin.
   The Kremlin says it sees no "added value" in a European seat at the
   table.
2. **War in Ukraine** — An overnight Russian strike on Zaporizhzhia kills
   2 and wounds 40, including four children; Ukraine strikes the Kerch
   Bridge again.
3. **Gaza** — Israeli strikes kill Naeem Abu Nahel, Hamas' internal
   security chief, with six others, medics say.
4. **US–Iran** — VP JD Vance and Secretary of State Marco Rubio meet
   Qatar's prime minister at the White House; Iran vows to use "all its
   tools" against the US naval blockade.
5. **Climate** — After COP31 in Antalya ends with no deal, the EU will
   seek an overhaul of how UN climate summits decide.
6. **Asia / NATO** — Several Russian aircraft enter South Korea's air
   defence identification zone; NATO warns it will defend against threats
   in space.

Every fact was checked against public reporting dated 24 November 2026
(AP, Reuters, Just Security, Smithsonian, NPR). Nothing in the image is
invented: casualty figures, names, and quotes are as reported that day,
and the COP31 story is framed as its 24 November fallout (the EU's
response after the Antalya talks ended without a deal), not as the
collapse itself.

## How it runs

`main.py` (Python 3, standard library only) copies the image shipped in
this repository to the output directory and verifies the copy:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.png (1024x1024 PNG, under 1 MiB)
```

It asserts the source exists, is a valid PNG, is at most 1 MiB and at
most 1024x1024 pixels, then verifies the copy is byte-identical by
comparing SHA-256 hashes. The default output directory is `/output`.

## Files

- `output/entry.png` — the front-page image (1024x1024 PNG)
- `main.py` — the entrypoint (copies the image, verifies it)
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
