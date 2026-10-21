# DevOps Practical Assignment 01: Git Version Control Workflow, Command Suite & GitHub Pages Deployment

**Student Name:** Rutuja Deepak Jagtap  
**PRN:** `123B1B146` | **Batch:** `C1`  
**Department:** Computer Engineering, PCCOE Pune  
**Academic Year:** 2026–2027  
**Official Curriculum Code:** `BCE27PE01` / `CE-4202`  

---

## 1. Aim
To explore the different Git commands for working with local repositories, remote repositories, and log operations (including `add`, `commit`, `status`, `log`, `show`, `branch`, `checkout`/`switch`, `merge`, `clone`, `pull`, `reset`, `revert`, `rebase`), enforce semantic version control discipline, isolate feature development using non-fast-forward merges (`--no-ff`), and publish a live responsive DevOps practical portfolio via GitHub Pages.

---

## 2. Learning Objectives
1. **Core Git Operations:** Master the 3-tree architecture (Working Directory, Staging Area / Index, HEAD Repository).
2. **Commit Hygiene:** Author atomic, descriptive semantic commits following conventional specifications (`feat:`, `chore:`, `docs:`, `fix:`).
3. **Branching Strategy:** Create isolated feature branches, execute 3-way non-fast-forward merges (`git merge --no-ff`), and visualize directed acyclic graphs (DAG).
4. **Disaster Recovery & History Rewriting:** Learn safe undo strategies using `git revert` (preserving history) vs `git reset` (manipulating HEAD).
5. **Remote Synchronization:** Configure authenticated remotes, fetch upstream commits, and push tracked branches to GitHub.
6. **Web Portfolio & GitHub Pages:** Build a responsive zero-framework web portfolio in HTML5/CSS3/JavaScript and host it live.

---

## 3. Theoretical Background

### 3.1 Git 3-Tree Architecture
Git manages project files through three internal states:
1. **Working Directory:** The local file system where files are authored and edited.
2. **Staging Area (Index):** A binary file (`.git/index`) containing a list of paths and SHA-1/SHA-256 object hashes that will form the next commit snapshot.
3. **Repository (HEAD):** The immutable object database containing commit objects, trees, and blobs that constitute the project history.

```
+--------------------+        git add        +--------------------+       git commit       +--------------------+
| Working Directory  | --------------------> |    Staging Area    | ---------------------> |  Git Repository    |
| (Unstaged Files)   | <-------------------- |   (Indexed Blobs)  | <--------------------- |    (HEAD Commit)   |
+--------------------+      git restore      +--------------------+      git restore       +--------------------+
                             --staged                                    --source=HEAD
```

### 3.2 Non-Fast-Forward Merge (`--no-ff`)
When merging a feature branch with no divergent commits on `main`, Git default is to fast-forward the branch pointer. Using `git merge --no-ff` creates an explicit merge commit having two parent commit hashes:
- Preserves the chronological lifecycle of the feature branch.
- Makes grouping and auditing of features transparent in `git log --graph`.
- Permits clean atomic rollbacks via `git revert -m 1 <merge_commit_sha>`.

---

## 4. Key Git Commands Reference

| Command | Category | Functionality |
| :--- | :--- | :--- |
| `git init -b main` | Repository Setup | Initializes a new local Git repository with default branch named `main`. |
| `git clone <url>` | Remote Sync | Clones a complete remote repository with full history into a local directory. |
| `git status -s` | Inspection | Displays compact status of tracked, modified, and untracked files. |
| `git add <files>` | Staging | Stages modifications into the Git Index. |
| `git commit -m "<msg>"` | Staging | Creates an immutable commit snapshot from staged files. |
| `git log --graph --oneline` | History | Renders a visual ASCII graph of branch divergence and merge history. |
| `git show <commit>` | Inspection | Shows detailed patch diff and metadata for a specific commit object. |
| `git switch -c <branch>` | Branching | Creates and checks out a new branch in a single command. |
| `git merge --no-ff <branch>` | Integration | Merges branch into current branch with an explicit merge commit. |
| `git stash` / `git stash pop` | Workspace | Temporarily shelves uncommitted changes to work on a clean tree. |
| `git revert <commit>` | Recovery | Creates a new commit that inverts the changes of an earlier commit safely. |
| `git reset --soft/hard` | History Edit | Moves HEAD pointer back; `--hard` discards working directory changes. |
| `git remote add origin <url>` | Remote Sync | Associates the local repo with a remote GitHub repository. |
| `git push -u origin main` | Remote Sync | Pushes local commits to remote and sets upstream tracking. |

---

## 5. Step-by-Step Hands-On Execution Guide

### Step 1: Run the Automated Verification Script
Run the automated simulation script to create a clean sandbox repo, test all 11 Git operations, and render the DAG graph:
```powershell
powershell -ExecutionPolicy Bypass -File scripts/simulate_git_workflow.ps1
```

### Step 2: Test Interactive Git Commands
```powershell
# Check current repository status
git status

# Inspect authentic commit history
git log --graph --oneline --all

# View the feature branch merge commit
git show 2aca92c
```

---

## 6. Verification Evidence
1. **Repository Status:** `screenshots/proof_01_git_status_init.png`
2. **Commit DAG Graph:** `screenshots/proof_02_git_commit_graph.png`
3. **Feature Branch & Merge:** `screenshots/proof_03_git_branch_merge.png`
4. **Remote Push Verification:** `screenshots/proof_04_git_push_remote.png`
5. **Live Portfolio Dark:** `screenshots/proof_05_portfolio_desktop_dark.png`
6. **Live Portfolio Light:** `screenshots/proof_06_portfolio_desktop_light.png`
7. **Assignments Grid:** `screenshots/proof_07_portfolio_assignments_grid.png`
8. **Interactive Modal:** `screenshots/proof_08_portfolio_quick_modal.png`
9. **Mobile Responsive Layout:** `screenshots/proof_09_portfolio_mobile_view.png`

---

## 7. Viva Voce Questions & Answers

**Q1: What is the difference between `git revert` and `git reset`?**  
*Answer:* `git reset` modifies the commit history by moving the HEAD and branch pointer backward, effectively erasing commits from the current branch history. `git revert` creates a brand-new commit that applies the inverse diff of a target commit, making it safe for public/shared branches because it does not rewrite history.

**Q2: What is the benefit of a 3-tree architecture in Git?**  
*Answer:* It decouples file authoring from commit staging. The Index allows developers to craft fine-grained, atomic semantic commits by staging only relevant lines or files, rather than committing everything in the working tree at once.

**Q3: How does `git merge --no-ff` differ from a default fast-forward merge?**  
*Answer:* A fast-forward merge simply slides the branch pointer forward without creating a commit object. A `--no-ff` merge generates a dedicated merge commit with two parents, preserving the feature branch's existence and facilitating rollback.

**Q4: How does GitHub Pages serve static web applications?**  
*Answer:* GitHub Pages is an automated static hosting service that listens to pushes on the designated branch (`main`). It serves static assets (HTML, CSS, JS, images) directly over HTTPS without requiring server-side runtime containers.

---

## 8. Conclusion
Mastery of Git command-line operations, 3-tree mechanics, semantic commits, feature branching, and non-fast-forward merging was achieved. The personal DevOps portfolio was deployed to GitHub Pages and is accessible at:  
👉 **[https://rutujadeepakjagtap.github.io/DevOps/](https://rutujadeepakjagtap.github.io/DevOps/)**
