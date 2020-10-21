from requests import get_news
from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    latest_news = get_news('latest')
    print(latest_news)
    hottest_news = get_news('hottest')
    trending_news = get_news('trending')
    title = 'Home - Welcome to The latest News Review Website Online'
    return render_template('index.html', title = title, latest = latest_news, hottest = hottest_news, trending = trending_news)

@app.route('/news/<news_id>')
def news(news_id):

     '''
    View news page function that returns the news details page and its data
    '''
     return render_template('news.html',id = news_id)

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('movie.html',id = news_id)    