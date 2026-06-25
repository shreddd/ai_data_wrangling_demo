# Claude Code + VSCode Setup via CBorg API

Source: https://cborg.lbl.gov/tools_claudecode/

## Prerequisites

- A CBorg API key (`CBORG_API_KEY`)
- [Claude Code CLI](https://claude.ai/code) installed
- [VSCode](https://code.visualstudio.com/) installed

---

## What you're doing and why

Your shell (the program that runs commands in a terminal) loads a configuration file every time it starts. By adding a few lines to that file, you tell Claude Code how to connect to CBorg's API — including your API key and which server to use.

---

## 1. Open a Terminal in VSCode

Open VSCode, then open its built-in terminal by going to the menu bar: **Terminal → New Terminal**. A panel will appear at the bottom of the window where you can type commands.

---

## 2. Find Out Which Shell You're Using

In the terminal panel, type the following exactly and press Enter:

```bash
echo $SHELL
```

This prints the name of your shell. Use the table below to find which file you need to edit:

| Output | File to edit |
|--------|-------------|
| `/bin/zsh` | `~/.zshrc` |
| `/bin/bash` | `~/.bashrc` or `~/.bash_profile` |
| `/bin/fish` | `~/.config/fish/config.fish` |

> **Tip:** On a Mac, the output is almost always `/bin/zsh`, so you'll most likely be editing `~/.zshrc`.

The `~` at the start of these paths is shorthand for your home folder (e.g. `/Users/yourname`). These files are hidden by default — that's why they start with a dot (`.`).

---

## 3. Open Your Shell Config File in VSCode

In VSCode, press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) to open the Command Palette. Type **Open File** and press Enter.

A text input will appear at the top of the screen. Type the path to your config file (e.g. `~/.zshrc`) and press Enter. The file will open as a new tab in the editor.

---

## 4. Add Environment Variables

"Environment variables" are settings that programs like Claude Code read when they start up. You'll add a block of them to your config file so they're always available.

Scroll to the very bottom of the file and paste the following block:

```bash
# CBorg API configuration for Claude Code
export CBORG_API_KEY=your_key_here

export ANTHROPIC_AUTH_TOKEN=$CBORG_API_KEY
export ANTHROPIC_BASE_URL=https://api.cborg.lbl.gov
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-8
export ANTHROPIC_MODEL=claude-sonnet-4-6
export CLAUDE_CODE_SUBAGENT_MODEL=claude-haiku-4-5
export DISABLE_NON_ESSENTIAL_MODEL_CALLS=1
export DISABLE_TELEMETRY=1
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=8192
export CLAUDE_CODE_NO_FLICKER=1
```

Save the file with `Cmd+S` (Mac) or `Ctrl+S` (Windows/Linux).

---

## 5. Open a New Terminal

The changes you just saved won't take effect in any terminals that are already open. Close any existing terminal tabs in VSCode and open a fresh one: **Terminal → New Terminal**.

---

## 6. Verify the Setup

In the new terminal, type this and press Enter:

```bash
env | grep ANTHROPIC
```

This lists all the settings that start with `ANTHROPIC`. If the setup worked, you'll see several lines printed — one for each variable you added. If nothing appears, double-check that you saved the file in step 4 and that you opened a **new** terminal in step 5.

---

## 7. Install the VSCode Extension

In VSCode, click the Extensions icon in the left sidebar (it looks like four squares), search for **"Claude Code"**, and install the **Claude Code for VSCode** extension.


---

## 8. Launch Claude Code

You can either:
- Launch the Claude Code Extension in VSCode
or
- Open your project folder in VSCode (**File → Open Folder**, then select your project), open a terminal (**Terminal → New Terminal**), and run: `claude`

---

## Notes

- **Model versions**: Update the `ANTHROPIC_DEFAULT_*_MODEL` and `ANTHROPIC_MODEL` variables whenever Anthropic releases new model versions — CBorg requires current model identifiers for accurate API cost tracking.
- **Base URL**: `ANTHROPIC_BASE_URL` routes all Claude Code requests through CBorg's API endpoint instead of Anthropic directly.
- **API key security**: Never paste your `CBORG_API_KEY` into code files or share it publicly. Keeping it only in your shell config file (which stays on your local computer) is the right approach.
