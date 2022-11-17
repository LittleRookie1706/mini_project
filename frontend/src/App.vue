<template>
  
  <v-app>
    
    <TopBar :baseURL="baseURL" :loginURL="loginURL" />

    <v-main>
      <v-container>Content area</v-container>

      <Carousel />

      <v-container class="d-flex justify-center">
        <v-row>
          <v-col :cols="3" class="tags-group">
            <TagGroup />
          </v-col>
          <v-col :cols="6" >
            <NewsCard />
            <NewsCard />
            <NewsCard />
            <NewsCard />
            <NewsCard />
          </v-col>
          <v-col :cols="3" class="most-view">
            <TagGroup />
          </v-col>
        </v-row>
      </v-container>

      <div class="d-flex align-center flex-column pa-6">
        <v-btn-toggle>
          <v-btn border="solid" color="#E0E0E0" variant="outlined">Prev</v-btn>
          <v-btn color="#E0E0E0" variant="outlined">Next</v-btn>
        </v-btn-toggle>
      </div>

    </v-main>

    <Footer />
  </v-app>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import News from './types/News';
import TopBar from './components/TopBar.vue';
import Carousel from './components/Carousel.vue';
import TagGroup from './components/TagGroup.vue';
import NewsCard from './components/NewsCard.vue';
import NewsGroup from './components/NewsGroup.vue';
import Footer from './components/Footer.vue';

const baseURL = ref("http://localhost:8000");
const loginURL = ref("https://discord.com/api/oauth2/authorize?client_id=937351409198829681&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fdiscord_oauth&response_type=code&scope=identify%20email%20connections%20guilds%20guilds.members.read");

const news = ref<News[]>([
      {id: 1, title: "xin chao moi nguoi", content: "abc"},
      {id: 2, title: "xin chao tat ca moi nguoi", content: "xyz"},  
    ])
</script>

<style>
  .tags-group{
    max-width: 400px;
  }

  .most-view{
    max-width: 400px;
  }
</style>
