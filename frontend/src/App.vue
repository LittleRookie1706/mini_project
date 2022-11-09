<template>
  
  <v-app>
    
    <!-- <TopBar /> -->
    <v-app-bar
        app
        absolute
        color="#fcb69f"
        light
        height="200px"
    >
      <div class="d-flex justify-center align-center w-100">
        <v-btn @click="console.log('app-bar')">Get data</v-btn>
      </div>
        <!-- <v-img
            class="mx-2"
            :src="require('../assets/images/logo3.png')"
            max-height="45"
            max-width="45"
            contain
        ></v-img>

        <v-toolbar-title>BETTERME</v-toolbar-title>
        
        <v-responsive
            class="mx-auto"
            max-width="700"
        >
            <v-card-actions class="justify-center">
                <v-text-field
                    color="#fff"
                    label="Searching..."
                    prepend-icon="fa-sharp fa-solid fa-magnifying-glass"
                    variant="outlined"
                    hide-details
                ></v-text-field>
            </v-card-actions>
        </v-responsive>

        <v-spacer></v-spacer>

        <v-avatar id="avatar-dropdown" color="surface-variant"></v-avatar>
        <v-menu activator="#avatar-dropdown">
            <v-list>
                <v-list-item
                v-for="(item, index) in items"
                :key="index"
                :value="index"
                >
                <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
 -->
    </v-app-bar>

    <v-main>
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

const news = ref<News[]>([
      {id: 1, title: "xin chao moi nguoi", content: "abc"},
      {id: 2, title: "xin chao tat ca moi nguoi", content: "xyz"},  
    ])
</script>

<style>
</style>
