class News:
    '''
    News class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://images.wsj.net/im-247417/social")'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count