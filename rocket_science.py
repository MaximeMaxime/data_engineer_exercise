from numpy.random import uniform

class article_classifier(object):
    """ article_classifier outputs an interest level (0-1) for a given text
    ------------------
    :params article_id (integer) : Article Identifier
    :params user_id (integer) : User Identifier

    :return interest_level :(float)  The interest level

    ------------------
    Example Usage : 

    article_id = 123
    user_id = 358
    response = article_classifier().run(article_id=article_id, user_id=user_id)
    print response
    """
    def __init__(self):
        pass

    def run(self, article_id, user_id):
        article_text = self.get_article(article_id)
        result = self.classifier(article_text, user_id)
        self.store_result(article_id, user_id, result)
        return result


    def get_article(self, article_id):
        """ This method should fetch the article's text and return it as a string """
        raise Exception("You must implement the get_article() method which fetches the article's text and returns it as a string")

    @staticmethod
    def classifier(article_text, user_id):
        """ Our research has proven that whether the level of interest correlates with :
            whether the user_id is odd or even and the length of the article's text """
        if user_id % 2 == 0:
            if len(article_text.split(" ")) % 2 == 0:
                return uniform(0,1,1)[0]
            else:
                return 0    
        else:
            if len(article_text) > 120:
                return 1
            else:
                return uniform(0,1,1)[0]

    def store_result(user_id, article_id, result):
        """ This method should store the result in the storage engine """
        raise Exception("You must implement the store_result() method which stores the result in the storage engine")