<script setup>
import { RouterView } from 'vue-router'
import IconTruck from './icons/IconTruck.vue'
import CalculateForm from './CalculateForm.vue'


</script>

<template>
  <div>
    <header class="title">
      <IconTruck />
      <h2>Calculadora de Viagem</h2>
    </header>
    <main>
      <section class="calculateForm">
        <CalculateForm />
      </section>
      <section class="search">
        <RouterView />
      </section>
    </main>
  </div>
</template>

<style scoped>
div {
  display: flex;
  flex-wrap: wrap;
  flex-grow: 1;
  align-content: center;
  width: min-content;
  height: min-content;

  margin: 1rem;

  box-shadow: var(--shadow-ligth);
  border-radius: 5px;
}
.title {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  height: 4rem;
  padding-left: 2rem;

  border-radius: 5px 5px 0 0;

  background-color: var(--color-background-secondary);
  color: var(--text-color-white);
}
main {
  display: flex; align-items: center; justify-content: flex-start;
  flex-wrap: wrap; width: 100%;
}
.calculateForm {
  align-items: center; justify-content: center;
  width: min-content;padding: 1rem;
}
.search{
  display: flex; justify-content: center; align-items: flex-start;
}

@media (max-width:1095px) {
    main{
      align-items: center; justify-content: center;
    }
    .row{
      width: 164px;
    }
  }
  @media (max-width:767px) {
    .search{
      align-items: center;
      width: 40rem;
    }
  }
</style>
