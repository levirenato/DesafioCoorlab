/* eslint-disable vue/no-reserved-component-names */
/* eslint-disable vue/multi-word-component-names */
import './assets/main.css'
import 'primevue/resources/themes/aura-light-cyan/theme.css'
import 'primeicons/primeicons.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config'
import Sidebar from 'primevue/sidebar'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import Calendar from 'primevue/calendar';
import Dialog from 'primevue/dialog';

const app = createApp(App)

app.use(router)
app.use(PrimeVue,{
    locale:{    
    "accept": "Sim",
    "addRule": "Adicionar Regra",
    "am": "AM",
    "apply": "Aplicar",
    "cancel": "Cancelar",
    "choose": "Escolher",
    "chooseDate": "Escolher Data",
    "chooseMonth": "Escolher Mês",
    "chooseYear": "Escolher Ano",
    "clear": "Limpar",
    "completed": "Concluído",
    "contains": "Contém",
    "custom": "Personalizado",
    "dateAfter": "Data depois de",
    "dateBefore": "Data antes de",
    "dateFormat": "dd/mm/yy",
    "dateIs": "Data é",
    "dateIsNot": "Data não é",
    "dayNames": [
      "Domingo",
      "Segunda-feira",
      "Terça-feira",
      "Quarta-feira",
      "Quinta-feira",
      "Sexta-feira",
      "Sábado"
    ],
    "dayNamesMin": [
      "D",
      "S",
      "T",
      "Q",
      "Q",
      "S",
      "S"
    ],
    "dayNamesShort": [
      "Dom",
      "Seg",
      "Ter",
      "Qua",
      "Qui",
      "Sex",
      "Sáb"
    ],
    "firstDayOfWeek": 0,
    "monthNames": [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro"
      ],
      "monthNamesShort": [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez"
      ],
}
})



app.component('Sidebar', Sidebar)
app.component('InputText', InputText)
app.component('Button', Button)
app.component('Dropdown', Dropdown)
app.component('Calendar', Calendar)
app.component('Dialog', Dialog)


app.mount('#app')
