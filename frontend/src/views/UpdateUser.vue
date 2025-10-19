<template>
  <div class="card">
    <h2>Update User</h2>
    <form @submit.prevent="doUpdate">
      <div>
        <label>Nama Lengkap</label>
        <input v-model="form.nama" type="text" required />
      </div>
      <div>
        <label>Email</label>
        <input v-model="form.email" type="email" required />
      </div>
      <div>
        <label>Username</label>
        <input v-model="form.username" type="text" required />
      </div>
      <button type="submit" :disabled="loading">
        {{ loading ? 'Updating...' : 'Update' }}
      </button>
      <button type="button" class="secondary" @click="goBack">Kembali</button>
      <div v-if="msg" class="message success">{{ msg }}</div>
      <div v-if="error" class="message error">{{ error }}</div>
    </form>
  </div>
</template>

<script>
import API from '../services/api'

export default {
  name: 'UpdateUser',
  data() {
    return {
      form: {
        nama: '',
        email: '',
        username: ''
      },
      loading: false,
      msg: '',
      error: ''
    }
  },
  async mounted() {
    await this.loadUserData()
  },
  methods: {
    async loadUserData() {
      try {
        const userId = this.$route.params.id
        console.log('Loading user data for ID:', userId)
        
        const response = await API.get(`/users/${userId}`)
        console.log('User data loaded:', response.data)
        
        this.form = {
          nama: response.data.nama,
          email: response.data.email,
          username: response.data.username
        }
      } catch (error) {
        console.error('Error loading user:', error)
        if (error.response && error.response.status === 404) {
          this.error = 'User tidak ditemukan'
        } else if (error.response && error.response.data) {
          this.error = error.response.data.message
        } else {
          this.error = 'Gagal memuat data user'
        }
      }
    },

    async doUpdate() {
      this.loading = true
      this.msg = ''
      this.error = ''

      try {
        const userId = this.$route.params.id
        console.log('Updating user ID:', userId, 'with data:', this.form)
        
        const response = await API.put(`/users/${userId}`, this.form)
        
        this.msg = response.data.message || 'Update berhasil'
        console.log('Update successful:', response.data)
        
        setTimeout(() => {
          this.$router.push('/dashboard')
        }, 1500)
      } catch (error) {
        console.error('Update error:', error)
        if (error.response && error.response.data) {
          this.error = error.response.data.message
        } else {
          this.error = 'Terjadi kesalahan saat update user'
        }
      } finally {
        this.loading = false
      }
    },

    goBack() {
      this.$router.push('/dashboard')
    }
  }
}
</script>