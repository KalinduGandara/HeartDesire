from .models import PersonalityTest
from .personality import *

def getData(body):
    return body['q1']+body['q2']+body['q3']+body['q4']+body['q5']+body['q6']+body['q7']+body['q8']+body['q9']+body['q10']


def submiteData(data):
    personalityData = getPersonality(data)
    p = PersonalityTest(E_ans=data[0], S_ans=data[1], T_ans=data[2], J_ans=data[3],
                        E_value=personalityData[0], S_value=personalityData[1], 
                        T_value=personalityData[2], J_value=personalityData[3],
                        Personality_type=personalityData[4])
    p.save()
    print(data)
    return p.pk

