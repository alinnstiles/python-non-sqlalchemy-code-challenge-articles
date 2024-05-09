class Article:

    all=[]
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
        # test this if correct it is
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            print("Title can not be changed")
        elif type(title) != str:
            print ("Title must be of type string")
        elif  len(title) < 5 or len(title) > 50:
            print("Title must be between 5 and 50 characters")
        else:
            self._title =title




class Author:
    def __init__(self, name:str):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name (self, name):
        if hasattr(self, "_name"):
            print ("Name can not be changed")
        elif type(name) != str:
            print("Name must be of type string")
        elif len(name) <= 0:
            print("Name must be longer than 0 characters")
        else:
            self._name = name
        pass

    def articles(self):
        return[article for article in Article.all if article.author == self]
    

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        top_areas_list = list(set([article.magazine.category for article in Article.all if article.author == self]))
        if top_areas_list==[]:
            return None
        else:
            return top_areas_list
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) == str and 2 <= len(name) <=16:
            self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if type(category) == str and 0 < len(category): 
            self._category = category


    def articles(self):
        return[article for article in Article.all if article.magazine == self]
        
    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))
        

    def article_titles(self):
        article_title_list = [article.title for article in Article.all if article.magazine == self]
        if article_title_list==[]:
            return None
        else:
            return article_title_list
    def contributing_authors(self):
        author_list = [article.author for article in Article.all if article.magazine == self]
        author_counts = {}
        contributing_authors = []

        for author in author_list:
            author_counts[author] = author_counts.get(author, 0) + 1

        for author, count in author_counts.items():
            if count > 2:
                contributing_authors.append(author)

        if contributing_authors:
            return contributing_authors
        else:
            return None