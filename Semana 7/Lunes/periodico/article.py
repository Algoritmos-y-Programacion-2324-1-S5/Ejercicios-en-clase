class Article:
    def __init__(self,title, sumup,body,images,date,writer):
        self.title = title
        self.sumup = sumup
        self.body = body
        self.images = images
        self.publish_date = None
        self.create_date = date
        self.writer = writer

    def show_article(self):
        return f"Title: {self.title} \nBody: {self.body}\nAuthor:{self.writer.show_employee()}"
    
    def set_publish_date(self, date):
        self.publish_date = date