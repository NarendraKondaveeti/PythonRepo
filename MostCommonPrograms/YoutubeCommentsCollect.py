from googleapiclient.discovery import build

api_key = "YOUR_API_KEY"

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="VIDEO_ID",
    maxResults=100
)

response = request.execute()

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    print(comment)