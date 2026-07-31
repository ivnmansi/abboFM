<script setup lang="ts">
import { onMounted, ref } from 'vue'
import type { CreateScrobblePayload } from '@/models'
import { useScrobbles } from '@/composables/useScrobbles'
import Header from '@/components/Header.vue'
import Card from 'primevue/card'
import Column from 'primevue/column'
import DataTable from 'primevue/datatable'

import AddScrobbleCard from '@/components/AddScrobbleCard.vue'

const { scrobbles, fetchScrobbles, addScrobble } = useScrobbles()

const formError = ref('')
const newScrobble = ref<CreateScrobblePayload>({
  song: '',
  artist: '',
  album: '',
})

const registerScrobble = async () => {
  if (!newScrobble.value.song || !newScrobble.value.artist || !newScrobble.value.album) {
    formError.value = 'Please fill in all fields.'
    return
  }

  formError.value = ''
  await addScrobble(newScrobble.value)
  newScrobble.value = { song: '', artist: '', album: '' }
}

onMounted(fetchScrobbles)
</script>

<template>
  <main class="min-h-screen bg-surface-950 px-4 py-6 text-surface-0 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-6xl">
      <Header />

      <div class="mt-8 grid gap-6">
        <AddScrobbleCard/>

        <Card>
          <template #title>Listening history</template>
          <template #subtitle>Your recently registered songs.</template>
          <template #content>
            <DataTable :value="scrobbles" striped-rows table-style="min-width: 42rem">
              <Column field="song_title" header="Song" />
              <Column field="artist_name" header="Artist" />
              <Column field="album_title" header="Album" />
              <Column field="timestamp" header="Timestamp" />
              <template #empty>No scrobbles registered yet.</template>
            </DataTable>
          </template>
        </Card>
      </div>
    </div>
  </main>
</template>
