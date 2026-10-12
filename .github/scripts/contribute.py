#!/usr/bin/env python3
"""
Daily GitHub Contribution Agent
Picks a random contribution type and updates/creates files to generate
natural-looking commits.
"""

import random
import json
import os
from datetime import datetime, timezone
from pathlib import Path

# ── Contribution strategies ─────────────────────────────────────────────────

def update_journal(now: datetime):
    """Append a timestamped entry to the dev journal."""
    path = Path("journal") / f"{now.strftime('%Y-%m')}.md"
    path.parent.mkdir(exist_ok=True)

    entries = [
        "Reviewed recent changes and refactored small utility functions.",
        "Explored new library patterns and took notes on best practices.",
        "Cleaned up comments and improved inline documentation.",
        "Investigated performance bottlenecks; added benchmarking notes.",
        "Worked through some algorithm puzzles to stay sharp.",
        "Read through open-source contributions for inspiration.",
        "Outlined feature ideas and captured them in the journal.",
        "Debugged a tricky edge case — added a note for future reference.",
        "Reviewed pull request patterns and took notes.",
        "Studied system design concepts; summarised key points.",
    ]

    entry = random.choice(entries)
    timestamp = now.strftime("%Y-%m-%d %H:%M UTC")
    line = f"\n## {timestamp}\n\n{entry}\n"

    with open(path, "a") as f:
        f.write(line)

    print(f"📓 Updated journal: {path}")


def update_stats(now: datetime):
    """Update a JSON stats file with daily activity metrics."""
    path = Path("stats") / "activity.json"
    path.parent.mkdir(exist_ok=True)

    data = json.loads(path.read_text()) if path.exists() else {"total_commits": 0, "sessions": []}

    data["total_commits"] += 1
    data["last_active"] = now.isoformat()
    data["sessions"].append({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M"),
        "type": "auto-commit",
        "score": random.randint(1, 10),
    })

    # Keep only last 200 sessions
    data["sessions"] = data["sessions"][-200:]

    path.write_text(json.dumps(data, indent=2))
    print(f"📊 Updated stats: {path}")


def update_readme(now: datetime):
    """Update the README's last-active badge timestamp."""
    path = Path("README.md")
    today = now.strftime("%Y--%m--%d")   # double dashes for shields.io URL encoding
    badge_line = (
        f"![Last Active](https://img.shields.io/badge/last--active-{today}-brightgreen)\n"
    )

    if path.exists():
        lines = path.read_text().splitlines(keepends=True)
        # Replace badge line if it exists, else prepend
        new_lines = [badge_line if line.startswith("![Last Active]") else line for line in lines]
        if badge_line not in new_lines:
            new_lines.insert(0, badge_line + "\n")
        path.write_text("".join(new_lines))
    else:
        path.write_text(
            f"# 🌱 Contribution Agent\n\n"
            f"{badge_line}\n"
            f"This repository is maintained by an automated contribution agent.\n"
        )

    print(f"📝 Updated README badge")


def update_notes(now: datetime):
    """Add a random dev note to the notes directory."""
    topics = [
        ("algorithms", [
            "Binary search works on sorted arrays in O(log n).",
            "Merge sort is stable and runs in O(n log n).",
            "Dijkstra's algorithm requires non-negative edge weights.",
            "Dynamic programming avoids recomputation via memoisation.",
            "A heap is a complete binary tree satisfying the heap property.",
        ]),
        ("python", [
            "Use `dataclasses` to auto-generate `__init__`, `__repr__`, and `__eq__`.",
            "`functools.lru_cache` is great for caching recursive calls.",
            "Generator expressions are memory-efficient alternatives to list comprehensions.",
            "`pathlib.Path` is the modern way to handle file paths.",
            "Type hints improve readability and enable static analysis.",
        ]),
        ("system-design", [
            "CAP theorem: a distributed system can only guarantee two of consistency, availability, partition tolerance.",
            "Load balancers distribute requests across multiple servers.",
            "Horizontal scaling adds more machines; vertical scaling adds more resources to one machine.",
            "Message queues decouple producers from consumers.",
            "CDNs cache static assets closer to end users.",
        ]),
    ]

    topic, notes = random.choice(topics)
    note = random.choice(notes)
    today = now.strftime("%Y-%m-%d")

    path = Path("notes") / f"{topic}.md"
    path.parent.mkdir(exist_ok=True)

    with open(path, "a") as f:
        f.write(f"\n### {today}\n\n- {note}\n")

    print(f"🗒️  Updated note: {path}")


def update_ideas(now: datetime):
    """Append a random project idea or todo."""
    path = Path("ideas.md")
    ideas = [
        "Build a CLI tool to visualise git history as a flamegraph.",
        "Create a browser extension that highlights deprecated APIs.",
        "Write a script that auto-generates release notes from PR titles.",
        "Experiment with WASM for running Python in the browser.",
        "Build a tiny static site generator in under 200 lines.",
        "Make a personal dashboard that tracks reading progress.",
        "Automate dependency updates with a custom bot.",
        "Write a fuzzer for a config parser to catch edge cases.",
        "Create a VS Code extension that times how long you spend per file.",
        "Build a tool that scores code readability automatically.",
    ]

    idea = random.choice(ideas)
    today = now.strftime("%Y-%m-%d")

    with open(path, "a") as f:
        f.write(f"\n- **{today}**: {idea}\n")

    print(f"💡 Updated ideas.md")


# ── Main ────────────────────────────────────────────────────────────────────

STRATEGIES = [update_journal, update_stats, update_readme, update_notes, update_ideas]

def main():
    now = datetime.now(timezone.utc)
    # Pick 1–2 strategies per run for variety
    count = random.randint(1, 2)
    chosen = random.sample(STRATEGIES, k=count)
    for strategy in chosen:
        strategy(now)

if __name__ == "__main__":
    main()
