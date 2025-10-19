<template>
  <div class="card">
    <h2>Login</h2>
    <form @submit.prevent="doLogin">
      <div>
        <label>Username</label>
        <input v-model="username" required />
      </div>
      <div>
        <label>Password</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Masuk</button>
      <button type="button" class="secondary" @click="$router.push({name:'Register'})">
        Registrasi Akun Baru
      </button>
      <div v-if="error" class="message error">{{ error }}</div>
    </form>
  </div>
</template>

<script>
import API from "../services/api";
import { setToken } from "../store/auth";
export default {
  data() {
    return { username: "", password: "", error: "" };
  },
  methods: {
    async doLogin() {
      this.error = "";
      try {
        const res = await API.post("/users/login", {
          username: this.username,
          password: this.password
        });
        setToken(res.data.token);
        this.$router.push({ name: "Dashboard" });
      } catch (err) {
        this.error = err.response?.data?.message || "Login gagal";
      }
    }
  }
};
</script>
