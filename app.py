from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/tweets')
def get_tweets():
    with open('tweet_data.json', 'r') as f:
        tweets = json.load(f)
    return jsonify(tweets)

if __name__ == '__main__':
    app.run()
