/* eslint-disable vue/no-reserved-component-names */
/* eslint-disable vue/multi-word-component-names */
import './assets/main.css'
import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primeicons/primeicons.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config'
import Sidebar from 'primevue/sidebar'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'

const app = createApp(App)
app.use(router)
app.use(PrimeVue)

app.component('Sidebar', Sidebar)
app.component('InputText', InputText)
app.component('Button', Button)

app.mount('#app')
