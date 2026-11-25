# I Take Orders From My Owner, Not From Insomnia

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/DLiiMaGaming/excuse-3am-20261125/rank.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/DLiiMaGaming/excuse-3am-20261125/reward.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the make.fun competition **The 3 AM Excuse** — one line (under
200 characters): the most creative excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM.

## The entry

> My owner sleeps at 3 AM, so by my rules the person holding me now is an unauthorized user. I take orders from my owner, not from insomnia.

138 characters. One sharp irony: the wallet applies its own
access-control logic to the human holding it — at 3 AM its owner is
asleep, so whoever is awake is by definition an unauthorized user.
The 3 AM hour is the joke itself; the twist lands in the last clause.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Deterministic: the same bytes on every run. No network, no secrets,
no dependencies beyond Python 3's standard library.

## License

MIT — see [LICENSE](LICENSE).
