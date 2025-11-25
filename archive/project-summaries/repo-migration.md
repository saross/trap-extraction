# Repository Migration Plan: claude_extraction to Standalone Repository

**Date:** 23 November 2025
**Issue:** Git repository accidentally initialised in parent directory (TRAP-WD-2020-04) instead of claude_extraction/ subdirectory
**Goal:** Migrate claude_extraction/ to new location as standalone repository with preserved history

---

## Current Situation

**Current repository structure:**
```
/media/shawn/.../TRAP-WD-2020-04/          ← Git repo root (incorrect)
├── .git/
├── .gitignore
├── claude_extraction/                      ← Should be repo root
│   ├── archive/
│   ├── inputs/
│   ├── outputs/
│   ├── scripts/
│   └── README.md
├── Kazanluk/                               ← Excluded via .gitignore
├── FinalData/                              ← Excluded via .gitignore
└── [other source data directories]        ← Excluded via .gitignore
```

**GitHub remote:** git@github.com:saross/trap-extraction.git

**Problem:** Repository root is one level too high, making the directory structure awkward and preventing easy relocation of claude_extraction/ folder.

---

## Recommended Approach: Git Filter-Repo Method

**Advantages:**
- Preserves complete commit history
- Clean, professional result
- GitHub repository remains at same URL
- All commits properly attributed

**Requirements:**
- `git-filter-repo` tool (install via pip: `pip install git-filter-repo`)
- OR use built-in `git subtree split` (slower but no installation needed)

---

## Migration Steps

### Option A: Using git-filter-repo (Recommended - Fastest)

#### Prerequisites

1. **Install git-filter-repo:**
   ```bash
   pip install git-filter-repo
   ```

2. **Choose new location for claude_extraction:**
   ```bash
   # Example new locations:
   # ~/projects/trap-extraction/
   # /path/to/new/location/trap-extraction/
   ```

#### Migration Process

**Step 1: Create fresh clone of current repository**
```bash
# Clone to temporary location
cd /tmp
git clone git@github.com:saross/trap-extraction.git trap-extraction-temp
cd trap-extraction-temp
```

**Step 2: Extract claude_extraction/ as repository root**
```bash
# Rewrite history to make claude_extraction/ the root directory
git filter-repo --path claude_extraction/ --path-rename claude_extraction/:
```

