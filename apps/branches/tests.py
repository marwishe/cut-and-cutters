import pytest
from apps.branches.models import Branch
# Create your tests here.
@pytest.mark.django_db
class TestBranch:

    def test_str_returns_name(self):
        branch = Branch.objects.create(
            name='Центральный',
            address='ул. Бривибас, 100',
            phone='+37120000000'
        )
        assert str(branch) == 'Центральный'