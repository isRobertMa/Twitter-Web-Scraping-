import tweepy

# Twitter API v2 Client credentials 
# VERY DANGEROUS, TESTING PURPOSE ONLY
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPoSngEAAAAAZ6XTXf%2FVHu1%2Bu%2BLDSLaaVYxZ5fI%3DPsfoAw87FDsy6dCZQOEYUTwU2zzywn25iN6Sfup4maM6YXdDVq'
CONSUMER_KEY = 'oyPT9CGy8oFbussqiYHdyii5t'
CONSUMER_SECRET = 'gUchqKOJuFlW7c8FsDsWj9ex17Tjzwde8YZjidyXtK4bDIGojl'
ACCESS_TOKEN = '1070671512871436288-xkpNtjJobDtrBBj42vBK3RNMtrAKcR'
ACCESS_TOKEN_SECRET = 'FXfiGqYLPuQ8p4gO5JoPe83o76pASyOMfVwaN5KQlAvBm'

# Twitter API v2 Client, return from request to the API
api = tweepy.Client(bearer_token= BEARER_TOKEN, consumer_key= CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, 
                    access_token= ACCESS_TOKEN, access_token_secret= ACCESS_TOKEN_SECRET)

# lookup myself
def lookup_me() -> None:
    """
    Lookup myself.
    """
    try: 
        # user is a response field 
        user = api.get_me()
        # Print user details
        print("User Details: ")
        print("userID: ", user.id)
        print("Name: ", user.name)
        print("Username: ", user.username)
        print("Created at: ", user.created_at)
        print("Is this user's tweet protected: ", user.protected)
    except tweepy.TweepyException as e:
        print("Error", e)


# Lookup specific user by their username, also known as the handle name
def lookup_user_by_username(username: str) -> None:
    """
    This function look up users by user name, print out their userID, userName, pinned Tweet ID, and creation date of the account.
    """
    try:
        # user is a response field 
        user = api.get_user(username=username)
        # Print user details
        print("User Details: ")
        print("userID: ", user.id)
        print("Name: ", user.name)
        print("Username: ", user.username)
        print("Created at: ", user.created_at)
        print("Is this user's tweet protected: ", user.protected)
    except tweepy.TweepyException as e:
        print("Error:", e)

# Call the function with a Twitter username
lookup_user_by_username("realDonaldTrump")

