<template>
  <div class="table-container">
    <h2>Dashboard</h2>

    <!-- Search Bar -->
    <div class="search-container">
      <SearchBar :onSearch="onSearch" />
    </div>

    <!-- Loading -->
    <div v-if="loading" class="message">Memuat data...</div>

    <!-- User Table -->
    <UserTable 
      :users="filteredUsers" 
      @update="goToUpdate" 
      @delete="confirmDelete" 
    />

    <!-- Logout Button -->
    <button @click="logout" class="logout-btn">Logout</button>

    <!-- Messages -->
    <div v-if="msg" class="message success">{{ msg }}</div>
    <div v-if="error" class="message error">{{ error }}</div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import UserTable from '@/components/UserTable.vue';
import API from '@/services/api.js';

export default {
  name: 'Dashboard',
  components: {
    SearchBar,
    UserTable
  },
  data() {
    return {
      q: '',
      users: [],
      loading: false,
      msg: '',
      error: ''
    };
  },
  computed: {
    filteredUsers() {
      if (!this.q) return this.users;
      return this.users.filter(u =>
        u.username.toLowerCase().includes(this.q.toLowerCase()) ||
        u.nama.toLowerCase().includes(this.q.toLowerCase())
      );
    }
  },
  methods: {
    onSearch(query) {
      this.q = query;
    },
    goToUpdate(user) {
      this.$router.push(`/update/${user.id}`);
    },
    async confirmDelete(user) {
      if (confirm(`Hapus user ${user.username}?`)) {
        try {
          await API.delete(`/users/${user.id}`);
          this.msg = 'User berhasil dihapus';
          this.fetchUsers();
        } catch (err) {
          this.error = 'Gagal menghapus user: ' + (err.response?.data?.message || err.message);
        }
      }
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/');
    },
    async fetchUsers() {
      const token = localStorage.getItem('token');
      if (!token) {
        this.error = 'Token tidak ditemukan. Silakan login ulang.';
        this.logout();
        return;
      }

      this.loading = true;
      this.error = '';
      try {
        const response = await API.get('/users');
        this.users = response.data;
      } catch (err) {
        console.error('Full error details:', err);
        console.error('Response data:', err.response?.data);
        if (err.response?.status === 422 || err.response?.status === 401) {
          this.error = `Error ${err.response.status}: ${err.response?.data?.msg || 'Token tidak valid.'}`;
        } else {
          this.error = 'Gagal memuat data: ' + (err.response?.data?.message || err.message);
        }
      } finally {
        this.loading = false;
      }
    }
  },
  mounted() {
    this.fetchUsers();
  }
};
</script>

<style scoped>
.table-container {
  max-width: 900px;
  margin: 40px auto;
  background: white;
  padding: 25px;
  border-radius: 15px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #1e3a8a;
  font-weight: 700;
}

.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table th, table td {
  padding: 14px;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}

table th {
  background: #1e3a8a;
  color: white;
}

table tr:hover {
  background-color: #f1f5f9;
  cursor: pointer;
}

.message {
  margin-top: 15px;
  text-align: center;
  font-weight: 600;
}

.message.error {
  color: #dc2626;
}

.message.success {
  color: #16a34a;
}

.logout-btn {
  margin-top: 20px;
  background-color: #2563eb;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.25s ease, transform 0.15s ease;
  width: 100%;
}

.logout-btn:hover {
  background-color: #1e40af;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
