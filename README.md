[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/kkazushi-eng/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/kkazushi-eng/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# Nov 18, 2026 — Three Powers, One Table

An entry for make.fun's [news-image-20261118](https://make.fun/bounty/news-image-20261118):
sum up the world's news of Wednesday 18 November 2026 in one image.

## The image

A front-page editorial cartoon dated **NOV 18, 2026**, headlined
**"THREE POWERS, ONE TABLE"**.

The centrepiece is the day's dominant story: at the APEC summit in Shenzhen,
China's Xi Jinping and Russia's Vladimir Putin met on 18 November, and US
President Donald Trump arrived in China for the first-ever trilateral
US–China–Russia summit scheduled for the next day. The three leaders are
shown shaking hands at one round table in front of the US, Chinese and
Russian flags, under a banner reading "APEC SHENZHEN — TRUMP · XI · PUTIN",
with a globe on the table.

Three panels along the bottom carry the day's other headline stories:

- **IRAN DRONES OVER GULF** — Iran said it launched drones at US installations
  at Kuwait's Ali Al Salem Air Base, Bahrain reported interceptions, and US
  aircraft struck a missile site on Iran's Qeshm Island.
- **GTA VI AFTER 13 YEARS** — Grand Theft Auto VI launched at midnight,
  13 years after the previous main installment.
- **NVIDIA BEATS $115B** — Nvidia reported quarterly revenue of $115.8 billion,
  beating forecasts in its first earnings report since Jensen Huang's exit.

## How it runs

`python3 main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR` when
that variable is set). It is deterministic: two runs write identical bytes.
The image is a 1024×1024 PNG, well under the 1 MiB limit.

## License

MIT — see `LICENSE`.
