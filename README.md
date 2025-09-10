# AI-Powered-Google-Maps-Scraper-with-Playwright-OpenAI

## 📌 Problem
Scraping Google Maps is notoriously difficult because:
- The HTML structure of search results is unorganized.
- Attribute keys change frequently, which breaks traditional scrapers.
- Google actively tries to prevent automated extraction.

This means a one-time script often fails quickly as Google updates its DOM.

## 💡 Solution
This project demonstrates how to **combine Playwright automation and generative AI** to extract structured business data from Google Maps.

The workflow is split into two main steps:
1. **Automated Collection with Playwright**  
   - Launches a browser using Playwright.  
   - Navigates to Google Maps with a given search query (e.g., "Bakeries in Chicago").  
   - Scrolls through the results and saves the results list into a clean **HTML snapshot**.  

2. **Data Parsing with AI + BeautifulSoup**  
   - Loads the saved HTML file.  
   - Uses BeautifulSoup to extract raw text content.  
   - Sends the extracted text to the **OpenAI API** to parse unstructured listings into structured **JSON records**.  
   - Converts the final dataset into a **CSV file** with fields like:  
     - Business Name  
     - Rating  
     - Reviews  
     - Price  
     - Category  
     - Location  
     - Hours  
     - Services  
     - Actions (e.g., order, book directly on Google Maps)

## ⚙️ Tech Stack
- **Python**
- [Playwright](https://playwright.dev/python/) – automated browser control  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing  
- [OpenAI API](https://platform.openai.com/) – generative AI for structured parsing  
- [Pandas](https://pandas.pydata.org/) – exporting JSON → CSV  

## 🚀 Usage
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/google-maps-playwright-scraper.git
   cd google-maps-playwright-scraper
