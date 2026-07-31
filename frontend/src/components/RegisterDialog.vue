<script setup lang="ts">
    import { ref } from 'vue';
    import axios from 'axios';
    import { useRouter } from 'vue-router';
    import api from '@/services/api';
    import Dialog from 'primevue/dialog';
    import InputText from 'primevue/inputtext';
    import Password from 'primevue/password';
    import Button from 'primevue/button';
    import Message from 'primevue/message';

    import type { CreateUserPayload } from '@/models';

    const router = useRouter();

    const visible = ref(true);
    const error = ref('');
    const submitting = ref(false);

    const newUser = ref<CreateUserPayload>({
        username: '',
        password: ''
    });
    const confirmPassword = ref('');

    const register = async() => {
        if (newUser.value.password !== confirmPassword.value) {
            error.value = 'Passwords do not match.';
            return;
        }

        error.value = '';
        submitting.value = true;

        try {
            await api.post('register/', {
                username: newUser.value.username,
                password: newUser.value.password
            });

            sessionStorage.setItem('registration-success', 'Account created successfully. You can now log in.')
            router.push('/login');
        } catch (err) {
            if (axios.isAxiosError(err)) {
                const details = err.response?.data;
                error.value = Array.isArray(details?.username)
                    ? details.username[0]
                    : Array.isArray(details?.password)
                      ? details.password[0]
                      : 'We could not create your account. Please try again.';
            } else {
                error.value = 'We could not create your account. Please try again.';
            }
        } finally {
            submitting.value = false;
        }
    }
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
                <h1 id="register-title" class="text-xl font-semibold">Register</h1>
                <p class="mt-1 text-sm text-purple-300">Create a new account</p>
            </div>
        </template>

        <form class="flex flex-col gap-5" aria-labelledby="register-title" @submit.prevent="register">
            <div class="flex flex-col gap-2">
                <label for="username" class="font-medium">Username</label>
                <InputText
                    id="username"
                    v-model="newUser.username"
                    autocomplete="username"
                    placeholder="Your username"
                    required
                    fluid
                />
            </div>

            <div class="flex flex-col gap-2">
                <label for="password" class="font-medium">Password</label>
                <Password
                    input-id="password"
                    v-model="newUser.password"
                    autocomplete="new-password"
                    placeholder="Your password"
                    :feedback="false"
                    toggle-mask
                    required
                    fluid
                />
            </div>

            <div class="flex flex-col gap-2">
                <label for="confirm-password" class="font-medium">Confirm password</label>
                <Password
                    input-id="confirm-password"
                    v-model="confirmPassword"
                    autocomplete="new-password"
                    placeholder="Confirm your password"
                    :feedback="false"
                    toggle-mask
                    required
                    fluid
                />
            </div>

            <Message v-if="error" severity="error">{{ error }}</Message>
            <Button type="submit" label="Register" severity="help" class="w-full" :loading="submitting" />
        </form>

        <template #footer>
            <p class="text-sm text-purple-300">
                Already have an account?
                <router-link to="/login" class="text-white hover:underline">Log in</router-link>
            </p>
        </template>
    </Dialog>
</template>
<style scoped>

</style>
