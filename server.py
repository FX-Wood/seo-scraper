from flask import Flask, request, jsonify
from scraper import get_scrape

app = Flask(__name__)

@app.route('/alive')
def alive():
    return 'alive'

@app.route('/scrape', methods=['POST'])
def scrape():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    
    if 'uri' not in data:
        return jsonify({"error": "No uri to scrape provided"}), 400

    meta_tags = get_scrape(data['uri'])
    
    return jsonify({"meta": meta_tags})

if __name__ == '__main__':
    app.run(debug=True)
