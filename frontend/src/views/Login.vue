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
    <main class="min-vh-100 d-flex align-items-center py-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-sm-10 col-md-8 col-lg-5 col-xl-4">
                    <section class="card border-1 shadow-sm" aria-labelledby="login-title">
                        <div class="card-body p-4 p-sm-5">
                            <div class="text-center mb-4">
                                <span class="badge text-bg-primary mb-3 px-3 py-2">Welcome</span>
                                <h1 id="login-title" class="h3 fw-bold mb-2">Login</h1>
                                <p class="text-body-secondary mb-0">Enter your details to continue.</p>
                            </div>

                            <form @submit.prevent="login">
                                <div class="mb-3">
                                    <label for="username" class="form-label fw-semibold">Username</label>
                                    <input id="username" v-model="username" class="form-control form-control-lg" type="text" autocomplete="username" placeholder="Tu nombre de usuario" required>
                                </div>

                                <div class="mb-4">
                                    <label for="password" class="form-label fw-semibold">Password</label>
                                    <input id="password" v-model="password" class="form-control form-control-lg" type="password" autocomplete="current-password" placeholder="Tu contraseña" required>
                                </div>

                                <div v-if="error" class="alert alert-danger py-2" role="alert">{{ error }}</div>
                                <button type="submit" class="btn btn-primary btn-lg w-100">Enter</button>
                            </form>
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </main>
</template>
