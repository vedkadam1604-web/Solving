#!/usr/bin/env python3
"""
Generates a natural-looking commit message for the daily contribution.
"""

import random
import sys
from datetime import datetime, timezone

PREFIXES = ["chore", "docs", "notes", "update", "refactor", "log", "track"]

MESSAGES = [
    "update dev journal with daily notes",
    "add daily activity log entry",
    "update README with latest activity badge",
    "add notes on algorithm patterns",
    "track daily progress and ideas",
    "log daily session and metrics",
    "update stats with today's activity",
    "append new ideas to backlog",
    "add system design study notes",
    "update python tips and tricks",
    "record daily development session",
    "add daily code exploration notes",
    "track progress on personal projects",
    "update contribution log",
    "add morning coding session notes",
    "append afternoon dev notes",
    "log evening development activity",
]

def main():
    prefix = random.choice(PREFIXES)
    msg = random.choice(MESSAGES)
    now = datetime.now(timezone.utc)

    # Occasionally add emoji for variety
    emoji_prefix = random.choice(["", "✨ ", "📝 ", "🔧 ", "📊 ", "💡 ", "🌱 ", ""])

    print(f"{emoji_prefix}{prefix}: {msg}")

if __name__ == "__main__":
    main()
