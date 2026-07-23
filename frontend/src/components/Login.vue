<script setup lang="ts">
    import {ref} from 'vue';
    import { useRouter } from 'vue-router';
    import api from '@/services/api';

    const router = useRouter();

    const username = ref('');
    const password = ref('');
    const error = ref('');

    const login = async() => {
        try {
            const res = await api.post('/token-auth/', {
                username: username.value,
                password: password.value
            });

            localStorage.setItem('token', res.data.token);
            error.value = '';
            router.push('/');
        } catch (err) {
            error.value = 'Invalid credentials';
        }
    }
</script>


<template>
    <form @submit.prevent="login">
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Login</button>
        <p v-if="error" style="color: red;">{{ error }}</p>
    </form>

</template>