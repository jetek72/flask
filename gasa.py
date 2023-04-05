from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/generate_lyrics', methods=['POST'])
def generate_lyrics():
    input_text = request.form.get('input_text')
    headers = {
        'Authorization': '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',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "prompt": input_text,
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, data=json.dumps(data))
    response_json = response.json()

    if 'choices' in response_json:
        generated_lyrics = response_json['choices'][0]['text']
        return jsonify({'generated_lyrics': generated_lyrics.strip()})
    else:
        return jsonify({'error': 'Failed to generate lyrics'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
