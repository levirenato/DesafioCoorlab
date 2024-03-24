<template>
  <section class="search" v-if="transports && transports[0] && transports[0]['fastest']">
    <h2 class="title">Essas são as melhores alternativas de viagens na data selecionada: </h2>

      <div class="results">
        <div class="row">
      <div class="details">
        <div class="icon">
          <IconPayment />
        </div>
        <div class="information">
          <strong><h2>{{ transports[0]["fastest"].name }}</h2></strong>
          <h4>Leito: {{ transports[0]["fastest"].bed }} (completo)</h4>
          <h4>tempo estimado: {{ transports[0]["fastest"].duration }}</h4>
        </div>
      </div>
      <div class="preco">
        <strong><h2>Preço</h2></strong>
        <h4>{{ transports[0]["fastest"].price_confort }}</h4>
      </div>
    </div>

    <div class="row">
      <div class="details">
        <div class="icon">
          <IconClock />
        </div>
        <div class="information">
          <strong><h2>{{ transports[0]["most_economical"].name }}</h2></strong>
          <h4>Poltrona: {{ transports[0]["most_economical"].seat }} (Convencional)</h4>
          <h4>tempo estimado: {{ transports[0]["most_economical"].duration }}</h4>
        </div>
      </div>
      <div class="preco">
        <strong><h2>Preço</h2></strong>
        <h4>{{ transports[0]["most_economical"].price_econ }}</h4>
      </div>
    </div>
    <router-link to="/">
      <Button  label="Limpar" style="width: 10rem; color:black; background-color: var(--yellow);" class="clearButton"/>
    </router-link>
    
  </div>



  </section>
  
</template>

<script>
import IconPayment from '../components/icons/IconPayment.vue'
import IconClock from '../components/icons/IconClock.vue'
import ApiMixin from '@/mixins/ApiMixin';

export default {
    name: "SearchView",
    mixins: [ApiMixin],



    created(){
      this.getTransport(`http://127.0.0.1:3000/search/${this.$route.params.city}`);
    },

    watch:{
      $route(to){
        this.getTransport(`http://127.0.0.1:3000/search/${to.params.city}`);
      }
      
    },
    components : {
        IconPayment,
        IconClock,
    }
}
</script>

<style scoped>

.search{
  display: flex; flex-direction: column; flex-wrap: wrap;
  gap: 1.5rem;
  width: 100%;
}
.results{
  display: flex; flex-direction: column;
  align-items: flex-end;
  gap:1rem;
}
.row{
  flex-wrap: wrap;
  display: flex;
  gap: 10px;
}
.title{
  width: 25rem;
 text-align: start;
 text-wrap: wrap;
}
.details{
  display: flex;
}
.information{width:20vw;border-radius: 0 5px 5px 0;}
.title, .information {word-wrap: break-word;} 

.preco {width: 10rem;border-radius: 5px;}

.information, .preco {
  background-color: var(--gray-2);
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



  @media (max-width:1095px) {
    .row{
      height: 164px;
    }
    .information{
      width: 40vw;
    }
  }
  @media (max-width:767px) {
    .information{
      align-items: center;
      
    }
  }
  @media (max-width:700px) {
    .information{
      min-width: 20vh;
    }
  }
</style>
