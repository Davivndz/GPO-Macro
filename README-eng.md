# GPO Sentinel - Computer Vision Automation (v9.2)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-stable-green.svg)
![UI](https://img.shields.io/badge/UI-Tkinter-black.svg)

**GPO Sentinel** is a high-performance automation tool developed in Python, specifically designed to optimize cycles in Grand Piece Online's (Roblox) Battle Royale mode. The project leverages **Computer Vision** for real-time decision-making and hardware-level emulation to interact seamlessly with the 3D environment.

## 🚀 Technical Highlights

* **Sentinel Vision:** Unlike time-based macros, Sentinel uses advanced image recognition (OpenCV/PyAutoGUI) to identify match states, server status (Match Found), and end-game triggers.
* **Hardware Emulation:** Powered by the `pydirectinput` library to send low-level input commands (Scancodes), bypassing standard software-input blocks implemented by game engines.
* **Safe Loading Logic:** Features 105s safety buffers and dynamic wait loops to handle network latency and asset loading variations effectively.
* **Visual Debug GUI:** An intuitive Tkinter-based interface providing real-time coordinate feedback and a comprehensive match cycle counter.

## 🛠️ Tech Stack

* **Python 3.10+**
* **PyAutoGUI / OpenCV:** Pattern recognition and computer vision.
* **PyDirectInput:** Low-level hardware input emulation.
* **Pynput:** Mouse event management for coordinate calibration.
* **Keyboard:** Global hooks for system-wide Hotkeys (F1/F2).
* **Tkinter:** Custom graphical user interface.

## 📋 Quick Start Guide

### 1. File Preparation
* **Extract All:** Do not run the bot directly from the `.zip` file. Extract all contents to a dedicated folder on your Desktop.
* **Dependencies:** Ensure the `.exe` and the image assets (`btn_open.png`, `match_found.png`, etc.) are located in the same directory.

### 2. Game Configuration
* **Display Mode:** Set Roblox to **Windowed** or **Borderless Windowed** mode.
* **Resolution:** Optimized for standard resolutions (e.g., 1920x1080). If buttons are not detected, capture custom screenshots of the UI elements and replace the default `.png` files using the same filenames.

### 3. Calibration (Mandatory)
Before starting, the bot must be calibrated to your monitor's coordinates:
1.  Run `GPO_Macro.exe` as **Administrator**.
2.  Navigate to the game's main menu.
3.  In the Macro UI, click the **MAP** button next to "1. Queue", then click the corresponding button within the game.
4.  Repeat this for all 5 actions in the list.
5.  Calibration is complete when all coordinates turn **GREEN**.

### 4. Controls
* **START (F1):** Initiates the automated cycle (Queue -> Match Wait -> Stat Upgrade -> Combat/M1 Spam -> Post-match reset).
* **STOP (F2):** Kill-switch. Immediately halts all mouse and keyboard actions.

## 🧠 Engineering Vision

This project was built with a focus on **stability and scalability**. The architecture decouples the interface logic (Main Thread) from the execution logic (Worker Thread), ensuring the GUI remains responsive even during intensive visual processing tasks.

---
*Disclaimer: This software is a technical study of automation and computer vision. Usage in online environments must comply with the platform's terms of service.*
