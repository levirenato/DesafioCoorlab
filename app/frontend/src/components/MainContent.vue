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
  align-content: flex-start;
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
  display: flex; align-items: center; justify-content: flex-start;
  flex-wrap: wrap;
  height: calc(100% - 4rem);
  width: 100%;
}
.calculateForm {
  align-items: center; justify-content: center;
  width: calc(45% * fit-content);padding: 1rem;
}
.search{
  flex-grow: 1;
  display: flex; justify-content: center; align-items: flex-start;
}
</style>
