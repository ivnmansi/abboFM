import { ref } from 'vue';
import { usersService } from '@/services/users';
import type { User } from '@/models';

export function useUsers() {
    const users = ref<User[]>([]);
    const currentUser = ref<User|null>(null);

    const fetchCurrentUser = async () => {
        try {
            const response = await usersService.getCurrentUser();
            currentUser.value = response.data;
        }
        catch (error) {
            console.error('Error fetching current user:', error);
        }
    };

    const fetchUsers = async (user?: number) => {
        try {
            const response = await usersService.getAll(user);
            users.value = response.data;
        }
        catch (error) {
            console.error('Error fetching users:', error);
        }
    };

    return {
        users,
        currentUser,
        fetchCurrentUser,
        fetchUsers
    };
}