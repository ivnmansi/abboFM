import api from './api';
import type { Scrobble, CreateScrobblePayload } from '@/models';

export const scrobbleService = {
    getAll() {
        return api.get<Scrobble[]>('scrobbles/')
    },
    create(data: CreateScrobblePayload){
        return api.post<Scrobble>('scrobbles/', {
            title: data.song,
            artist: data.artist,
            album: data.album,
        })
    },
    getByUser(userId: number) {
        return api.get<Scrobble[]>(`users/${userId}/scrobbles/`);
    }
}
