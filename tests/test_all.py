import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

from blog.models import Article


User = get_user_model()


@pytest.mark.django_db
def test_user_fixture(user):
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_read_time_property(article):
    content = article.content.split()
    word_count = len(content)
    expected_read_time = word_count // 200
    assert article.get_read_time == expected_read_time


@pytest.mark.django_db
def test_articles_view(client, article_factory):
    a = article_factory.create_batch(100)
    for article in a:
        print(article.image.path)
    response = client.get(reverse('article_list'))
    assert response.status_code == 200
    assert len(response.context['articles']) == 100
    assert Article.objects.all().count() == 100
