export interface User {
  id: number;
  username: string;
}

export interface Artist {
    id: number;
    name: string;
}

export interface Album {
  id: number;
  title: string;
  artist: number;
}

export interface Song {
  id: number;
  title: string;
  album: number;
}

export interface Scrobble {
  id: number;
  song_title: string;
  artist_name: string;
  album_title: string;
  timestamp: string;
  user: number;
  song: number;
}