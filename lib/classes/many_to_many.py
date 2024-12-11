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

# Test case

# Comprehensive Test Cases for Article, Author, and Magazine Classes

def test_case():

# Create authors
    print("Creating Authors...")
    author1 = Author("Alice Becker")
    author2 = Author("Charles Johnson")
    print(f"Author 1: {author1.name}")
    print(f"Author 2: {author2.name}")

    # Test attempting to modify author name
    print("\nTesting immutability of Author name...")
    try:
        author1.name = "Jane Doe"
    except Exception as e:
        print(f"Expected Error: {e}")

    # Create magazines
    print("\nCreating Magazines...")
    mag1 = Magazine("Tasty Times", "Food")
    mag2 = Magazine("Explorer Journal", "Travel and Adventure")
    print(f"Magazine 1: {mag1.name}, Category: {mag1.category}")
    print(f"Magazine 2: {mag2.name}, Category: {mag2.category}")

    # Test setting invalid magazine attributes
    print("\nTesting invalid magazine name and category...")
    try:
        mag1.name = "T"  # Invalid name (too short)
    except Exception as e:
        print(f"Expected Error: {e}")

    try:
        mag1.category = ""  # Invalid category (empty)
    except Exception as e:
        print(f"Expected Error: {e}")

    # Create articles
    print("\nCreating Articles...")
    article1 = Article(author1, mag1, "5 Quick and Healthy Breakfast Recipes")
    article2 = Article(author1, mag1, "Exploring the World of Fermented Foods")
    article3 = Article(author2, mag2, "Top 5 Beaches for a Dream Vacation")
    article4 = Article(author2, mag2, "A Guide to Road Trips Across Europe")
    print(f"Article 1: '{article1.title}', Author: {article1.author.name}, Magazine: {article1.magazine.name}")
    print(f"Article 2: '{article2.title}', Author: {article2.author.name}, Magazine: {article2.magazine.name}")
    print(f"Article 3: '{article3.title}', Author: {article3.author.name}, Magazine: {article3.magazine.name}")
    print(f"Article 4: '{article4.title}', Author: {article4.author.name}, Magazine: {article4.magazine.name}")

    # Test creating an invalid article
    print("\nTesting invalid article creation...")
    try:
        invalid_article = Article("NotAnAuthor", mag1, "Invalid Article")
    except Exception as e:
        print(f"Expected Error: {e}")

    # Testing Author Methods
    print("\nTesting Author methods...")
    print(f"Author 1 Articles: {[article.title for article in author1.articles()]}")
    print(f"Author 2 Articles: {[article.title for article in author2.articles()]}")
    print(f"Author 1 Magazines: {[magazine.name for magazine in author1.magazines()]}")
    print(f"Author 2 Magazines: {[magazine.name for magazine in author2.magazines()]}")
    print(f"Author 1 Topic Areas: {author1.topic_areas()}")
    print(f"Author 2 Topic Areas: {author2.topic_areas()}")

    # Testing Magazine Methods
    print("\nTesting Magazine methods...")
    print(f"Magazine 1 Articles: {[article.title for article in mag1.articles()]}")
    print(f"Magazine 2 Articles: {[article.title for article in mag2.articles()]}")
    print(f"Magazine 1 Contributors: {[contributor.name for contributor in mag1.contributors()]}")
    print(f"Magazine 2 Contributors: {[contributor.name for contributor in mag2.contributors()]}")
    print(f"Magazine 1 Article Titles: {mag1.article_titles()}")
    print(f"Magazine 2 Article Titles: {mag2.article_titles()}")
    print(f"Magazine 1 Contributing Authors (with >2 articles): {[author.name for author in mag1.contributing_authors() or []]}")
    print(f"Magazine 2 Contributing Authors (with >2 articles): {[author.name for author in mag2.contributing_authors() or []]}")

    # Creating additional articles to test contributing_authors method
    print("\nAdding additional articles to test contributing authors with >2 articles...")
    Article(author2, mag1, "How to Make Artisan Bread")
    Article(author2, mag1, "The Science of Sourdough")
    print(f"Updated Magazine 1 Contributing Authors: {[author.name for author in mag1.contributing_authors() or []]}")

    # Verifying the class attribute for magazines
    print("\nTesting class attribute 'all' for Magazine...")
    print(f"All Magazines: {[mag.name for mag in Magazine.all]}")

    # Verifying the class attribute for articles
    print("\nTesting class attribute 'all' for Article...")
    print(f"All Articles: {[article.title for article in Article.all]}")

test_case()

