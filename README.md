# 🌡️ Automated Temperature Data Collector

*Reliable web scraping solution for automated temperature monitoring using Selenium WebDriver*

## 📌 About 

This script automatically:
1. Launches a configured Chrome browser instance
2. Navigates to `http://automated.pythonanywhere.com`
3. Extracts the current temperature value
4. Returns cleaned numerical data

Perfect for:
- Environmental monitoring systems
- Data logging applications
- IoT temperature tracking

## ⚙️ Installation

1. Ensure Chrome is installed
2. Install requirements:
```bash
pip install selenium==4.0.0
```
3. Download matching [ChromeDriver](https://chromedriver.chromium.org/)

## 🚀 Running the Script

Execute directly:
```bash
python main.py
```

Sample successful output:
```text
23.7  # Current temperature in °C
```
