import requests
from flask import Flask, render_template, request
from form import Research, Upload
from image_analysis import describe_image, analyze_image
from flask_bootstrap import Bootstrap
import config.azure_config as azure_config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ErnR468dnezfheI3FUbeehui3'
Bootstrap(app)


az = azure_config.AzureServices()

@app.route('/', methods=['GET'])
def homee():
    return "hello world ba"

@app.route('/home', methods=['GET'])
def home():

    form = Research(request.form)
    form.tags.data = az.get_tags()
    return render_template('/form_tags.html', form=form)


@app.route('/all_images', methods=['GET'])
def all_images():

    img = az.get_all_pictures()
    return render_template('/all_images.html', form=img)


@app.route('/set_picture', methods=['POST'])
def set_picture():
    tags = request.form.getlist('tags')
    img = az.find_picture(tags)
    return str(img)
    return render_template('/set_picture.html', img=img, tags=tags)


@app.route('/upload_with_url', methods=['GET', 'POST'])
def upload_file():
    form = Upload(request.form)
    return render_template('/form_img_url.html', form=form)


@app.route('/upload_from_file', methods=['GET', 'POST'])
def upload_url():
    form = Upload(request.form)
    return render_template('/form_img_file.html', form=form)


@app.route('/upload_done', methods=['GET', 'POST'])
def upload_done():
    if request.method == 'POST':
        if request.form:
            url = request.form['imageUrl']
            name = request.form['imageName']
            description = request.form['imageDescription']
            print(url)
            # az.insert_pictures(name, description, url)
    return render_template('/uploaded.html', url=url, name=name, description=description)


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True, use_debugger=True, use_reloader=True)
    app.run(host='localhost', debug=True, port=5001)
