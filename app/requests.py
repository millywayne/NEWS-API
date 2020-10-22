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

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('original_title')
            overview = news_details_response.get('overview')
            poster = news_details_response.get('poster_path')
            vote_average = news_details_response.get('vote_average')
            vote_count = news_details_response.get('vote_count')

            news_object = News(id,title,overview,poster,vote_average,vote_count)

    return news_object

def search_news(news_name):
    search_news_url = 'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=487c722040f046eaa31635a68e73583c={}&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news = search_news_response['results']
            search_news_results = process_results()


    return search_news_results