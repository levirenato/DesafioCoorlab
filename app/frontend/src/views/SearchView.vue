<template>
  <section class="search">
    <div class="row">
      <h2 class="title">Essas são as melhores alternativas de viagens na data selecionada: </h2>
      <div class="details">
        <div class="icon">
          <IconPayment />
        </div>
        <div class="information">
          <strong><h2>{{ find[0].fastest.name }}</h2></strong>
          <h4>Leito: {{ find[0].fastest.bed }} (completo)</h4>
          <h4>tempo estimado: {{ find[0].fastest.duration }}</h4>
        </div>
      </div>
      <div class="preco">
        <strong><h2>Preço</h2></strong>
        <h4>{{ find[0].fastest.price_confort }}</h4>
      </div>
    </div>

    <div class="row">
      <div class="details">
        <div class="icon">
          <IconPayment />
        </div>
        <div class="information">
          <strong><h2>{{ find[1].most_economical.name }}</h2></strong>
          <h4>Poltrona: {{ find[1].most_economical.seat }} (Convencional)</h4>
          <h4>tempo estimado: {{ find[1].most_economical.duration }}</h4>
        </div>
      </div>
      <div class="preco">
        <strong><h2>Preço</h2></strong>
        <h4>{{ find[1].most_economical.price_econ }}</h4>
      </div>
    </div>
  </section>
</template>

<script>
import IconPayment from '../components/icons/IconPayment.vue'


export default {
    name: "SearchView",

    data(){
    return {
            find : [],
        }
      },
      methods:{
        getTransport(){
          fetch(`http://127.0.0.1:3000/search/${this.$route.params.city}`)
          .then(res => res.json())
          .then(data => this.find = data)
        }
      },
     created(){
         this.getTransport();
    },
    components : {
        IconPayment,
    }
}
</script>

<style scoped>
.search{
  display: flex; flex-direction: column; flex-wrap: wrap;
  gap: 1.5rem;
  width: max-content;
}
.row{
  flex-wrap: wrap;
  display: flex;
  gap: 10px;
}
.title{
 text-align: start;
}
.details{
  display: flex;
}

.title, .information {word-wrap: break-word;} 

.preco {width: 10rem;}

.information, .preco {
  background-color: var(--gray-2);
  border-radius: 5px;
}

.icon{
  display: flex; align-items: center;
  background-color: var(--cyan);
  border-radius: 5px 0 0 5px ;
}

.information, .preco, .icon {
  padding: 10px;
  display: grid; align-items: center; justify-content: flex-start;
  }
</style>
