<script setup>
import BtCalculator from './inputs/BtCalculator.vue';
import IconLogo from './icons/IconLogo.vue'

import { ref } from "vue";

const visible = ref(false);
</script>

<template>
  <nav>
    <Sidebar v-model:visible="visible" class="aside">
      <IconLogo />
      <BtCalculator />
  </Sidebar>
  <Button icon="pi pi-bars" @click="visible = true" class="button" />
  </nav>
</template>
<style>
.button{
      display: none;
      width: 36px;
      height: 36px;
    }

nav{
  display: flex;
  justify-content: flex-start; align-items: center;
  width: 100%;height: 5rem;
  padding: 1rem;

  box-shadow: var(--shadow-strong);

}
.aside{
  background-color: var(--color-background-secondary);
  padding: 1.2rem;
  width: max-content;

  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: flex-start;
}
@media (max-width:700px) {
    nav{
      min-width: 42rem;
    }
  }
@media (max-width:767px) {
    .button{
      display: block;
    }
    
  }
</style>
