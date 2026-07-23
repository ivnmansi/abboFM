import {ref} from 'vue';
import { scrobbleService } from '@/services/scrobbles';
import type { Scrobble } from '@/models';

export function useScrobbles() {
    const scrobbles = ref<Scrobble[]>([]);

    const fetchScrobbles = async () => {
        try {
            const response = await scrobbleService.getAll();
            scrobbles.value = response.data;
        } catch (error) {
            console.error('Error fetching scrobbles:', error);
        }
    };

    const addScrobble = async (data: { song: string, artist: string, album: string }) => {
        try {
            await scrobbleService.create(data);
            await fetchScrobbles();
        }
        catch (error) {
            console.error('Error:', error)
        }
    }

    return {
        scrobbles,
        fetchScrobbles,
        addScrobble,
    };
}
