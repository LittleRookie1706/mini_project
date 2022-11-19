<template>

<v-container
  class="mt-10"
  style="max-width:980px;"

>  
    <v-carousel 
      cycle
      show-arrows-on-hover
      class="rounded-xl"
    >
      <v-carousel-item
        v-for="news in slideshowList"
        :key="news.id"
        :src="news.banner_img"
        :href="news.id"
        fit
        class="d-flex align-center justify-center"
      >
        <div :href="news.id" class="d-flex align-center justify-center">
          <h2 class="slideshow-title ma-5">
            {{ news.title }} 
          </h2>
        </div>

      </v-carousel-item>
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