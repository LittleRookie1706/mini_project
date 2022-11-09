<template>

<v-container>  
    <v-carousel :show-arrows="false">
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        fit
      ></v-carousel-item>
    </v-carousel>
</v-container>

</template>

<script setup lang="ts">
  import { ref } from 'vue';

  const items = ref([
        {
          src: 'https://e.khoahoc.tv/photos/image/2022/11/08/Gaia-BH1-black-hole-650-size-650x340-znd.jpg',
        },
        {
          src: 'https://e.khoahoc.tv/photos/image/2022/11/08/kiem-thien-thach-650-size-650x340-znd.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        },
      ])

</script>


<style>

</style>