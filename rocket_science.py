from numpy.random import uniform

class article_classifier(object):
    """ article_classifier outputs an interest level (0-1) for a given text
    ------------------
    :params article_text: (string) The text of the article
    :return interest_level :(float)  The interest level
    ------------------
    Example Usage : 

    article_text = 'This is an amazing article'
    response = article_classifier(article_text = article_text).run()
    print response
    """
    def __init__(self, article_text):
        self.article_text = article_text

    def run(self):
        return uniform(0,1,1)[0]


