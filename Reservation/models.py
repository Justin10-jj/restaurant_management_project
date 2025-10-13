class Resrvation(models.Model):
    customer_name=models.CharField(max_length=100)
    table_number=models.PositiveIntegerFiled()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    