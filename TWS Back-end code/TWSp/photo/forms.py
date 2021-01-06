from django.forms import inlineformset_factory
from photo.models import Category, Product

ProductInlineFormSet = inlineformset_factory(Category, Product,
        fields = ['pname', 'pcost', 'pimage',
              'pcontent', 'psize', 'pweight', 'pship', 'pstore'],
                                           extra = 2)