from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from app.address.models import Prefecture, City, Address
from django.urls import reverse


class Host(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("hosts:place_create", kwargs={"host": self.id})

    class Meta:
        db_table = 'hosts'

    def __str__(self):
        return "{}: {}".format(self.pk, self.user)


class Place(models.Model):
    class TimeFrame(models.IntegerChoices):
        QUARTER = 15
        HALF = 30
        THREE_QUARTER = 45
        HOUR = 60

    id = models.AutoField(primary_key=True)
    title = models.CharField(_("Place Title"), null=False, max_length=400)
    body = models.CharField(_("Place Body"), max_length=1000)
    host = models.ForeignKey(Host, related_name='place', on_delete=models.CASCADE, verbose_name="所有者")

    postal_code = models.IntegerField(blank=True, null=True, verbose_name="郵便番号")
    prefecture = models.OneToOneField(Prefecture, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="都道府県")
    city = models.OneToOneField(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="市町村")
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="番地など")

    address1 = models.CharField(_("address1"), max_length=500, null=True)
    address2 = models.CharField(_("address2"), max_length=500, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone")

    time_frame = models.IntegerField(choices=TimeFrame.choices, default=60)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    class Meta:
        db_table = 'places'

    def __str__(self):
        return "{}: {}".format(self.pk, self.title)


class PlaceItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Place Item"), null=False, max_length=400)
    place = models.ForeignKey(Place, related_name='place_item', on_delete=models.CASCADE, verbose_name="場所")
    price_per_time_frame = models.IntegerField(
        verbose_name='時間枠あたりの料金',
        blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(10000)]
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    class Meta:
        db_table = 'place_items'

    def __str__(self):
        return "{}: {}".format(self.pk, self.name)
