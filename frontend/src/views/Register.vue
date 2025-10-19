<template>
  <div>
    <h2>Registrasi</h2>
    <form @submit.prevent="doRegister">
      <div><input v-model="nama" placeholder="nama lengkap" required /></div>
      <div><input v-model="email" placeholder="email" required /></div>
      <div><input v-model="username" placeholder="username" required /></div>
      <div><input v-model="password" type="password" placeholder="password" required /></div>
      <div><button type="submit">Registrasi</button></div>
    </form>
    <div v-if="error" style="color:red">{{ error }}</div>
    <div v-if="success" style="color:green">{{ success }}</div>
  </div>
</template>

<script>
import API from "../services/api";

export default {
  data() {
    return { username: "", password: "", email: "", nama: "", error: "", success: "" };
  },
  methods: {
    async doRegister() {
      this.error = ""; this.success = "";
      // basic email check
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(this.email)) {
        this.error = "Format email tidak valid";
        return;
      }
      try {
        const res = await API.post("/users/register", {
          username: this.username,
          password: this.password,
          email: this.email,
          nama: this.nama
        });
        this.success = "Registrasi berhasil. Mengarahkan ke login...";
        setTimeout(() => this.$router.push({ name: "Login" }), 1200);
      } catch (err) {
        this.error = err.response?.data?.message || "Gagal registrasi";
      }
    }
  }
};
</script>
