# 🕷️ Python Web Scraper – Quotes Edition

## 📌 What is This?

This Python script scrapes **quotes, authors, and tags** from [https://quotes.toscrape.com](https://quotes.toscrape.com), a website made for practicing web scraping.  
It goes through **multiple pages** of quotes and saves the data into a structured **CSV file**.

---

## ❓ What is a Web Scraper?

A **web scraper** is a tool that programmatically visits a website, reads its content (HTML), and extracts specific data like text, prices, or titles.  
This is often used for:
- Market research  
- Competitive analysis  
- Data aggregation  
- Academic research  
---

## ▶️ Features

✅ Scrapes multiple pages (with page limit)  
✅ Extracts quote text, author, and tags  
✅ Saves results to `quotes.csv`  
✅ Handles network errors and empty pages  
✅ Mimics a real browser with headers  
✅ Adds random delay between requests to avoid getting banned

---

## 🚀 How to Run

### 1. Clone or Download the Script

Save the main file as `scraper.py`.

### 2. Install Required Python Packages

```bash
pip install requests beautifulsoup4
```
### DEMO 

<p align="center"><img src = "public/demo1.gif"/></p>