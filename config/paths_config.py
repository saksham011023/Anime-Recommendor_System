import os

##############DATA INGESTION#############

RAW_DIR="artifacts/raw"
CONFIG_PATH="config/config.yaml"

################# DATA PROCESSING #############
PROCESSED_DIR="artifacts/processed"
ANIMELIST_CSV="artifacts/raw/animelist.csv"
ANIME_CSV="artifacts/raw/anime.csv"
ANIMESYNOPSIS_CSV="artifacts/raw/anime_with_synopsis.csv"

X_TRAIN_ARRAY=os.path.join(PROCESSED_DIR,"X_train_array.pkl")
X_TEST_ARRAY=os.path.join(PROCESSED_DIR,"X_test_array.pkl")
y_TRAIN=os.path.join(PROCESSED_DIR,"y_train.pkl")
y_TEST=os.path.join(PROCESSED_DIR,"y_test.pkl")

RATING_DF=os.path.join(PROCESSED_DIR,"rating.csv")
DF=os.path.join(PROCESSED_DIR,"anime_df.csv")
SYNOPSIS_DF=os.path.join(PROCESSED_DIR,"synopsis_df.csv")

USER2USER_ENCODED="artifacts/processed/user2user_encoded.pkl"
USER2USER_DECODED="artifacts/processed/user2user_decoded.pkl"

ANIME2ANIME_ENCODED="artifacts/processed/anime2anime_encoded.pkl"
ANIME2ANIME_ENCODED="artifacts/processed/anime2anime_encoded.pkl"

