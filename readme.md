# 🧠 Number Guessing Game (CLI)
---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CLI-Interactive-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Rich-Console%20Colors-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

---

A fun CLI-based number guessing game built in Python — with colors, difficulty levels, a timer, and replay support. Simple, fast, and surprisingly addictive.

---

## 🔥 Preview

> 🎥 Replace this GIF link with your own terminal recording later.

<p align="center">
  <img src="https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif" width="500" alt="Number Guessing Game Preview">
</p>



## 🎮 Features

- ✅ Interactive CLI gameplay
- 🎯 3 difficulty levels: Easy, Medium, Hard
- 🔢 Random number between **1 and 100**
- 🕒 Timer to measure how long you take to guess
- 🔁 Option to play multiple rounds
- 🎨 Colored output using [`rich`](https://github.com/Textualize/rich)
- 🚫 Handles invalid numeric input gracefully

---

## 🧩 How It Works

```text
1. Game starts
2. You choose a difficulty level
3. The computer thinks of a number between 1 and 100
4. You start guessing
5. You get hints: "Too high" / "Too low"
6. You either:
   - Guess correctly → Win + see attempts + time
   - Run out of attempts → Lose and see the correct number
7. You choose to play again or quit
