import factory
from django.contrib.auth import get_user_model
from .models import Author, Article


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('text')
    birth_date = factory.Faker('date_of_birth')


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
    
    image = factory.django.ImageField(color='blue', width=800, height=600, format='jpeg')
    author = factory.SubFactory(AuthorFactory)
    title = factory.Faker('sentence', nb_words=6, locale='fr_FR')
    slug = factory.Faker('slug')
    content = factory.Faker('text', max_nb_chars=10000, locale='fr_FR')
    view_count = factory.Faker('random_int', min=0, max=1000)
