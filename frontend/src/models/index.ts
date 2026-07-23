export interface User {
  id: number;
  username: string;
  joined_date: string;
  total_scrobbles: number;
}

export interface Artist {
    id: number;
    name: string;
    biography: string;
    image: string;
    album_count: number;
    song_count: number;
    total_scrobbles: number;
}

export interface Album {
  id: number;
  title: string;
  artist_name: string;
  release_date: string;
  total_scrobbles: number;
}

export interface Song {
  id: number;
  title: string;
  album: number;
  artist_name: string;
  total_scrobbles: number;
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