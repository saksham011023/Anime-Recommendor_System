from utils.helpers import *
from config.paths_config import *

similar_users=find_similar_users(11880,USER_WEIGHTS_PATH,USER2USER_ENCODED,USER2USER_DECODED)
print(similar_users)
user_pref=get_user_preferences(11880,RATING_DF,DF)
print(user_pref)