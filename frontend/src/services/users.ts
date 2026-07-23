import api from './api'
import type { User } from '@/models'

export const usersService = {
  getAll( user?: number ) {
    return api.get<User[]>('users/', { params: { user } })
  },
  getCurrentUser() {
    return api.get<User>('user/')
  }
}