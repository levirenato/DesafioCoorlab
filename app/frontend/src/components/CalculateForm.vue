<template>
    <form @submit="handleSubmit">
        <div class="title">
            <IconPayment />
            <h2>Calcule o valor da viagem</h2>
        </div>

        <div class="inputs">
            <div class="">
            <label for="selectedCity">Destino</label>
            <Dropdown inputId="selectedCity" v-model="selectedCity" 
             :options="transports" optionLabel="city" 
            placeholder="Selecione o destino" class="w-full md:w-14rem" style="width: 100%;"/>
        </div>
        <div class="">

            <label for="data" class="font-bold block mb-2"> Data </label>
            <Calendar v-model="selectedDate" showIcon iconDisplay="input"
            inputId="data" placeholder="Selecione a data" style="width: 100%;"/>
        </div>
        </div>


        
        <Button label="Buscar" style="width: 10rem; color:black;" @click="visible = validation()" />
        <Dialog v-model:visible="visible" modal style="height: 16rem; width: 30rem; display: flex; justify-content: center; text-align: center;" >
                <h2 style="margin: 1rem;">Insira os valores para iniciar a cotação</h2>
                <div class="flex justify-content-end gap-2">
                    <Button type="button" label="Fechar" @click="visible = false" style="width: 10rem; color:black;"></Button>
                </div>
        </Dialog>
    </form>
</template>

<script>
import IconPayment from './icons/IconPayment.vue'
import { ref } from "vue";

export default {
    name: "CalculateForm",

    data(){
        return {
            selectedDate : ref(),
            selectedCity : ref(),
            visible : ref(false),
            transports : [],
        }
    },
    
    methods: {
        validation() {
            if(this.selectedDate == undefined | this.selectedCity == undefined){
                return true
            }
           else{
               this.$router.replace(`/search/${this.selectedCity.city}`);
               return false
            }
        },
       getData(){
            fetch('http://127.0.0.1:3000/')
            .then(res => res.json())
            .then(data => this.transports = data)
       }
    },

    created(){
        this.getData()
    },

    components : {
        IconPayment,
    }
}
</script>

<style scoped>
form{
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    width: 25rem;
    height: 25rem;
    
    padding: 2rem;
    gap: 2rem;
    border-radius: 5px;
    background-color: var(--gray-1);
}
.title{
    display: flex;
    align-items: flex-start; justify-content: baseline;
    
}
.bt-submit{
    width: 10rem;
    justify-content: center;
    margin-top: 2rem;
}
</style>
