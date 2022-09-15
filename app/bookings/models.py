from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from hosts.models import Place, PlaceItem


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, verbose_name="予約したユーザー")
    place = models.ForeignKey(Place, related_name='booking', on_delete=models.CASCADE, verbose_name="場所")
    start_date_time = models.DateTimeField(blank=True, null=True, verbose_name="予約開始時間")
    end_date_time = models.DateTimeField(blank=True, null=True, verbose_name="予約終了時間")
    num_time_frame = models.IntegerField(
        verbose_name='時間枠数',
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(50)]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    class Meta:
        db_table = 'bookings'

    def __str__(self):
        return "{}: {}".format(self.pk, self.user)


class BookingStatus(models.Model):
    class Status(models.TextChoices):
        TEMPORARY = "TEMPORARY"
        APPROVAL = "APPROVAL"
        REFUSE = "REFUSE"

    id = models.AutoField(primary_key=True)
    booking = models.OneToOneField(Booking, related_name='booking_status', on_delete=models.CASCADE, verbose_name="予約ID")
    status = models.CharField(choices=Status.choices, default="APPROVAL", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'booking_status'

    def __str__(self):
        return "{}: {}".format(self.booking, self.status)
        

class BookingPrice(models.Model):
    """BookingPrice
    """
    id = models.AutoField(primary_key=True)
    booking = models.OneToOneField(Booking, related_name='booking_price', on_delete=models.CASCADE, verbose_name="予約ID")
    price= models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'booking_price'

    def __str__(self):
        return "{}: {}".format(self.booking, self.price)


class BookingCheckIn(models.Model):
    """BookingCheckIn
    """
    id = models.AutoField(primary_key=True)
    booking = models.OneToOneField(Booking, related_name='booking_checkin', on_delete=models.CASCADE, verbose_name="予約ID")
    checkin = models.DateTimeField(verbose_name="入店時間")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'booking_checkin'

    def __str__(self):
        return "{}: {}".format(self.booking, self.checkin)


class BookingCheckOut(models.Model):
    """BookingCheckOut
    """
    id = models.AutoField(primary_key=True)
    booking = models.OneToOneField(Booking, related_name='booking_checkout', on_delete=models.CASCADE, verbose_name="予約ID")
    checkout = models.DateTimeField(verbose_name="当日のチェックアウト")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'booking_checkout'

    def __str__(self):
        return "{}: {}".format(self.booking, self.checkout)


class Review(models.Model):
    """Review
    """
    id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, related_name='review', on_delete=models.CASCADE, verbose_name="予約ID")
    rating = models.FloatField(default=0, validators=[validators.MinValueValidator(0),validators.MaxValueValidator(5.0)])
    body = models.CharField(_("Review Body"), max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return "{}: {}".format(self.booking, self.rating)