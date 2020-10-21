from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

News = news.News

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results =(news_results_list)


    return news_results

def process_results(news):
    '''
     Function  that processes the news result and transform them to a list of Objects

    Args:
        news: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_items in news:
        id = news_items.get('id')
        title = news_items.get('original_title')
        overview = news_items.get('overview')
        poster = news_items.get('poster_path')
        vote_average = news_items.get('vote_average')
        vote_count = news_items.get('vote_count')

        if poster:
            news_object = News(id,title,overview,poster,vote_average,vote_count)
            news_results.append(news_object)

    return news_results