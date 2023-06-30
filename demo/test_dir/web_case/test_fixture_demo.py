import seldom


class BaiduTest(seldom.TestCase):
    """
    * start_class/end_class
    * start/end
    """

    @classmethod
    def start_class(cls):
        """start class"""
        print("test class start")
        cls.max_window()
        cls.sleep(3)

    @classmethod
    def end_class(cls):
        """end class"""
        ...

    def start(self):
        """start"""
        print("test case start")
        self.index_page = "https://www.baidu.com/"
        self.news_page = "https://news.baidu.com/"
        self.sleep(5)
    def end(self):
        """end"""
        ...

    def test_open_index(self):
        """open baidu index page"""
        self.open(self.index_page)
        self.sleep(5)
    def test_open_news(self):
        """"open baidu news page"""
        self.open(self.news_page)
        self.sleep(5)

if __name__ == '__main__':
    seldom.main(debug=True)
