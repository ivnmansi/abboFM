/**
 * @abstract Represents a user given by the backend API
 */
export interface User {
  id: number;
  username: string;
  date_joined: string;
  total_scrobbles: number;
}

export interface CreateUserPayload {
  username: string;
  password: string;
}

/**
 * @abstract Represents an artist given by the backend API
 */
export interface Artist {
    id: number;
    name: string;
    biography: string;
    image: string;
    album_count: number;
    song_count: number;
    total_scrobbles: number;
}

/**
 * @abstract Represents an album given by the backend API
 */
export interface Album {
  id: number;
  title: string;
  artist: number | null;
  artist_name: string | null;
  release_date: string | null;
  song_count: number;
  total_scrobbles: number;
}

/**
 * @abstract Represents a song given by the backend API
 */
export interface Song {
  id: number;
  title: string;
  album: number | null;
  artist: number | null;
  album_title: string | null;
  artist_name: string | null;
  duration: number | null;
  total_scrobbles: number;
}

/**
 * @abstract Represents a scrobble given by the backend API
 */
export interface Scrobble {
  id: number;
  song_title: string;
  artist_name: string;
  album_title: string;
  timestamp: string;
  user: number;
  song: number;
}

/**
 * @abstract Payload for creating a new scrobble.
 */
export interface CreateScrobblePayload {
  song: string;
  artist: string;
  album: string;
}