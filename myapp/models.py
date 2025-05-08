from django.db import models

# class Person(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name


# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through = "Membership")

#     def __str__(self):
#         return self.name


# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateFiled()
#     invite_reason = models.CharField(max_length=64)

#     class Meta:
#         constained = [
#             models.UniqueConstraint(
#                 fileds = ["person", "group"], name = "unique_person_group"
#             )
#         ]
