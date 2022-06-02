from django.db import models

class Rental(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    rental_name = models.CharField(max_length=100)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    previous_reservation_id = models.IntegerField(blank=True, null=True)
 
    def __str__(self):
        return '%s %s %s' % (self.rental.name, str(self.check_in), str(self.check_out))

    def save(self, *args, **kwargs):
        rental = Rental.objects.get(id=self.rental.id)
        self.rental_name = rental.name
        super().save(*args, **kwargs)


