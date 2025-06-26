import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.factories import UserFactory, AuthorFactory, ArticleFactory


@pytest.fixture(autouse=True)
def media_root(tmp_path):
    """
    Fixture pour rediriger MEDIA_ROOT vers un répertoire temporaire,
    et restaurer sa valeur initiale après le test.
    """
    # Sauvegarder la valeur initiale de MEDIA_ROOT
    original_media_root = settings.MEDIA_ROOT
    
    # Rediriger MEDIA_ROOT vers le répertoire temporaire
    settings.MEDIA_ROOT = tmp_path
    
    # Fournir le répertoire temporaire au test
    yield tmp_path
    
    # Restaurer la valeur initiale de MEDIA_ROOT
    settings.MEDIA_ROOT = original_media_root


@pytest.fixture
def user():
    user = UserFactory()
    return user


@pytest.fixture
def article():
    article = ArticleFactory()
    return article


@pytest.fixture
def article_factory():
    return ArticleFactory
