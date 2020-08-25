class book:
    def __init__(self, title, author, publisher, price, royalty):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.royalty = royalty
    @classmethod
    def royalty(num_of_copies):
        if(num_of_copies<=500):
            royalty = 0.1*self.price
        elif(num_of_copies<=1000):
            royalty = 0.125*self.price
        else:
            royalty = 0.15*self.price

class ebook(EPUB,
