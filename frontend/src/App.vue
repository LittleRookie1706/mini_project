<template>
  
  <v-app>
    
    <TopBar :baseURL="baseURL" />

    <v-main>
      <v-container>Content area</v-container>
      <Carousel />
      <NewsCard />
    </v-main>
    <Footer />

  </v-app>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import News from './types/News';
import TopBar from './components/TopBar.vue';
import Carousel from './components/Carousel.vue';
import NewsCard from './components/NewsCard.vue';
import Footer from './components/Footer.vue';

const baseURL = ref("http://localhost:8000");

const news = ref<News[]>([
      {id: 1, title: "xin chao moi nguoi", content: "abc"},
      {id: 2, title: "xin chao tat ca moi nguoi", content: "xyz"},  
    ])
</script>

<style>
</style>
