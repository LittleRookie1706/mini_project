<template>
  <v-container 
  
  >
    <v-expansion-panels v-model="panel" multiple>

      <v-expansion-panel class="rounded-lg">
        <v-expansion-panel-title 
          expand-icon="fa-solid fa-caret-down" 
          collapse-icon="fa-solid fa-caret-up" 
          :style="[
            {backgroundImage: 'url(' + require('../assets/images/header_banner_1.png') + ')' },
            {backgroundSize:'100%'},
            {backgroundPosition:'center bottom'}
          ]"
          disable-icon-rotate>
          <h3>TagsGroup</h3>  
        </v-expansion-panel-title>
        <v-expansion-panel-text>Tag</v-expansion-panel-text>
        <v-expansion-panel-text>Tag</v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel class="rounded-lg">
        <v-expansion-panel-title 
          expand-icon="fa-solid fa-caret-down" 
          collapse-icon="fa-solid fa-caret-up" 
          :style="[
            {backgroundImage: 'url(' + require('../assets/images/header_banner_1.png') + ')' },
            {backgroundSize:'100%'},
            {backgroundPosition:'center bottom'}
          ]"
          disable-icon-rotate>
          <h3>TagsGroup</h3>  
        </v-expansion-panel-title>
        <v-expansion-panel-text>Tag</v-expansion-panel-text>
        <v-expansion-panel-text>Tag</v-expansion-panel-text>
      </v-expansion-panel>

    </v-expansion-panels>
  </v-container>
</template>

<script setup lang="ts">
  import { ref } from 'vue';

  const panel = ref([0, 1]);
</script>

<style>
  h3{
    color: #fff;
  }

  .v-expansion-panel-text{
    color: black;
  }

  .fa-solid{
    color: #fff;
  }

</style>