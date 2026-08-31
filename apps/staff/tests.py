import pytest
from apps.staff.models import Master
from apps.branches.tests import Branch
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.
@pytest.mark.django_db
class TestMaster:

    def test_avatar_upload_path(self, create_branch):
        branch = create_branch()
        dummy_image = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
        )

        fake_avatar = SimpleUploadedFile(
            name='test_avatar.gif',
            content=dummy_image,
            content_type='image/gif'
        )

        master = Master.objects.create(name='Ирина', branch=branch, avatar=fake_avatar)

        assert master.avatar.name.startswith('masters/avatar/')
        assert 'test_avatar' in master.avatar.name

    def test_str_returns_name(self, create_branch):
        branch = create_branch()
        master = Master.objects.create(name='Ирина', branch=branch)

        assert str(master) == 'Ирина'
