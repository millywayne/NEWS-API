from requests import get_news
from flask import render_template
from app import app
from requests import get_news,get_news, search_news
from flask import render_template, request,redirect,url_for
from .forms import ReviewForm
from app.models import review
Review = review.Review

# Views
@app.main.route('/')
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
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, latest = latest_news, hottest = hottest_news, trending = trending_news)

@app.route('/news/<news_id>')
def news(news_id):

     '''
    View news page function that returns the news details page and its data
    '''
     return render_template('news.html',id = news_id)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns  news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)
    
    return render_template('news.html',id = news_id,  title = title, news = news, reviews = reviews) 

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_format = "+".join(news_name_list)
    searched_news = search_news(news_format)
    title = f'search results for {news_name}'
    return render_template('search.html', title, news = searched_news)      