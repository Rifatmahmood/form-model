from django import forms


class GroomForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Please enter your name",
       
        error_messages={
            "required": "Name is required.",
            "max_length": "Name cannot exceed 100 characters.",
        },
    )
    father = forms.CharField(
        max_length=100,
        label="Father Name",
        error_messages={
            "required": "Father name is required.",
            "max_length": "Father name cannot exceed 100 characters.",
        },
    )
    email = forms.EmailField(
        error_messages={
            "required": "Email is required.",
            "invalid": "Enter a valid email address.",
        }
    )
    interests = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        label="Write About your Hobbies, interests, etc",
        help_text = "You can write about what You love to do when you are free, What you love to eat, How you spend your time etc",
        error_messages={
            "required": "Please write about your hobbies and interests.",
        },
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Birth Date",
        error_messages={
            "required": "Birth date is required.",
            "invalid": "Enter a valid date.",
        },
    )
    gender = forms.ChoiceField(
        choices=[("M", "Male"), ("F", "Female")],
        label="Gender",
        error_messages={
            "required": "Please select your gender.",
            "invalid_choice": "Select a valid choice.",
        },
    )
    age = forms.IntegerField(
        label="Age",
        error_messages={
            "required": "Age is required.",
            "invalid": "Enter a valid age.",
        },
    )
    height = forms.FloatField(
        label="Height in meters",
        error_messages={
            "required": "Height is required.",
            "invalid": "Enter a valid height.",
        },
    )
    website = forms.URLField(
        label="Personal Website",
        required=False,
        error_messages={
            "invalid": "Enter a valid URL.",
        },
    )
    monthly_income = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Monthly Income",
        error_messages={
            "required": "Monthly income is required.",
            "invalid": "Enter a valid amount.",
        },
    )
    bio_data = forms.FileField(
        label="Upload bio data",
        required=False,
        error_messages={
            "invalid": "Upload a valid file.",
        },
    )
    profile_picture = forms.ImageField(
        label="Upload Profile Picture",
        required=False,
        error_messages={
            "invalid": "Upload a valid image file.",
        },
    )
    consent = forms.BooleanField(
        required=False,
        label="I am telling the truth",
        error_messages={
            "invalid": "Please confirm the truthfulness of your information.",
        },
    )
