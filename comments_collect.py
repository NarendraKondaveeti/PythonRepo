import requests
from textblob import TextBlob

API_KEY = "AIzaSyBBk-qsBoJ_LcHqeemf1XWHWVtnnahvcQA"  # 🔹 Replace with your API Key
VIDEO_ID = "hp5yimKgnMQ"  # 🔹 Replace with correct Video ID

url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={VIDEO_ID}&key={API_KEY}&maxResults=5000"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("youtube_comments_rating.txt", "w", encoding="utf-8") as file:
        for item in data.get("items", []):
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            sentiment_score = TextBlob(comment_text).sentiment.polarity

            # 🔹 Positive = True, Negative = False
            rating = "True" if sentiment_score > 0 else "False"

            file.write(f"{comment_text}\nRating: {rating}\n\n")

    print("✅ **Comments & Ratings saved to youtube_comments_rating.txt successfully!**")

else:
    print(f"🚨 API Request Failed! Status Code: {response.status_code}")
    print(response.text)  # Debugging purpose
