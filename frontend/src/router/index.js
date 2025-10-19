import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Dashboard from "../views/Dashboard.vue";
import UpdateUser from "../views/UpdateUser.vue";

const routes = [
  { path: "/", component: Login, name: "Login" },
  { path: "/register", component: Register, name: "Register" },
  {
    path: "/dashboard",
    component: Dashboard,
    name: "Dashboard",
    meta: { requiresAuth: true }
  },
  {
    path: "/update/:id",
    component: UpdateUser,
    name: "UpdateUser",
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");
  if (to.meta.requiresAuth && !token) {
    next({ name: "Login" });
  } else {
    next();
  }
});

export default router;