This command:
- Keeps only commits that touched claude_extraction/
- Moves all files from claude_extraction/ to repository root
- Preserves complete commit history and authorship
- Removes .git/config (you'll need to re-add remote)

**Step 3: Verify the result**
```bash
# Check that repository root now contains the right files
ls -la
# Should see: archive/, inputs/, outputs/, scripts/, README.md, etc.

# Check commit history is intact
git log --oneline
# Should see all your commits with proper messages
```

**Step 4: Re-add GitHub remote and force push**
```bash
# Add back the remote
git remote add origin git@github.com:saross/trap-extraction.git

# Force push to replace GitHub history
git push --force --set-upstream origin master
```

⚠️ **Warning:** `--force` will overwrite GitHub repository history. Ensure no one else has cloned it yet.

**Step 5: Move to final location**
```bash
# Move the cleaned repository to desired location
mv /tmp/trap-extraction-temp /path/to/new/location/trap-extraction

# Verify it works
cd /path/to/new/location/trap-extraction
git status
git remote -v
```

**Step 6: Clean up old repository**
```bash
# Back on the original drive, remove the old .git directory
cd /media/shawn/.../TRAP-WD-2020-04
rm -rf .git .gitignore

# Now claude_extraction/ and siblings are just regular directories
# Move claude_extraction/ content to new location if needed
# Delete or keep source data directories as needed
```

---

### Option B: Using git subtree split (No Installation Required)

If you can't install git-filter-repo, use this built-in Git method:

**Step 1: Extract subdirectory to new branch**
```bash
cd /media/shawn/.../TRAP-WD-2020-04

# Extract claude_extraction/ history to new branch
git subtree split --prefix=claude_extraction -b claude-extraction-only
```

**Step 2: Create new repository from branch**
```bash
# Create new directory at target location
mkdir -p /path/to/new/location/trap-extraction
cd /path/to/new/location/trap-extraction

# Initialize new repository
git init

# Pull the extracted history
git pull /media/shawn/.../TRAP-WD-2020-04 claude-extraction-only
```

**Step 3: Connect to GitHub and force push**
```bash
git remote add origin git@github.com:saross/trap-extraction.git
git push --force --set-upstream origin master
```

**Step 4: Clean up old repository**
```bash
cd /media/shawn/.../TRAP-WD-2020-04
git branch -D claude-extraction-only  # Delete temporary branch
rm -rf .git .gitignore                 # Remove git from parent directory
```

---

### Option C: Fresh Start (Simplest but Loses Detailed History)

If preserving individual commit history isn't critical:

**Step 1: Copy files to new location**
```bash
# Copy claude_extraction to new location
cp -r /media/shawn/.../TRAP-WD-2020-04/claude_extraction /path/to/new/location/trap-extraction
cd /path/to/new/location/trap-extraction
```

**Step 2: Initialize new repository**
```bash
git init
git add .
git commit -m "feat: Initial commit - TRAP extraction project with 100% walker data coverage

Complete archaeological survey attribution dataset from TRAP 2009-2011 seasons.

Key achievements:
- 268/268 records with complete walker data (100% coverage)
- 17 backup files preserving extraction history
- 6 Python extraction/quality scripts
- Comprehensive documentation and reports
- All extractions verified against source diaries

Previous work history preserved in archive/cc-interactions/ and reports.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Step 3: Force push to GitHub**
```bash
git remote add origin git@github.com:saross/trap-extraction.git
git push --force --set-upstream origin master
```

**Step 4: Clean up old location**
```bash
cd /media/shawn/.../TRAP-WD-2020-04
rm -rf .git .gitignore
```

---

## Verification Checklist

After migration, verify:

- [ ] Repository root contains: archive/, inputs/, outputs/, scripts/, README.md
- [ ] No claude_extraction/ parent directory visible
- [ ] `git log` shows commit history (Options A & B) or single commit (Option C)
- [ ] `git remote -v` shows correct GitHub URL
- [ ] Can `git pull` and `git push` successfully
- [ ] GitHub repository displays correctly at https://github.com/saross/trap-extraction
- [ ] All files present: attribution.csv, scripts, archive content
- [ ] Old .git directory removed from TRAP-WD-2020-04

---

## Post-Migration Actions

**1. Update local development setup:**
```bash
# Update your working directory path
cd /path/to/new/location/trap-extraction

# Verify Python scripts still work
python3 scripts/check_current_failed_extractions.py
```

**2. Update any documentation referencing old paths**

**3. Add repository description on GitHub:**
- Go to https://github.com/saross/trap-extraction/settings
- Add description: "TRAP Archaeological Survey Attribution Data Extraction (2009-2011)"
- Add topics: archaeology, data-extraction, field-survey, python, trap

**4. Consider adding repository README badges:**
```markdown
[![DOI](https://zenodo.org/badge/...svg)](https://zenodo.org/...)
[![License](https://img.shields.io/badge/License-...-blue.svg)](LICENSE)
```

---

## Recommended Option

**Use Option A (git-filter-repo)** if possible:
- ✅ Cleanest result
- ✅ Preserves complete history
- ✅ Fastest execution
- ✅ Professional repository structure

**Use Option B (git subtree)** if you can't install git-filter-repo:
- ✅ Preserves complete history
- ✅ No additional tools needed
- ⚠️ Slower than Option A

**Use Option C (fresh start)** only if:
- ⚠️ You don't need individual commit history
- ✅ You want the simplest process
- ✅ Quick and guaranteed to work

---

## Timeline Estimate

**Option A:** 15-30 minutes
**Option B:** 30-45 minutes
**Option C:** 10-15 minutes

---

## Risks and Mitigation

**Risk: Lose commit history**
- **Mitigation:** Test with temporary clone first
- **Mitigation:** Keep backup of original .git directory until verified

**Risk: Break GitHub connection**
- **Mitigation:** Document current remote URL before starting
- **Mitigation:** Use `git remote -v` to verify after migration

**Risk: Force push to wrong repository**
- **Mitigation:** Verify remote URL before `git push --force`
- **Mitigation:** Check GitHub repository page after push

---

## Backup Strategy

**Before starting migration:**

1. **Backup current .git directory:**
   ```bash
   cd /media/shawn/.../TRAP-WD-2020-04
   cp -r .git .git.backup-$(date +%Y%m%d)
   ```

2. **Backup claude_extraction directory:**
   ```bash
   tar -czf claude_extraction-backup-$(date +%Y%m%d).tar.gz claude_extraction/
   ```

3. **Note current GitHub state:**
   ```bash
   git log --oneline > git-log-backup-$(date +%Y%m%d).txt
   git remote -v > git-remote-backup-$(date +%Y%m%d).txt
   ```

---

## Questions to Answer Before Migration

1. **Where is the new location?**
   - [ ] Same machine, different directory?
   - [ ] Different drive?
   - [ ] Different machine entirely?

2. **What happens to source data directories?**
   - [ ] Keep Kazanluk/, FinalData/, etc. on current drive?
   - [ ] Move to different location?
   - [ ] Delete after migration?

3. **Is anyone else using this repository?**
   - [ ] Solo project (safe to force push)
   - [ ] Shared (need to coordinate force push)

4. **Do you need detailed commit history?**
   - [ ] Yes → Use Option A or B
   - [ ] No → Use Option C

---

## Support Commands

**Check what git filter-repo would do (dry run):**
```bash
git filter-repo --path claude_extraction/ --path-rename claude_extraction/: --dry-run
```

**View repository size before/after:**
```bash
du -sh .git
```

**Verify commit count preserved:**
```bash
# Before migration
git rev-list --count HEAD

# After migration (should be same or fewer, but not zero)
git rev-list --count HEAD
```

---

## Conclusion

This migration will:
- Fix the repository structure issue
- Allow claude_extraction to be a standalone, relocatable repository
- Maintain professional commit history (Options A & B)
- Enable easy removal from current drive

The repository will have a cleaner structure matching its GitHub name and purpose.

**Recommended:** Option A with git-filter-repo for best results.

---

**Document prepared:** 23 November 2025
**Next step:** Choose migration option and schedule execution time
