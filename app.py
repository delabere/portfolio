from flask import Flask, render_template

app = Flask(__name__)

project_info = {
    # [information about our projects (urls, titles, descriptions, images)]
}


@app.route("/")
def index():
    """This is the main and only page for our portfolio site"""

    return render_template('index.html', project_info=project_info)


if __name__ == "__main__":
    app.run()
