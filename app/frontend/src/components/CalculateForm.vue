<script setup>
import IconPayment from './icons/IconPayment.vue'
import { ref } from "vue";

const selectedDate = ref();
const selectedCity = ref();
const cities = ref([
    { name: 'New York', code: 'NY' },
    { name: 'Rome', code: 'RM' },
    { name: 'London', code: 'LDN' },
    { name: 'Istanbul', code: 'IST' },
    { name: 'Paris', code: 'PRS' }
]);
</script>

<template>
    <form method="get">
        <div class="title">
            <IconPayment />
            <h2>Calcule o valor da viagem</h2>
        </div>
        <label for="selectedCity">Destino</label>
        <Dropdown inputId="selectedCity" v-model="selectedCity" 
        v-tooltip.top="'Selecione um destino'"
        editable :options="cities" optionLabel="name" 
        placeholder="Selecione o destino" class="w-full md:w-14rem" style="width: 100%;"/>
        
        <div class="flex-auto cyan-600">
            <label for="data" class="font-bold block mb-2"> Data </label>
            <Calendar v-model="selectedDate" showIcon iconDisplay="input" 
            v-tooltip.top="'Selecione uma data'"
            inputId="data" placeholder="Selecione a data" style="width: 100%;"/>
        </div>

        <router-link to="/search" rel="noopener" class="bt-submit">
            <Button label="Buscar" style="width: 10rem;" />
        </router-link>
        
    </form>
</template>

<style scoped>
form{
    display: flex; flex-direction: column;
    justify-content: center;
    width: 100%;
    height: 25rem;
    
    padding: 2rem;

    border-radius: 5px;
    background-color: var(--gray-1);
}
.title{
    display: flex;
    align-items: flex-end; justify-content: baseline;
    margin-bottom: 2rem;
    gap: 0.4rem;
}
.bt-submit{
    width: 10rem;
    justify-content: center;
    margin-top: 2rem;
}
</style>
