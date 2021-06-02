

from django.test import TestCase

from accounts.models import Profile


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Profile.objects.create(email='guido@django.com', password='Django1234')

    def test_email(self):
        profile = Profile.objects.get(id=1)
        email = profile.email
        self.assertEquals(email, 'guido@django.com')

    def test_email_unique(self):
        profile = Profile.objects.get(id=1)
        unique = profile._meta.get_field('email').unique
        self.assertEquals(unique, True)

    def test_email_error_messages_unique(self):
        profile = Profile.objects.get(id=1)
        error_messages_unique = profile._meta.get_field('email').error_messages['unique']
        self.assertEquals(error_messages_unique, 'A profile with that email already exists.')

    def test_email_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('email').max_length
        self.assertEquals(max_length, 254)

    def test_password(self):
        profile = Profile.objects.get(id=1)
        password = profile.password
        self.assertEquals(password, 'Django1234')

    def test_password_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('password').max_length
        self.assertEquals(max_length, 128)

    def test_object_str(self):
        profile = Profile.objects.get(id=1)
        object_str = profile.__str__()
        self.assertEquals(object_str, f"Profil {profile.pk}: {profile.email}")
