
from django.test import TestCase

from catalog.forms import HomeSearchForm, NavSearchForm


class HomeSearchFormTest(TestCase):

    def test_homesearch_field_in_fields(self):
        form = HomeSearchForm()
        self.assertTrue(form.fields['search'])

    def test_homesearch_field_is_not_required(self):
        form = HomeSearchForm()
        self.assertFalse(form.fields['search'].required)

    def test_homesearch_field_widget(self):
        form = HomeSearchForm()
        self.assertEqual(form.fields['search'].widget.attrs, {'placeholder': 'produit ou catégorie'})


class NavSearchFormTest(TestCase):

    def test_navsearch_field_in_fields(self):
        form = NavSearchForm()
        self.assertTrue(form.fields['search'])

    def test_navsearch_field_is_not_required(self):
        form = NavSearchForm()
        self.assertFalse(form.fields['search'].required)

    def test_navsearch_field_widget(self):
        form = NavSearchForm()
        self.assertEqual(form.fields['search'].widget.attrs, {'placeholder':'chercher'})
