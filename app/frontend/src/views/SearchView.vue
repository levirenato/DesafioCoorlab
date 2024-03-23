<script setup>
import IconPayment from './../components/icons/IconPayment.vue';
</script>
<template>
  <section class="search">
    <h2 class="title">Essas são as melhores alternativas de viagens na data selecionada: </h2>
    <div class="row">
      <div class="details">
        <div class="icon">
          <IconPayment />
        </div>
        <div class="information">
          <strong><h2>Nome da transportadora</h2></strong>
          <h4>Leito:</h4>
          <h4>tempo estimado:</h4>
        </div>
      </div>
      <div class="preco">
        <h4>Preço</h4>
        <h4>100 R$</h4>
      </div>
    </div>

    <div class="row">
      <div class="details">
        <div class="icon">
          <IconPayment />
        </div>
        <div class="information">
          <strong><h2>Nome da transportadora</h2></strong>
          <h4>Leito:</h4>
          <h4>tempo estimado:</h4>
        </div>
      </div>
      <div class="preco">
        <h4>Preço</h4>
        <h4>100 R$</h4>
      </div>
    </div>
  </section>
</template>

<style scoped>
.search{
  display: flex; flex-direction: column; flex-wrap: wrap;
  gap: 1.5rem;
  width: max-content;
}
.row{
  display: flex;
  gap: 10px;
}
.title{
 text-align: start;
}
.details{
  display: flex;
}

.title, .information {width: 25rem;}

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
