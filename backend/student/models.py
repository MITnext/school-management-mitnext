from django.db import models


class Section_master(models.Model):
    sec_name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.sec_name


class StdClass_master(models.Model):
    class_name = models.CharField(max_length=15)
    section = models.ForeignKey(Section_master, on_delete=models.CASCADE, related_name='std_section')
    teacher = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.class_name} - {self.section}"


class Religion_master(models.Model):
    religion_name = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.religion_name


class MainCaste_master(models.Model):
    maincaste_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.maincaste_name


class SubCaste_master(models.Model):
    castesub_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.castesub_name


class State_master(models.Model):
    state_name = models.CharField(max_length=100)
    state_shortcut = models.CharField(max_length=3)

    def __str__(self):
        return self.state_name


class City_master(models.Model):
    state = models.ForeignKey(State_master, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    city_shortcut = models.CharField(max_length=4)

    def __str__(self):
        return self.city_name


class StudentPersonalDetails(models.Model):
    std_id = models.CharField(max_length=10)
    std_first_name = models.CharField(max_length=100)
    std_middle_name = models.CharField(max_length=100)
    std_last_name = models.CharField(max_length=100)
    photo = models.FileField(upload_to='student_photos', null=True, blank=True)
    gender_choices_type = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices_type)
    option_choices_type = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    ]
    blood_group = models.CharField('Option Type', max_length=10, choices=option_choices_type)
    admission_date = models.DateField()
    std_class = models.ForeignKey(StdClass_master, on_delete=models.CASCADE, related_name='std_class')
    std_section = models.ForeignKey(Section_master, on_delete=models.CASCADE, related_name='section')
    std_rollno = models.IntegerField()
    dateofbirth = models.DateField()
    birth_place = models.TextField()
    aadharnumber = models.BigIntegerField()
    aadharcard = models.FileField(upload_to='Student_aadharcards', null=True, blank=True)
    caste_main = models.ForeignKey(MainCaste_master, on_delete=models.CASCADE, related_name='caste_main')
    caste_sub = models.ForeignKey(SubCaste_master, on_delete=models.CASCADE, related_name='caste_sub')
    religion = models.ForeignKey(Religion_master, on_delete=models.CASCADE, related_name='religion')
    ph_number_father = models.BigIntegerField()
    ph_number_mother = models.BigIntegerField()
    email = models.EmailField(null=True, blank=True)
    local_address = models.TextField()
    postal_address = models.TextField()
    postal_city = models.CharField(max_length=100)
    postal_state = models.CharField(max_length=50)
    postal_zip_code = models.IntegerField()
    father_occupation = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=50)

    def __str__(self):
        return self.std_first_name


class PreviousSchoolDetails(models.Model):
    student = models.ForeignKey(StudentPersonalDetails, on_delete=models.CASCADE, related_name='previous_schools')
    school_name = models.CharField(max_length=255)
    school_board = models.CharField(max_length=255)
    school_address = models.TextField()
    school_city = models.CharField(max_length=100)
    school_state = models.CharField(max_length=100)
    school_zip_code = models.CharField(max_length=20)
    school_phone_number = models.CharField(max_length=20, null=True, blank=True)
    grade_attended = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason_for_leaving = models.TextField(null=True, blank=True)
    transfer_certificate = models.FileField(upload_to='pdfs', null=True, blank=True)

    def __str__(self):
        return f"{self.school_name})"
