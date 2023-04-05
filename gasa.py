from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate_lyrics', methods=['POST'])
def generate_lyrics():
    input_text = request.form.get('input_text')
    openai_api_key = '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'

    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'prompt': input_text,
        'temperature': 0.7,
        'max_tokens': 2048,
        'top_p': 1,
        'frequency_penalty': 0,
        'presence_penalty': 0
    }

    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return jsonify(result)
    else:
        return jsonify({'error': 'Failed to generate lyrics'}), 400

if __name__ == '__main__':
    app.run(debug=True)
