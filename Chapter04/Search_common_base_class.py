class Content:
    """Common base class for all articles/pages"""
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url

    def print(self):
        """
        Flexible printing function controls output
        """
        print('New article found for topic: {}'.format(self.topic))
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY: {}'.format(self.body))


class Website:
    """Contains information about website structure"""
    def __init__(self, name, url, searchUrl, resultListing, resultUrl,
                 absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

if __name__ == '__main__':
    content = Content('aa', 'bb', 'cc', 'dd')

