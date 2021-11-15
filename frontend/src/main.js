// import '@babel/polyfill'
// import 'mutationobserver-shim'
// import './plugins/bootstrap-vue'
// import BootstrapVue from 'bootstrap-vue'
import axios from 'axios'
// import Vue from 'vue'
import App from './App.vue'

import { createApp } from 'vue'
import router from './router'


// fastapi
axios.defaults.baseURL = 'http://localhost:8000/'

// new Vue({
//     router: router,t
//     render: home => home(App)
// }).$mount('#app');

createApp(App)
    .use(router)
    // .use(BootstrapVue)
    .mount('#app')
