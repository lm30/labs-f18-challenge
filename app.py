from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<int:num>', methods=['GET'])
def poke_num(num):
	r = requests.get("https://www.pokeapi.co/api/v2/pokemon/" + str(num) + "/")
	return render_template("pokedex.html", id=num, name=(r.json()["name"]), getid="true")

@app.route('/pokemon/<string:name>', methods=['GET'])
def poke_name(name):
	r = requests.get("https://www.pokeapi.co/api/v2/pokemon/" + name + "/")
	return render_template("pokedex.html", id=(r.json())["forms"][0]["url"].split("/")[-2], name=name)

if __name__ == '__main__':
    app.run()