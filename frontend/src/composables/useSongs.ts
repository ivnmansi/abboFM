import { ref } from 'vue'
import { songsService } from '@/services/songs'
import type { Song } from '@/models'

export function useSongs(){
    const songs = ref<Song[]>([])

    const getSongName = (songId: number) => {
        const song = songs.value.find(s => s.id === songId)
        return song ? song.title : 'Unknown Song'
    }

    const fetchSongs = async () => {
        try {
            const response = await songsService.getAll()
            songs.value = response.data
        } catch (error) {
            console.error('Error fetching songs:', error)
        }
    }

    return {
        songs,
        fetchSongs,
        getSongName
    };
}