# Scraper

## Files
Consists of a minimal server and a scraper

## Setup
*optionally use a venv*
pip install -r requirements.txt
py server.py

## Use
```
curl http://localhost:5000/alive

curl -X POST http://localhost:5000/scrape -H "Content-Type: application/json" -d '{"uri": "https://wikipedia.org"}'
```

