<script setup lang="ts">
    import { onMounted, ref } from 'vue';
    import { useRouter } from 'vue-router';
    import api from '@/services/api';
    import Dialog from 'primevue/dialog';
    import InputText from 'primevue/inputtext';
    import Password from 'primevue/password';
    import Button from 'primevue/button';
    import Message from 'primevue/message';
    import { useToast } from 'primevue/usetoast';

    const router = useRouter();
    const toast = useToast();

    const visible = ref(true);
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

    onMounted(() => {
        const message = sessionStorage.getItem('registration-success');

        if (message) {
            toast.add({ severity: 'success', summary: 'Welcome to abboFM', detail: message, life: 5000 });
            sessionStorage.removeItem('registration-success');
        }
    });
</script>
<template>
    <Dialog
        v-model:visible="visible"
        modal
        :closable="false"
        :draggable="false"
        class="w-full max-w-md"
    >
        <template #header>
            <div>
                <h1 id="login-title" class="text-xl font-semibold">Welcome</h1>
                <p class="mt-1 text-sm text-purple-300">Login to your account</p>
            </div>
        </template>

        <form class="flex flex-col gap-5" aria-labelledby="login-title" @submit.prevent="login">
            <div class="flex flex-col gap-2">
                <label for="username" class="font-medium">
                    <font-awesome-icon icon="user" class="mr-2" />
                    Username
                </label>
                <InputText
                    id="username"
                    v-model="username"
                    autocomplete="username"
                    placeholder="Your username"
                    required
                    fluid
                />
            </div>

            <div class="flex flex-col gap-2">
                <label for="password" class="font-medium">
                    <font-awesome-icon icon="lock" class="mr-2" />
                    Password
                </label>
                <Password
                    input-id="password"
                    v-model="password"
                    autocomplete="current-password"
                    placeholder="Your password"
                    :feedback="false"
                    toggle-mask
                    required
                    fluid
                />
            </div>

            <Message v-if="error" severity="error">{{ error }}</Message>
            <Button type="submit" label="Enter" severity="help" class="w-full" />
        </form>

        <template #footer>
            <p class="text-sm text-purple-300">
                Don't have an account?
                <router-link to="/register" class="hover:underline text-white">Sign up</router-link>
            </p>
        </template>
    </Dialog>
</template>
<style scoped>

</style>
