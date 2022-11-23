<template>

<v-container
  style="max-width:955px; padding: 0px;"
>  
    <v-carousel 
      cycle
      show-arrows-on-hover
      class="rounded-xl"
    >
      <router-link v-for="news in slideshowList" :key="news.id" :to="{ name:'newspost', params: { newsId: news.id }}">
        <v-carousel-item
          :src="news.banner_img"
          fit
          class="d-flex align-center justify-center"
        >
          <div class="d-flex align-center justify-center">
            <h2 class="slideshow-title ma-5">
              {{ news.title }} 
            </h2>
          </div>

        </v-carousel-item>
      </router-link>
    </v-carousel>
</v-container>

</template>

<script setup lang="ts">
  import { defineProps } from 'vue';

  const props = defineProps({ slideshowList: Array })

</script>


<style>
  .slideshow-title{
    width: 60%;
    white-space: normal;
    background: #fff;
    opacity: 0.75;
    font-size: 2.5rem;
    font-weight: 800;
    text-align: center;
  }
</style>