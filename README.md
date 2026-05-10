# SCRIPT: Documentation Upgrade to Version 2.0
# ACTION: Reflecting the evolution from Version 1.0

new_readme = """
# Mini ATM System (Version 2.0) 🚀

I have successfully upgraded this project from Version 1.0! This version marks a major step forward in my Python learning journey.

## ✅ New in Version 2.0
- **Transaction History:** Now tracks all deposits and withdrawals during the session.
- **Improved Input Validation:** Uses `.isdigit()` to prevent crashes from non-numeric inputs.
- **Enhanced UI:** Cleaner terminal menus and status icons ([✓], [!], [i]).

## 🚀 Features
- **Security:** PIN-protected login.
- **Transactions:** Check balance, deposit funds, and withdraw cash.
- **Formatting:** Currency is displayed with two decimal places for a professional look.

## 🛠️ Python Topics Mastered
- Variables (Strings, Floats, Integers)
- While Loops & Control Flow (Break/Continue)
- List Operations (`append` and iteration)
- Error Prevention & Conditional Logic

## 🔮 Roadmap: Version 3.0
- [ ] **Data Persistence:** Saving balance and history to a `.txt` or `.json` file.
- [ ] **Security+:** Limit PIN login attempts (e.g., 3 strikes).
- [ ] **Multi-User:** Support for multiple accounts/PINs.

---
*Evolved and coded by a dedicated Python learner.*
"""

def publish_v2_docs():
    print("[SYSTEM] Archive: Version 1.0 documentation moved to history.")
    print("[SYSTEM] Active: Version 2.0 README is now live.")
    print("\n" + new_readme)

publish_v2_docs()
