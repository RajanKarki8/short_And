import string
from flask import Flask, request, render_template, redirect
import random

app = Flask(__name__)

urls_mapping = {}

@app.route('/')
def homebase():
    return render_template('main.html')

def make_short_url():
    var_chars = string.ascii_letters+string.digits+string.punctuation
    return ''.join(random.choice(var_chars) for _ in range(6))
    
@app.route('/test_url', methods = ['post'])
def final_url():
    real_url = request.form['url']
    short = make_short_url()
    urls_mapping[short]=real_url
    return render_template('result.html', short=short)

@app.route('/<short>')
def redirect_url(short):
    real_url = urls_mapping.get(short)
    if real_url:
        return redirect(real_url, code=301)
    else:
        return 'url not found', 404

if __name__ == '__main__':
    app.run(debug=True)












