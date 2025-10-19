1. Installasi dan konfigurasi
   1) Install Node.js
   2) Install Phyton
   3) Install MySQL Workbench
   4) Install Vue.js + Flask untuk frontend dan backend, berikut adalah kode utamanya
      a. frontend
   	 npm create vue@latest
   	 npm install
      b. backend
   	 py -m venv .venv
   	 pip install flask
   	 pip install flask\_restful
   	 pip install flask\_sqlalchemy
   	 flask db init
   (Install juga library tambahan seperti axios, flask\_cors, flask\_jwt\_extended jika dibutuhkan)

   
2. Pembuatan Database dengan query:
   CREATE TABLE users (
   id BIGINT PRIMARY KEY AUTO\_INCREMENT,
   username VARCHAR(50) NOT NULL UNIQUE,
   password VARCHAR(255) NOT NULL,
   email VARCHAR(100) NOT NULL UNIQUE,
   nama VARCHAR(100) NOT NULL,
   created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP
   );
   
3. Melakukan koneksi db
   import axios from "axios";

   const API = axios.create({
     baseURL: import.meta.env.VITE\_API\_URL || "http://127.0.0.1:5000",
     timeout: 5000,
   });

   API.interceptors.request.use((config) => {
     const token = localStorage.getItem("token");
     if (token) {
       config.headers.Authorization = `Bearer ${token}`;
     }
     return config;
   });
   export default API;
   
4. Inisialisasi data, Pembuatan CRUD dan Controller

   
5. Konfigurasi API dengan :
   import axios from "axios";

   const API = axios.create({
     baseURL: import.meta.env.VITE\_API\_URL || "http://127.0.0.1:5000",
     timeout: 5000,
   });

   API.interceptors.request.use((config) => {
     const token = localStorage.getItem("token");
     if (token) {
       config.headers.Authorization = `Bearer ${token}`;
     }
     return config;
   });

   export default API;



6\. Alur web

&nbsp;  Login/Registrasi > Halaman Utama > Tampil data user > Aksi CRUD

&nbsp;  

7\. Cara run project

&nbsp;  jalankan backend : flask run

&nbsp;  jalankan frontend : npm run dev 



8\. Teknologi yang digunakan :

&nbsp;  - Frontend: Vue.js, Axios

&nbsp;  - Backend: Flask, Flask-RESTful, SQLAlchemy

&nbsp;  - Database: MySQL
   



