from mdblog.app import flask_app
from mdblog.models import db
from mdblog.models import Article

# pip install loremipsum
from loremipsum import get_sentences
import random

# pocet clánkov
COUNT = 47

def create_article(num):
    title = "Article {:02d}".format(num)

    # vygenerobane vetu su v liste.Musím ich spojiť do jedneho stringu
    content = " ".join(get_sentences(random.randint(3,9), True))
    article = Article(title=title, content=content)
    return article

# na prácu s databázou, potrebujeme aplokačný kontext!
with flask_app.app_context():

    # idem v cykle vytvárať články
    for num in range(1, COUNT+1):
        article = create_article(num)
        db.session.add(article)
        db.session.commit()
        print("article #{:02d}".format(num))