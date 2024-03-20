<script setup>
import { RouterLink, RouterView } from 'vue-router'
import IconTruck from './icons/IconTruck.vue'
</script>

<template>
  <div>
    <header class="title">
      <IconTruck />
      <h2>Calculadora de Viagem</h2>
    </header>
    <main>
      <section class="calculateForm">
        formulario
        <RouterLink to="/search">Buscar</RouterLink>
      </section>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
div {
  display: flex;
  flex-wrap: wrap;
  width: calc(82vw);
  height: 35rem;

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
  display: flex;
  flex-wrap: wrap;
  height: 100%;
  width: 100%;
}
.calculateForm {
  height: 100%;
  width: 40%;
}
</style>
