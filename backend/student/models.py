from django.db import models


class Section_master(models.Model):
    sec_name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.sec_name


class StdClass_master(models.Model):
    class_name = models.CharField(max_length=15)
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


class Tehsil_master(models.Model):
    state = models.ForeignKey(State_master, on_delete=models.CASCADE)
    tehsil_name = models.CharField(max_length=50)
    description = models.TextField()


class Nationality_master(models.Model):
    nationality_name = models.CharField(max_length=50)
    description = models.TextField()


class motherTongue_master(models.Model):
    mothertongue_name = models.CharField(max_length=50)
    description = models.TextField()


class SchoolBoard_master(models.Model):
    board_name = models.CharField(max_length=50)
    description = models.TextField()


class StudentPersonalDetails(models.Model):
    std_id = models.CharField(max_length=10)
    std_first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
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
    nationality = models.ForeignKey(Nationality_master, on_delete=models.CASCADE)
    domicile = models.CharField(max_length=100)
    mother_tongue = models.ForeignKey(motherTongue_master, on_delete=models.CASCADE)
    ph_number_father = models.BigIntegerField()
    ph_number_mother = models.BigIntegerField()
    email = models.EmailField(null=True, blank=True)
    local_address = models.TextField()
    postal_address = models.TextField()
    postal_city = models.ForeignKey(City_master, on_delete=models.CASCADE)
    tehsil = models.ForeignKey(Tehsil_master, on_delete=models.CASCADE)
    postal_state = models.ForeignKey(State_master, on_delete=models.CASCADE)
    postal_zip_code = models.IntegerField()
    father_occupation = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=50)

    def __str__(self):
        return self.std_first_name


class PreviousSchoolDetails(models.Model):
    student = models.ForeignKey(StudentPersonalDetails, on_delete=models.CASCADE)
    school_board = models.ForeignKey(SchoolBoard_master, on_delete=models.CASCADE)
    Udise_num = models.IntegerField()
    school_name = models.CharField(max_length=255)
    school_address = models.TextField()
    school_city = models.ForeignKey(City_master, on_delete=models.CASCADE)
    tehsil = models.ForeignKey(Tehsil_master, on_delete=models.CASCADE)
    school_state = models.ForeignKey(State_master, on_delete=models.CASCADE)
    school_zip_code = models.CharField(max_length=20)
    school_phone_number = models.CharField(max_length=20, null=True, blank=True)
    grade_attended = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason_for_leaving = models.TextField(null=True, blank=True)
    transfer_certificate = models.FileField(upload_to='pdfs', null=True, blank=True)

    def __str__(self):
        return f"{self.school_name})"
