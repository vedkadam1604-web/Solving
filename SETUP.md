# 🛠️ Setup Guide

Follow these steps to get the contribution agent running in **under 5 minutes**.

---

## Step 1 — Create a new GitHub repository

1. Go to [github.com/new](https://github.com/new)
2. Name it something like `daily-dev-log` or `contribution-agent`
3. Set visibility to **Public** *(required for contributions to count on your profile graph)*
4. **Do NOT** initialise with a README — we'll push one ourselves

> [!IMPORTANT]
> The repo must be **Public** for contributions to appear on your GitHub profile graph.

---

## Step 2 — Copy this project into your new repo

```bash
# Clone this project
git clone https://github.com/YOUR_USERNAME/contribution-agent
cd contribution-agent

# Add the files
cp -r /path/to/this/project/. .

# Push
git add -A
git commit -m "🌱 init: set up contribution agent"
git push -u origin main
```

Or simply push the contents of this folder to your new empty repo.

---

## Step 3 — Enable GitHub Actions permissions

1. Go to your repo → **Settings** → **Actions** → **General**
2. Under **Workflow permissions**, select **Read and write permissions**
3. Click **Save**

> [!IMPORTANT]
> Without this, the workflow cannot push commits back to the repository.

---

## Step 4 — Trigger it manually to test

1. Go to your repo → **Actions** tab
2. Click **🌱 Daily GitHub Contribution Agent** in the left sidebar
3. Click **Run workflow** → **Run workflow**
4. Watch it run — within ~30 seconds you should see a new commit on your repo

---

## Step 5 — You're done! 🎉

The workflow will now run automatically at **09:00, 13:00, and 18:00 UTC** every day, creating 3 commits with varied content. Over a week that's **21 commits** — your contribution graph will stay solidly green.

---

## Customisation

### Change the commit times

Edit [`.github/workflows/daily-contribution.yml`](.github/workflows/daily-contribution.yml) and update the cron expressions:

```yaml
schedule:
  - cron: '0 9 * * *'    # 09:00 UTC
  - cron: '0 13 * * *'   # 13:00 UTC
  - cron: '0 18 * * *'   # 18:00 UTC
```

[Crontab Guru](https://crontab.guru) is handy for writing cron expressions.

### Add your own contribution strategies

Open [`.github/scripts/contribute.py`](.github/scripts/contribute.py) and add a new function following the pattern of existing ones, then add it to the `STRATEGIES` list at the bottom.

---

## FAQ

**Q: Will this affect my streak?**  
A: Yes — commits made by GitHub Actions under your repository count towards your contribution graph as long as the repo is public and the commits are made to the default branch.

**Q: Does it cost anything?**  
A: No. GitHub Actions provides 2,000 free minutes/month for public repositories — this workflow uses about 3 minutes/day, well within the free tier.

**Q: What if I want more commits per day?**  
A: Add more `cron` entries to the workflow's `schedule` section. Each entry is one additional commit per day.
