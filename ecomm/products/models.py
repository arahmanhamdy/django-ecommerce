from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField


@python_2_unicode_compatible
class ProductCategory(models.Model):
    name = models.CharField(_('name'), max_length=255)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def get_absolute_url(self):
        return "product:category_detail", [self.slug]

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'))
    price = models.FloatField(_('price'))
    category_id = models.ForeignKey(ProductCategory, verbose_name=_('category'))
    slug = AutoSlugField(populate_from='name')
    is_featured = models.BooleanField(verbose_name=_('Featured?'), default=False)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def get_absolute_url(self):
        return "product:product_detail", [self.slug]

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/', verbose_name=_("Image"))
