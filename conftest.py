import pytest
from apps.branches.models import Branch

@pytest.fixture
def create_branch(db):
    """Тестовый филиал"""
    def _make_branch(name='Тестовый филиал', address='Улица, 1', phone='+12345'):
        return Branch.objects.create(name=name, address=address, phone=phone)
    return _make_branch
