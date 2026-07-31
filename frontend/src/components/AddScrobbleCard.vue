<script setup lang="ts">
    import { ref } from 'vue'
    import type { CreateScrobblePayload } from '@/models'
    import { useScrobbles } from '@/composables/useScrobbles'

    import Card from 'primevue/card'
    import InputText from 'primevue/inputtext'
    import Button from 'primevue/button'
    import Message from 'primevue/message'

    const { addScrobble } = useScrobbles()

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

</script>

<template>
    <Card>
        <template #title>
            <div class="flex flex-col gap-1 sm:flex-row sm:items-center sm:justify-between">
                <div>
                    <h1 id="new-scrobble-title" class="text-xl font-semibold">Add a scrobble</h1>
                    <p class="mt-1 text-sm font-normal text-purple-300">
                        Add a song to your listening history.
                    </p>
                </div>
            </div>
        </template>

        <template #content>
            <form class="grid gap-4 md:grid-cols-3" aria-labelledby="new-scrobble-title" @submit.prevent="registerScrobble">
                <div class="flex flex-col gap-2">
                    <label for="song" class="font-medium">Song</label>
                    <InputText id="song" v-model="newScrobble.song" placeholder="Song title" required fluid />
                </div>
                <div class="flex flex-col gap-2">
                    <label for="artist" class="font-medium">Artist</label>
                    <InputText id="artist" v-model="newScrobble.artist" placeholder="Artist name" required fluid />
                </div>
                <div class="flex flex-col gap-2">
                    <label for="album" class="font-medium">Album</label>
                    <InputText id="album" v-model="newScrobble.album" placeholder="Album title" required fluid />
                </div>

                <Message v-if="formError" severity="warn" class="md:col-span-3">
                    {{ formError }}
                </Message>
                <div class="flex justify-end md:col-span-3">
                    <Button type="submit" severity="help">
                        <font-awesome-icon icon="fa-solid fa-plus" /> Scrobble
                    </Button>
                </div>
            </form>
        </template>
    </Card>
</template>
