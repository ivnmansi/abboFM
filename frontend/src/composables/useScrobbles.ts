import {ref} from 'vue';
import { scrobbleService } from '@/services/scrobbles';
import type { Scrobble, CreateScrobblePayload } from '@/models';

export function useScrobbles() {
    const scrobbles = ref<Scrobble[]>([]);
    const isLoading = ref(false);

    const fetchScrobbles = async () => {
        isLoading.value = true;
        try {
            const response = await scrobbleService.getAll();
            scrobbles.value = response.data;
        }
        catch (error) {
            console.error('Error fetching scrobbles:', error);
        }
        finally {
            isLoading.value = false;
        }
    };

    const addScrobble = async (data: CreateScrobblePayload) => {
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
        isLoading
    };
}
