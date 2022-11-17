<template>
    <v-footer 
      color="black" 
      class="d-flex flex-column" 
      :style="[
              {backgroundImage: 'url(' + require('../assets/images/header_banner_1.png') + ')' },
              {backgroundSize:'100%'},
              {backgroundPosition:'center bottom'}
      ]"
    >
      <v-row justify="center" no-gutters>
        <v-btn
          v-for="link in links"
          :key="link"
          variant="text"
          class="mx-2"
          rounded="xl"
        >
          {{ link }}
        </v-btn>
        <v-col class="text-center mt-4" cols="12">
          {{ new Date().getFullYear() }} — <strong>Betterme</strong>
        </v-col>
      </v-row>
    </v-footer>
  </template>

<script setup lang="ts">
    const links = [
        'Home',
        'About Us',
        'Privacy and Policy',
        'Contact Us',
    ]

</script>

<style>

</style>