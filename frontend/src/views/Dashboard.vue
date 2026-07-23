<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { useRouter } from 'vue-router'

    import { useScrobbles } from '@/composables/useScrobbles'
    import { useSongs } from '@/composables/useSongs'

    import Header from '@/components/Header.vue'

    const { scrobbles, fetchScrobbles, addScrobble } = useScrobbles()
    const router = useRouter()



    
    const newScrobble = ref({
        song: '',
        artist: '',
        album: ''
    })

    const registerScrobble = async () => {
        if (!newScrobble.value.song || !newScrobble.value.artist || !newScrobble.value.album) {
            alert('Please fill in all fields.')
            return
        }

        await addScrobble(newScrobble.value)

        newScrobble.value = {
            song: '',
            artist: '',
            album: ''
        }
    }

    onMounted(() => {
        fetchScrobbles()
    })
</script>

<template>
    <main class="min-vh-100 py-4 py-md-5">
        <div class="container">
            <Header />

            <div class="row justify-content-center mt-4">
                <div class="col-12 col-xl-10">
                    <section class="card border-1 shadow-sm mb-4" aria-labelledby="new-scrobble-title">
                        <div class="card-body p-4">
                            <div class="d-flex flex-column flex-sm-row justify-content-between align-items-sm-center gap-2 mb-4">
                                <div>
                                    <h1 id="new-scrobble-title" class="h4 fw-bold mb-1">Add a scrobble</h1>
                                    <p class="text-body-secondary mb-0">Add a song to your listening history.</p>
                                </div>
                                <span class="badge text-bg-primary align-self-start">New scrobble</span>
                            </div>

                            <form @submit.prevent="registerScrobble">
                                <div class="row g-3 align-items-end">
                                    <div class="col-12 col-md-4">
                                        <label for="song" class="form-label fw-semibold">Song</label>
                                        <input id="song" v-model="newScrobble.song" class="form-control" type="text" placeholder="Song title" required>
                                    </div>
                                    <div class="col-12 col-md-4">
                                        <label for="artist" class="form-label fw-semibold">Artist</label>
                                        <input id="artist" v-model="newScrobble.artist" class="form-control" type="text" placeholder="Artist name" required>
                                    </div>
                                    <div class="col-12 col-md-4">
                                        <label for="album" class="form-label fw-semibold">Album</label>
                                        <input id="album" v-model="newScrobble.album" class="form-control" type="text" placeholder="Album title" required>
                                    </div>
                                    <div class="col-12 d-grid d-sm-flex justify-content-sm-end">
                                        <button type="submit" class="btn btn-primary px-4">Scrobble</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </section>

                    <section class="card border-1 shadow-sm" aria-labelledby="history-title">
                        <div class="card-header border-bottom-0 pt-4 px-4">
                            <h2 id="history-title" class="h4 fw-bold mb-1">Listening history</h2>
                            <p class="text-body-secondary mb-0">Your recently registered songs.</p>
                        </div>
                        <div class="card-body p-0 p-md-4">
                            <div class="table-responsive">
                                <table class="table table-hover align-middle mb-0">
                                    <thead>
                                        <tr>
                                            <th scope="col" class="ps-4">Song</th>
                                            <th scope="col">Artist</th>
                                            <th scope="col">Album</th>
                                            <th scope="col" class="pe-4">Timestamp</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="scrobble in scrobbles" :key="scrobble.id">
                                            <td class="ps-4 fw-semibold">{{ scrobble.song_title }}</td>
                                            <td>{{ scrobble.artist_name }}</td>
                                            <td>{{ scrobble.album_title }}</td>
                                            <td class="pe-4 text-body-secondary text-nowrap">{{ scrobble.timestamp }}</td>
                                        </tr>
                                        <tr v-if="!scrobbles.length">
                                            <td colspan="4" class="py-5 text-center text-body-secondary">No scrobbles registered yet.</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </main>
</template>
