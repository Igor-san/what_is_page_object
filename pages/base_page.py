
class BasePage():
    '''
    Base Class
    '''
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        '''
        Open url in browser
        '''
        self.browser.get(self.url)