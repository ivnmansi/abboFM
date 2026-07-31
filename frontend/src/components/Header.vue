<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Button from 'primevue/button'
import Tag from 'primevue/tag'
import { useUsers } from '@/composables/useUsers'

const { currentUser, fetchCurrentUser } = useUsers()
const router = useRouter()

const logout = () => {
  localStorage.removeItem('token')
  router.push('/login')
}

onMounted(fetchCurrentUser)
</script>

<template>
  <header class="flex flex-col gap-4 border-b border-surface-800 pb-5 sm:flex-row sm:items-center sm:justify-between">

    <div class="flex items-center gap-3">
      <h1 class="text-3xl font-bold tracking-tight logo">abbo.FM</h1>
      <Tag :value="`${currentUser?.total_scrobbles ?? 0} scrobbles`" severity="secondary" />
    </div>

    <div class="flex items-center justify-between gap-3 sm:justify-end">
      <span class="text-sm text-surface-400">
        Welcome, <strong class="font-semibold text-surface-0">{{ currentUser?.username ?? 'there' }}</strong>
      </span>
      <Button label="Log out" severity="danger" outlined size="small" @click="logout" />
    </div>
  </header>
</template>

<style scoped>
.logo {
    color: transparent;
    background: linear-gradient(to right, var(--p-purple-400), var(--p-blue-300));
    -webkit-background-clip: text;
    background-clip: text;
}
</style>
