import api from './api';
import type { Scrobble } from '@/models';

interface queryParams {
    song: string,
    artist: string,
    album: string
}

export const scrobbleService = {
    getAll() {
        return api.get<Scrobble[]>('scrobbles/')
    },
    create(queryParams: queryParams){
        return api.post<Scrobble>('scrobbles/', queryParams)
    }
}