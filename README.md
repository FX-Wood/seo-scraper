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

# output
{
  "meta": [
    ...
    {
      "content": "Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation.",
      "name": "description",
      "property": null
    },
    ...
    {
      "content": "Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation.",
      "name": null,
      "property": "og:description"
    },
    {
      "content": "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
      "name": null,
      "property": "og:image"
    }
  ]
}
```

