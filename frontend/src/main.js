import 'bootstrap/dist/css/bootstrap.min.css'
import '@fortawesome/fontawesome-free'
import 'bootstrap'

import axios from 'axios'
import App from './App.vue'

import { createApp } from 'vue'
import router from './router'


// fastapi
axios.defaults.baseURL = 'http://localhost:8000/api/v1'

let app = createApp(App)

app.use(router)
app.mount("#app")