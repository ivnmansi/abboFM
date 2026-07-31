<script lang="ts" setup>
import Card from 'primevue/card'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

import type { Scrobble } from '@/models'
const props = defineProps<{
  scrobbles: Scrobble[]
  isLoading: boolean
}>()
</script>
<template>
    <Card>
        <template #title>Listening history</template>
        <template #subtitle>
            <p class="text-purple-300 text-sm">Recently registered songs.</p>
        </template>
        <template #content>
        <DataTable :value="scrobbles" :loading="isLoading" striped-rows table-style="min-width: 42rem">
            <Column field="song_title" header="Song" />
            <Column field="artist_name" header="Artist" />
            <Column field="album_title" header="Album" />
            <Column field="timestamp" header="Timestamp" />
            <template #empty>No scrobbles registered yet.</template>
            <template #loading>
                <div class="flex flex-col items-center justify-center gap-2 py-6">
                    <i class="pi pi-spin pi-spinner text-3xl text-purple-400"></i>
                    <span class="text-sm text-surface-400">Loading...</span>
                </div>
            </template>
        </DataTable>
        </template>
    </Card>

</template>
<style scoped>
</style>