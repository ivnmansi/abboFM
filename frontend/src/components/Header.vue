<template>
    <header class="border-bottom pb-3">
        <nav class="navbar navbar-expand-md p-0" aria-label="Main navigation">
            <div class="container-fluid p-0 gap-3">
                <div class="d-flex align-items-center gap-3">
                    <span class="navbar-brand mb-0 h1 fw-bold">abboFM</span>
                    <span class="badge text-bg-primary">{{ currentUser?.total_scrobbles ?? 0 }} scrobbles</span>
                </div>

                <div class="d-flex align-items-center gap-3 ms-md-auto">
                    <span class="navbar-text text-body-secondary">Welcome, <strong class="text-body">{{ currentUser?.username ?? 'there' }}</strong></span>
                    <button type="button" class="btn btn-outline-danger" @click="logout">Log out</button>
                </div>
            </div>
        </nav>
    </header>
</template>
<script setup lang="ts">
    import { onMounted } from 'vue'
    import { useUsers } from '@/composables/useUsers'
    const {currentUser, fetchCurrentUser } = useUsers()
    import { useRouter } from 'vue-router'

    const router = useRouter()

    const logout = () => {
        localStorage.removeItem('token')
        router.push('/login')
    }

    onMounted(() => {
        fetchCurrentUser()
    })
</script>
