# 🌱 GitHub Contribution Agent

![Last Active](https://img.shields.io/badge/last--active-2026--10--22-brightgreen)
![Commits Daily](https://img.shields.io/badge/commits-3--5%2Fday-blue)
![Powered by](https://img.shields.io/badge/powered%20by-GitHub%20Actions-black?logo=github-actions)

An automated contribution agent that keeps my GitHub contribution graph active every day.

## How it works

A GitHub Actions workflow runs **3 times a day** (09:00, 13:00, 18:00 UTC) and randomly selects from a set of contribution strategies:

| Strategy | File(s) Updated |
|---|---|
| 📓 Dev Journal | `journal/YYYY-MM.md` |
| 📊 Activity Stats | `stats/activity.json` |
| 📝 README Badge | `README.md` |
| 🗒️ Dev Notes | `notes/<topic>.md` |
| 💡 Ideas Backlog | `ideas.md` |

Each run picks 1–2 strategies at random, creating natural-looking commit variety.

## Setup

See [SETUP.md](SETUP.md) for full setup instructions.
