import os
import random
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_dp.settings")
django.setup()
from django.contrib.auth.models import User
from blood_donner.models import Donner

fake = Faker()

def create_random_user(created_by_id, team_id, site_id, num_users=100):
    for _ in range(num_users):
        username = fake.unique.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        blood_grup = random.choice(["A+", "A-","B+" "B-", "AB+", "AB-", "O+", "O-"])
        phone_number = fake.phone_number()

        #Create user
        user = User.objects.create_user(
            username=username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,

        )

        # assign profile data
        user.profile.team_id = team_id
        user.profile.site_id = site_id
        user.profile.role = 'Donner'
        user.save()

        # create donner
        Donner.objects.create(
            user = user,
            blood_grup = blood_grup,
            phone_number = phone_number,
            created_by_id = created_by_id

        )

if __name__ == "__main__":
    CREATED_BY_ID=40
    TEAM_ID=40
    SITE_ID=4

    NUM_USERS = 100
    create_random_user(CREATED_BY_ID,TEAM_ID,SITE_ID,NUM_USERS)
    print(f"s_c {NUM_USERS} d_u!")