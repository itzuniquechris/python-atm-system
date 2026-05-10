# 🏧 Python BootCamp ATM (Version 2.0)

A lightweight, terminal-based ATM simulator built with Python. This project demonstrates core programming logic, user input handling, and state management.

## 🌟 What's New in v2.0
- **Transaction History:** Added tracking for deposits and withdrawals during the active session.
- **Robust Validation:** Implemented `.isdigit()` checks to prevent system crashes on invalid inputs.
- **Enhanced UI:** Added status icons (`[✓]`, `[!]`, `[i]`) and improved menu formatting for a better user experience.

## 🚀 Features
- **Secure Access:** PIN-protected entry system.
- **Financial Operations:** 
  - Real-time balance inquiries.
  - Instant deposits with automated balance updates.
  - Withdrawal system with **insufficient funds** protection.
- **Logging:** View a summary of all transactions performed during the session.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Logic used:** 
  - `while` loops for continuous session management.
  - `list` structures for transaction logging.
  - `f-strings` for precise currency formatting (`.2f`).
  - Conditional branching for transaction rules.

## 📂 Project Structure
- `balance`: Tracks current liquid funds (Float).
- `deposit[]` / `withdraw[]`: List-based storage for session history.
- `correct_pin`: Hardcoded security key for authentication.

## 🌱 Future Roadmap (v3.0)
- [ ] **Data Persistence:** Save user data to a `.txt` file to keep balances after restart.
- [ ] **Security Lock:** Automatic lockout after 3 failed PIN attempts.
- [ ] **Multiple Users:** Transition from hardcoded values to a dictionary-based user database.

---
*Created as part of my Python learning journey. Feel free to explore the code!*
