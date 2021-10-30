from functions.FirebaseDB import db
def getPlayHistorypushups(user_id):
        a=[]
        users=db.child("users").child(user_id).child("history").get()
        for user in users.each():
            date_of_play=user.key()
            pushups=db.child("users").child(user_id).child("history").child(date_of_play).child("pushups").get().val()
            data=[date_of_play,pushups]
            a.append(data)
        return a

def getPlayHistorysquats(user_id):
        a=[]
        users=db.child("users").child(user_id).child("history").get()
        for user in users.each():
            date_of_play=user.key()
            squats=db.child("users").child(user_id).child("history").child(date_of_play).child("squats").get().val()
            data=[date_of_play,squats]
            a.append(data)
        return a

def getPlayHistoryCaloryBurnt(user_id):
        a=[]
        users=db.child("users").child(user_id).child("history").get()
        for user in users.each():
            date_of_play=user.key()
            pushups=db.child("users").child(user_id).child("history").child(date_of_play).child("pushups").get().val()
            squats=db.child("users").child(user_id).child("history").child(date_of_play).child("squats").get().val()
            calories_burnt_data=CaloriesBurnt(pushups,squats)
            data=[date_of_play,calories_burnt_data]
            a.append(data)
        return a

def CaloriesBurnt(pushups,squats):
    pushups=int(pushups)
    squats=int(squats)
    burntcalorie=(0.75*pushups) + (0.55 * squats)
    burntcalorie=round(burntcalorie)
    return burntcalorie