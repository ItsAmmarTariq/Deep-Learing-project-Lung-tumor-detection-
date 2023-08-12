from django.db import models

# Define the medicine mapping
MEDICINE_MAPPING = {
    'malignant': ['medicine1', 'medicine2', 'medicine3'],
    'benign': ['medicine4', 'medicine5', 'medicine6'],
    'normal': ['medicine7', 'medicine8', 'medicine9']
}
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    malignant_case = models.IntegerField(default=0)
    benign_case = models.IntegerField(default=0)
    normal_case = models.IntegerField(default=0)
    suggested_medicines = models.ManyToManyField(Medicine, blank=True)

    def __str__(self):
        return self.name

    def suggest_medicines(self):
        # Look up the predicted case based on the counts
        if self.malignant_case > self.benign_case and self.malignant_case > self.normal_case:
            predicted_case = 'malignant'
        elif self.benign_case > self.malignant_case and self.benign_case > self.normal_case:
            predicted_case = 'benign'
        else:
            predicted_case = 'normal'

        # Look up the suggested medicines from the mapping
        suggested_medicines = Medicine.objects.filter(name__in=MEDICINE_MAPPING.get(predicted_case, []))

        # Set the suggested medicines for this doctor
        self.suggested_medicines.set(suggested_medicines)
