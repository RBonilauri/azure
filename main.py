import requests
from flask import Flask, render_template, request
from form import Research
from flask_bootstrap import Bootstrap
import config.azure_config as azure_config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ErnR468dnezfheI3FUbeehui3'
Bootstrap(app)


@app.route('/', methods=['GET'])
def home():

    form = Research(request.form)

    tags = ["Poire","Pêche","Steak"]

    #form.tag.data = azure_config.AzureServices().get_tags()

    return render_template('/form_tags.html',tags=tags, form=form)

@app.route('/picture', methods=['POST'])
def picture():
    if request.method == 'POST':
        request.g

        pass
    pass


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    pass


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True, use_debugger=True, use_reloader=True)
    app.run(host='localhost', debug=True, port=5001)
