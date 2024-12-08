class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Article title should be a string.")
        if not (5<= len(title) <=50):
            raise Exception("Article title should be between 5 to 50 characters, inclusive.")
        if not isinstance(author, Author):
            raise Exception("Article's author should be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise Exception("Article's magazine should be an instance of the Magazine class.")
        self._author = author
        self._magazine = magazine
        self._title = title

        magazine._articles.append(self)
        if self not in author._articles:
            author._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Article's author should be an instance of the Author class.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("Article's author should be an instance of the Author class.")
        self._magazine = new_magazine
    
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_author_name):
        # Prevent changes to the name attribute
        if hasattr(self, "_name"):
            raise Exception("Cannot modify name after it has been set.")
        self._name = new_author_name

    def articles(self):
        return self._articles


    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        if article not in self._articles:
            self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    all = []
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Magazine name should be a string.")
        if not (2 <= len(name) <= 16):
            raise Exception("Magazine Name should be between 2 and 16 characters, inclusive.")
        if not isinstance(category, str):
            raise Exception("Magazine category should be a string.")
        if len(category) == 0:
            raise Exception("Magazine category must be longer than zero characters.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_magazine_name):
        if not isinstance(new_magazine_name, str):
            raise Exception("Magazine name should be a string.")
        if not (2 <= len(new_magazine_name) <= 16):
            raise Exception("Magazine Name should be between 2 and 16 characters, inclusive.")

        self._name = new_magazine_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise Exception("Magazine category should be a string.")
        if len(new_category) == 0:
            raise Exception("Magazine category must be longer than zero characters.")

        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1

        result = [author for author, count in author_counts.items() if count > 2]

        return result if result else None

    # @classmethod
    # def top_publisher(cls):
    #     if not  cls.all:
    #         return None
    #     else:
    #         return cls.all

    # Tried to access the magazine with the highest number of articles published using the class attribute.


