from functions.FirebaseDB import db
import datetime
def get_date():
    now = datetime.datetime.now().ctime().split()
    present_date=now[1]+" "+now[2]
    return present_date

def user_info_storage(name,age,height,weight,email):
    user_id=get_user_id(email)
    present_date=get_date()
    data={
        "name":name,
        "age":age,
        "height":height,
        "weight":weight,
        "email":email,
    }
    data2={
        "pushups":0,
        "squats":0
    }
    db.child("users").child(user_id).child("profile").set(data)
    db.child("users").child(user_id).child("history").child(present_date).set(data2)


def get_user_id(email):
 a=email.split('.')
 user_id=a[0]
 return user_id
