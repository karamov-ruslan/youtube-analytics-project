import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id # ID канала
        self.__title = self.channel['items'][0]['snippet']['title'] # Название канала
        self.__description = self.channel['items'][0]['snippet']['description'] # Описание канала
        self.__url = f'https://www.youtube.com/channel/{channel_id}' # Ссылка на канал
        self.__subscriber_count = self.channel['items'][0]['statistics']['subscriberCount'] # Количество подписчиков
        self.__video_count = self.channel['items'][0]['statistics']['videoCount'] # количество видео
        self.__view_count = self.channel['items'][0]['statistics']['viewCount'] # Общее количество просмотров

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def video_count(self):
        return self.__video_count

    @property
    def view_count(self):
        return self.__view_count

    @classmethod
    def get_service(cls):
        return cls.youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps( self.channel, indent=2, ensure_ascii=False))

    def to_json(self, f_name):
        dct = {
            'id': self.__channel_id,
            'title': self.__title,
            'description': self.__description,
            'url': self.__url,
            'subscriber count': self.__subscriber_count,
            'video count': self.__video_count,
            'view count': self.__view_count,
            }

        with open(f_name, 'w') as f:
            f.write(json.dumps(dct))
