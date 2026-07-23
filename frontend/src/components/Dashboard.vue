<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import api from '@/services/api'
    import { useRouter } from 'vue-router'

    import type { Scrobble } from '@/models'
    import type { Song } from '@/models'

    import { useScrobbles } from '@/composables/useScrobbles'
    import { useSongs } from '@/composables/useSongs'

    const { scrobbles, fetchScrobbles, addScrobble } = useScrobbles()
    const { songs, getSongName, fetchSongs } = useSongs()

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

    const logout = () => {
        localStorage.removeItem('token')
        router.push('/login')
    }

    onMounted(() => {
        fetchScrobbles()
    })
</script>

<template>
  <div>
    <header style="display: flex; justify-content: space-between; align-items: center;">
      <h2>Mis Scrobbles</h2>
      <button @click="logout">Cerrar Sesión</button>
    </header>
    
    <form @submit.prevent="registerScrobble" style="display: flex; gap: 10px; margin-bottom: 20px;">
      <input v-model="newScrobble.song" type="text" placeholder="Canción" required />
      <input v-model="newScrobble.artist" type="text" placeholder="Artista" required />
      <input v-model="newScrobble.album" type="text" placeholder="Álbum" required />
      <button type="submit">Scrobblear</button>
    </form>

    <table>
        <thead>
            <tr>
                <th>Canción</th>
                <th>Artista</th>
                <th>Álbum</th>
                <th>Fecha y Hora</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="scrobble in scrobbles" :key="scrobble.id">
                <td>{{ scrobble.song_title }}</td>
                <td>{{ scrobble.artist_name }}</td>
                <td>{{ scrobble.album_title }}</td>
                <td>{{ scrobble.timestamp }}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>