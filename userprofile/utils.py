from .models import UserBio,PatnertBio,MatchingCouples
from django.db.models import Q
from django.contrib.auth.models import User


ageDiff = 2
heightDiff = 10
weightDiff = 5
salaryDiff = 5000

def calPreference(patnerBio:UserBio,prefernceBio:PatnertBio):
    match = 0
    if(abs(int(patnerBio.age)-int(prefernceBio.age))<ageDiff):
        match += 1
    if(abs(int(patnerBio.height)-int(prefernceBio.height))<heightDiff):
        match += 1
    if(abs(int(patnerBio.weight)-int(prefernceBio.weight))<weightDiff):
        match += 1
    if(abs(int(patnerBio.salary)-int(prefernceBio.salary))<salaryDiff):
        match += 1
    if(patnerBio.education == prefernceBio.education):
        match += 1
    if(patnerBio.nationality == prefernceBio.nationality):
        match += 1
    if(patnerBio.religion == prefernceBio.religion):
        match += 1
    if(patnerBio.skin_complexity == prefernceBio.skin_complexity):
        match += 1
    if(patnerBio.eye_color == prefernceBio.eye_color):
        match += 1
    if(patnerBio.occupation == prefernceBio.occupation):
        match += 1
    
    return match



def matchPreference(user,prefernceBio:PatnertBio):
    allBios = UserBio.objects.filter(~Q(user = user.id))
    for bio in allBios:
        match = calPreference(bio,prefernceBio)
        patner = User.objects.get(pk = bio.user.id)
        matchObj = MatchingCouples.objects.get_or_create(user = user,patner = patner,prefereceMatching = 5)
        print(matchObj)
    

