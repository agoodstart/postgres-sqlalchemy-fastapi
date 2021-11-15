import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

import axios from 'axios'
import App from './App.vue'

import { createApp } from 'vue'
import router from './router'


// fastapi
axios.defaults.baseURL = 'http://localhost:8000/'

createApp(App)
    .use(router)
    .mount('#app')
