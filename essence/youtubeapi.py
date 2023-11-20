import googleapiclient.discovery
import googleapiclient.errors
from urllib.parse import urlparse, parse_qs
from isodate import parse_duration

# Parse youtube ID from URL
def video_id(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None

api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyBRH6EWN4RPnZGkPHv8pIL4jMTC9KNbdJ8"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

def video_info(video_id):
    response = youtube.videos().list(part='snippet,contentDetails', id=video_id).execute()
    items = response['items'][0]
    info = dict()
    info["title"] = items['snippet']['title']
    info["channel"] = items['snippet']['channelTitle']
    info["length"] = int(parse_duration(items['contentDetails']['duration']).total_seconds())
    return info