import asyncio
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager

import requests

import dotenv
import os

dotenv.load_dotenv()
API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}

"""
    Get current user from the API
"""
async def get_current_user():
    try:
        res = requests.get(f"{API_URL}users/", headers=HEADERS)

        if res.status_code == 200:
            return res.json()
        else:
            if DEBUG:
                print(f"Error getting current user: {res.status_code} - {res.text}")
            return None
    except Exception as e:
        if DEBUG:
            print(f"Error getting current user: {e}")
        return None


"""
    Gets the current media playing on windows
"""
async def get_current_media():
    # get session manager
    manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()

    # get current session
    session = manager.get_current_session()

    if session is None:
        return None, None
    
    # get media properties
    media_properties = await session.try_get_media_properties_async()
    timeline = session.get_timeline_properties()

    return media_properties, timeline

async def main():

    # get current user from the API
    current_user = await get_current_user()
    if current_user is None:
        print("Error getting current user")
        return
    
    print(f"Logged in as: {current_user[0]['username']} (ID: {current_user[0]['id']})")

    # get the last media played
    last_title = None
    try:
        res = requests.get(f"{API_URL}scrobbles/last/", headers=HEADERS)
        if res.status_code == 200:
            last_scrobble = res.json()
            last_title = last_scrobble['song_title']
            if DEBUG:
                print(f"Last scrobble: {last_title} by {last_scrobble['artist_name']}")
    except Exception as e:
        if DEBUG:
            print(f"Error getting last scrobble: {e}")

    # loop to check for current media every 5 seconds
    while True:
        current_media, timeline = await get_current_media()

        # if there is no media playing, wait for 5 seconds and continue
        if current_media is None:
            await asyncio.sleep(5)
            continue

        # if the media is the same as the last one, wait for 5 seconds and continue
        if last_title is not None and current_media.title == last_title:
            await asyncio.sleep(5)
            continue
        
        # remaining case the media is different, send a request to the API
        print(f"Scrobbling: {current_media.title} by {current_media.artist}")

        data = {
            "song_title": current_media.title,
            "artist_name": current_media.artist,
            "album_title": current_media.album_title,
            "duration": timeline.end_time.total_seconds() if timeline else 0,
        }

        try:
            res = requests.post(f"{API_URL}scrobbles/", json=data, headers=HEADERS)

            if res.status_code == 201:
                last_title = current_media.title
            else:
                if DEBUG:
                    print(f"Error sending request to API: {res.status_code} - {res.text}")
        
        except Exception as e:
            if DEBUG:
                print(f"Error sending request to API: {e}")

        await asyncio.sleep(5)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
