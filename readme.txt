🔗 Python QR Code Generator

A lightweight, beginner-friendly Python CLI application that converts URLs or text into QR code images and saves them as PNG files.

Built with: Python · qrcode · Pillow

📌 Overview

This project demonstrates how to build a practical Python utility using user input, string manipulation, conditional logic, and an external image-generation library.
Enter your content, choose a filename, and generate a QR code in seconds.

✨ Features
Instant QR generation — convert URLs or text into QR codes.
Custom filenames — choose a name for your output image.
PNG output — save generated QR codes as image files.
Automatic extension handling — append .png when the filename doesn't already have that extension.
Simple CLI — no complicated setup or graphical interface required.
🛠️ Tech Stack
Technology	Purpose
Python 3	Core application logic
qrcode	QR code generation
Pillow	Image processing and PNG output
Git & GitHub Version control and project hosting
🚀 Getting Started
Prerequisites
Python 3 installed
pip package installer
Git (optional, for cloning the repository)
1. Clone the repository
bash
git clone https://github.com/YOUR-USERNAME/python-qr-code-generator.git
cd python-qr-code-generator


Replace YOUR-USERNAME with your GitHub username.

Alternatively, download the repository as a ZIP file.

2. Create a virtual environment (recommended)
bash
python -m venv .venv


Activate it:

Windows

bash
.venv\Scripts\activate


macOS / Linux

bash
source .venv/bin/activate

3. Install dependencies
bash
pip install -r requirements.txt

4. Run the application
bash
python main.py

💻 Example
text
Enter the URL: https://github.com
Enter the filename: github
QR code saved as github.png


The generated github.png image will be saved in the application's current working directory.

Scan the image using your phone's camera or a QR code reader to access the encoded content.


