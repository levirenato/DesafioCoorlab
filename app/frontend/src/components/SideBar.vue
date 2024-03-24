<script setup>
import BtCalculator from './inputs/BtCalculator.vue';
import IconLogo from './icons/IconLogo.vue'
</script>

<template>
  <aside>
    <IconLogo />
    <BtCalculator />
  </aside>
</template>

<style scoped>
aside{
  background-color: var(--color-background-secondary);
  padding: 1.2rem;
  width: fit-content; height: 100vh;

  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: flex-start;
}

</style>
