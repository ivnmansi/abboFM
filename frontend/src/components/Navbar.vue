<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import MegaMenu from 'primevue/megamenu'

const router = useRouter()


const navigation = [
    { label: 'Dashboard', icon: 'fas fa-home', link: '/'
    },
    {
        label: 'Profile', icon: 'fas fa-user', link: '/profile'
    },
    {
        label: 'Settings', icon: 'fas fa-cog', link: '/settings'
    },
    {
        label: 'API Key', icon: 'fas fa-key', link: '/api-key'
    }
]
</script>

<template>
    <MegaMenu :model="navigation" orientation="horizontal" class="w-full">
        <template #item="{ item, label }">
            <router-link :to="item.link" class="flex items-center gap-2 px-4 py-2 text-sm font-medium text-surface-0 hover:bg-surface-800 rounded-md">
                <font-awesome-icon :icon="item.icon" class="text-purple-300" />
                <span>{{ label }}</span>
            </router-link>
        </template>

        
    </MegaMenu>
</template>
