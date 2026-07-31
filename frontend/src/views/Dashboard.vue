<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useScrobbles } from '@/composables/useScrobbles'
import Header from '@/components/Header.vue'
import Navbar from '@/components/Navbar.vue'

import AddScrobbleCard from '@/components/AddScrobbleCard.vue'
import ListeningHistoryTable from '@/components/ListeningHistoryTable.vue'

const { scrobbles, fetchScrobbles, isLoading } = useScrobbles()

onMounted(fetchScrobbles)
</script>

<template>
  <main class="min-h-screen bg-surface-950 px-4 py-6 text-surface-0 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-6xl">
      <Header />
      <Navbar />
      <div class="mt-8 grid gap-6">
        <AddScrobbleCard/>

        <ListeningHistoryTable :scrobbles="scrobbles" :isLoading="isLoading" />
      </div>
    </div>
  </main>
</template>
