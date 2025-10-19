<template>
  <div class="search-bar">
    <input v-model="q" placeholder="Cari username atau nama..." />
    <button @click="emitSearch">Cari</button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return { 
      q: ""
    };
  },
  methods: {
    emitSearch() {
      // Kirim query ke parent hanya saat tombol ditekan
      this.$emit('search', this.q);
    }
  }
};
</script>

<style scoped>
.search-bar {
  display: flex;
  gap: 10px;
  width: 100%;
  max-width: 500px;
}

.search-bar input {
  flex: 7;
  padding: 12px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 14px;
  background-color: #f9fafb;
  transition: all 0.3s ease;
}

.search-bar input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 6px rgba(37, 99, 235, 0.3);
  outline: none;
  background-color: white;
}

.search-bar button {
  flex: 3; 
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.25s ease, transform 0.15s ease;
}

.search-bar button:hover {
  background-color: #1e40af;
  transform: translateY(-1px);
}
</style>
