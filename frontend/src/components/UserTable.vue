<template>
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Username</th>
        <th>Nama Lengkap</th>
        <th>Email</th>
        <th>Aksi</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="u in users" :key="u.id">
        <td>{{ u.id }}</td>
        <td>{{ u.username }}</td>
        <td>{{ u.nama }}</td>  
        <td>{{ u.email }}</td>  
        <td>
          <button @click="$emit('update', u)">Update</button>
          <button @click="$emit('delete', u)">Delete</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "UserTable",
  props: ["users"]
};
</script>