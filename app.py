from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
default_key = '1'
cache = {default_key: 'one'}

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
		cache[key] = request.form['cache_value']

	cache_value = None;
	if key in cache:
		cache_value = cache[key]

	return render_template('second-index.html', key=key, cache_value=cache_value)


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)
