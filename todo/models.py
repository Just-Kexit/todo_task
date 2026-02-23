from django.db import models


class Task(models.Model):

    content = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tags", blank=True)

    class Meta:
        ordering = ["is_completed", "-create_at"]

    def __str__(self):
        return (
            f"'{self.name}' - deadline: "
            f"{self.deadline.strftime("%d.%m.%Y %H:%M")}, "
            f"is completed: {self.is_completed}"
        )


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
