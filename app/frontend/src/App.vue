<script setup>
import SideBar from './components/SideBar.vue'
import NavBar from './components/NavBar.vue'
import MainContent from './components/MainContent.vue'
</script>

<template>
  <SideBar class="sideBar" />
  <div class="content">
    <NavBar />
    <MainContent />
  </div>
</template>
<style scoped>
.sideBar {
  height: 100vh;
  width: 100%;
}

.content {
  display: flex;
  justify-content: flex-start;
  align-content: flex-start;
  flex-wrap: wrap;
  width: 100%;

  row-gap: 5%;
}
</style>
