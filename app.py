from flask import Flask, jsonify, request, render_template
import redis

app = Flask(__name__)
default_key = '1'
cache = redis.Redis(host='redis', port=6379, db=0)
cache.set(default_key, 'one')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/2')
def hello_People():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})

@app.route('/storage', methods=['GET', 'POST'])
def mainpage():

	key = default_key
	if 'key' in request.form:
		key = request.form['key']

	if request.method == 'POST' and request.form['submit'] == 'save':
		cache.set(key, request.form['cache_value'])

	cache_value = None;
	if cache.get(key):
		cache_value = cache.get(key).decode('utf-8')

	return render_template('second-index.html', key=key, cache_value=cache_value)


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)
