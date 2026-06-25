# Claude Code + VSCode Setup via CBorg API

Source: https://cborg.lbl.gov/tools_claudecode/

## Prerequisites

- A CBorg API key (see Step 0 below)
- [Python 3.8 or later](https://www.python.org/downloads/) installed — after installing, confirm it's working by opening a terminal and running `python3 --version` (Mac/Linux) or `python --version` (Windows). You should see a version number printed.
- [Claude Code CLI](https://claude.ai/code) installed
- [VSCode](https://code.visualstudio.com/) installed

---

## Step 0. Get Your CBorg API Key

Go to [https://api.cborg.lbl.gov/key/manage](https://api.cborg.lbl.gov/key/manage) and log in with your LBNL credentials.

If you don't have a key yet, click **Generate Key**. Copy the key and save it somewhere safe — you'll need it in the setup steps below. You won't be able to view the full key again after leaving the page.

---

## What you're doing and why

Programs like Claude Code read "environment variables" when they start up — these are named settings that tell it things like your API key and which server to connect to. This guide shows you how to set those variables so they're available every time you open a terminal.

---

## Setup: Choose Your Operating System

- [Mac or Linux](#mac--linux-setup)
- [Windows](#windows-setup)

---

## Mac / Linux Setup

### Step 1. Open a Terminal in VSCode

Open VSCode, then open its built-in terminal via the menu bar: **Terminal → New Terminal**. A panel will appear at the bottom of the window where you can type commands.

### Step 2. Find Out Which Shell You're Using

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

The `~` is shorthand for your home folder (e.g. `/Users/yourname`). These files are hidden by default — that's why they start with a dot (`.`).

### Step 3. Open Your Shell Config File in VSCode

In VSCode, press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Linux) to open the Command Palette. Type **Open File** and press Enter.

A text input will appear at the top of the screen. Type the path to your config file (e.g. `~/.zshrc`) and press Enter. The file will open as a new tab in the editor.

### Step 4. Add the Configuration

Scroll to the very bottom of the file and paste the following block. Replace `your_key_here` with your actual CBorg API key:

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

Save the file with `Cmd+S` (Mac) or `Ctrl+S` (Linux).

### Step 5. Open a New Terminal

The changes you just saved won't take effect in any terminals that are already open. Close any existing terminal tabs in VSCode and open a fresh one: **Terminal → New Terminal**.

### Step 6. Verify the Setup

In the new terminal, type this and press Enter:

```bash
env | grep ANTHROPIC
```

This lists all settings whose names start with `ANTHROPIC`. If the setup worked, you'll see several lines printed. If nothing appears, double-check that you saved the file in Step 4 and that you opened a **new** terminal in Step 5.

Once verified, skip ahead to [Step 7: Install the VSCode Extension](#step-7-install-the-vscode-extension).

---

## Windows Setup

On Windows, the easiest way to set environment variables is through the Windows Settings interface — no config file editing required.

### Step 1. Open the Environment Variables Window

Click the **Start menu** and search for **"environment variables"**. Click **"Edit the system environment variables"** when it appears.

In the window that opens, click the **"Environment Variables..."** button near the bottom.

### Step 2. Add Each Variable

You'll see two sections: "User variables" (top) and "System variables" (bottom). Work in the **User variables** section.

For each variable in the list below, click **New...**, enter the variable name and value, and click **OK**:

| Variable name | Value |
|---|---|
| `CBORG_API_KEY` | your actual CBorg API key |
| `ANTHROPIC_AUTH_TOKEN` | your actual CBorg API key (same value) |
| `ANTHROPIC_BASE_URL` | `https://api.cborg.lbl.gov` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | `claude-haiku-4-5` |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | `claude-sonnet-4-6` |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | `claude-opus-4-8` |
| `ANTHROPIC_MODEL` | `claude-sonnet-4-6` |
| `CLAUDE_CODE_SUBAGENT_MODEL` | `claude-haiku-4-5` |
| `DISABLE_NON_ESSENTIAL_MODEL_CALLS` | `1` |
| `DISABLE_TELEMETRY` | `1` |
| `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` | `1` |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | `8192` |
| `CLAUDE_CODE_NO_FLICKER` | `1` |

Click **OK** to close each dialog, then **OK** again to close the Environment Variables window, and **OK** once more to close the System Properties window.

> **Note:** `ANTHROPIC_AUTH_TOKEN` should be set to the same value as your `CBORG_API_KEY` — just paste your key in both places.

### Step 3. Open a New Terminal in VSCode

Environment variable changes on Windows only take effect in terminals opened **after** you made the change. Close VSCode completely and reopen it, then open a terminal via **Terminal → New Terminal**.

### Step 4. Verify the Setup

In the terminal, type this and press Enter:

```powershell
Get-ChildItem Env: | Where-Object Name -like 'ANTHROPIC*'
```

You should see a table listing all the `ANTHROPIC` variables you just set. If nothing appears, go back and check that you clicked OK on all the dialogs in Step 2, and that you fully restarted VSCode in Step 3.

---

## Step 7. Install the VSCode Extension

In VSCode, click the Extensions icon in the left sidebar (it looks like four squares), search for **"Claude Code"**, and install the **Claude Code for VSCode** extension.

---

## Step 8. Launch Claude Code

You can either:
- Launch the Claude Code Extension directly within VSCode using the sidebar icon, or
- Open your project folder (**File → Open Folder**, then select your project), open a terminal (**Terminal → New Terminal**), and type `claude`

---

## Notes

- **Model versions**: Update the model name variables whenever Anthropic releases new versions — CBorg requires current model identifiers for accurate API cost tracking.
- **Base URL**: `ANTHROPIC_BASE_URL` routes all Claude Code requests through CBorg's API instead of Anthropic directly.
- **API key security**: Never paste your API key into code files or share it publicly. Keeping it in your shell config (Mac/Linux) or user environment variables (Windows) means it stays on your local machine only.
