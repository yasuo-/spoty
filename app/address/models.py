from django.db import models
from django.utils.translation import gettext_lazy as _

class Region(models.Model):
    """
    エリア地方
    """
    name = models.CharField(_("Region Name"), max_length=50)
    name_kana = models.CharField(_("Region Name Kana"), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'region'

    def __str__(self):
        """show main key and name"""
        return "{}: {}".format(self.pk, self.name)


class Prefecture(models.Model):
    """
    都道府県
    """
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="エリア地方 id")
    code = models.CharField(max_length=2, blank=True, null=True, verbose_name="都道府県コード")
    name = models.CharField(max_length=255, verbose_name="地方名")
    name_kana = models.CharField(max_length=255, verbose_name="地方名かな")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'prefecture'

    def get_region_id(self) -> int:
        return self.region.id

    def get_region_name(self) -> str:
        return self.region.name

    def __str__(self):
        """show main key and name"""
        return "{}: {}".format(self.code, self.name)


class City(models.Model):
    """
    市区町村マスタ
    """
    prefecture = models.ForeignKey(Prefecture, on_delete=models.PROTECT, verbose_name="都道府県 id")
    code = models.CharField(max_length=6, verbose_name="団体コード", primary_key=True)
    name = models.CharField(max_length=60, verbose_name="市区町村 name")
    name_kana = models.CharField(max_length=200, verbose_name="市区町村 かな")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'city'

    def get_prefecture_id(self) -> int:
        return self.prefecture.id

    def get_prefecture_code(self) -> str:
        return self.prefecture.code

    def get_prefecture_name(self) -> str:
        return self.prefecture.name

    def get_full_address_name(self) -> str:
        full_address_name = '%s%s' % (self.prefecture.name, self.name)
        return full_address_name.strip()

    def __str__(self):
        """show main key and name"""
        return "{}: {}".format(self.code, self.name)


class Address(models.Model):
    """
    address 
    """
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="City id")
    address1 = models.CharField(_("address1"), max_length=500)
    address2 = models.CharField(_("address2"), max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'address'

    def __str__(self):
        """show main key and name"""
        return "{}: {}".format(self.address1, self.address2)