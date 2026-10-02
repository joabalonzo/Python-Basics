
git --version
→ Check if Git is installed.

# Clone Repository

git clone REPOSITORY-LINK
→ Download repository to your computer.

# Go inside repository
cd REPOSITORY-NAME

→ Enter the repository folder.

# Open VS Code
code .
→ Open current folder in VS Code.





# Check repository connection
git remote -v
→ Shows which GitHub repository you're connected to.
`origin` = GitHub repository**

### Login
git push
→ Git may ask you to log in/authenticate.



# 1. Check changes
git status
→ See what you changed.

# 2. Add changes
git add .
→ Prepare all changes.

# 3. Commit
git commit -m "Add reviewer"
→ Save your changes.

# 4. Push
git push
→ Send changes to GitHub.






git log --oneline -3


→ Shows your latest 3 commits.





bash
git status
git add .
git commit -m "My changes"
git push




| Command         | Meaning            |
| --------------- | ------------------ |
| `git clone`     | Get repository     |
| `cd`            | Go inside          |
| `code .`        | Open VS Code       |
| `git remote -v` | Check connection   |
| `git status`    | Check changes      |
| `git add .`     | Prepare changes    |
| `git commit`    | Save changes       |
| `git push`      | Send to GitHub     |
| `git log`       | See commit history |

---

# IF SOMETHING GOES WRONG

git bash
git status
git remote -v
git log --oneline -3


→ Check these first.

