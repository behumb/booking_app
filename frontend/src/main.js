import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './style.css'


const app = createApp(App)
app
    .use(store)
    .use(router, axios)
app.mount('#app')