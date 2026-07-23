import api from './api'
import type { Song } from '@/models'

export const songsService = {
  getAll() {
    return api.get<Song[]>('songs/')
  }
}