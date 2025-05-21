import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('User', () => {
  const user = ref(0)

  return { user }
})
