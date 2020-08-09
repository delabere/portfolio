from flask import Flask, render_template
import os

app = Flask(__name__)

project_info = [
    {
        "title": "Pizza-Shop",
        "image_url": "https://raw.githubusercontent.com/delabere/Pizza-Delivery-DjangoApp/master/img/pizza_store.png",
        "description": "A Django based Pizza ordering site. Customers can order food and admins can manage those orders.",
        #"description": "This is an example pizza shop website which allows you do order custom pizzas, subs, pastas, salads and platters of food!",
        #"repo_url": "https://github.com/delabere/Pizza-Delivery-DjangoApp",
        "repo_url": "http://pizza.delabere.com",
        "project_url": None,
    },
    {
        "title": "Gif-Chat",
        "repo_url": "http://chat.delabere.com",
        "image_url": "https://raw.githubusercontent.com/delabere/Gif-Chat-FlaskApp/master/gif-chat.jpeg",
        "description": "This is a Flask-powered realtime chat application which using web-sockets and JavaScript on the front-end.",
        #"repo_url": "https://github.com/delabere/Gif-Chat-FlaskApp",
        "project_url": None,
    },
    {
        "title": "Sentimento",
        "image_url": "https://github.com/delabere/Sentimento-FlaskApp/blob/master/sentimento/Sentimento-FrontPage.png?raw=true",
        "description": "This is a pet project for creating an interactive dashboard running sentiment analysis over API data using the Google News API and the Google Sentiment API using Flask, Pandas, and Plotly.",
        "repo_url": "http://sentimento.delabere.com/",
        #"repo_url": "https://github.com/delabere/Sentimento-FlaskApp",
        "project_url": None,
    },
    {
        "title": "Over-Booked",
        "image_url": "https://github.com/delabere/Over-Booked-FlaskApp/raw/master/overbooked/Over-Booked.png",
        "description": "Over-Booked is a fully responsive website that allows you to search information and leave reviews for thousands of books!",
        "repo_url": "http://overbooked.delabere.com/",
        #"repo_url": "https://github.com/delabere/Over-Booked-FlaskApp",
        "project_url": None,
    },
]


@app.route("/")
def index():
    """This is the main and only page for our portfolio site"""

    return render_template("index.html", project_info=project_info)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
