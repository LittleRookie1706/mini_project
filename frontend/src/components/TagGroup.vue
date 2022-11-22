<template>
  <v-container>
    <v-expansion-panels v-model="panel" multiple>

      <v-expansion-panel class="rounded-lg"
        v-for="[key, value] of Object.entries(tagGroups)"
        :key="key"
      >
        <v-expansion-panel-title 
          expand-icon="fa-solid fa-caret-down" 
          collapse-icon="fa-solid fa-caret-up" 
          :style="[
            {backgroundImage: 'url(' + require('../assets/images/header_banner_1.png') + ')' },
            {backgroundSize:'100%'},
            {backgroundPosition:'center bottom'}
          ]"
          disable-icon-rotate>
          <h3>{{key}}</h3>  
        </v-expansion-panel-title>
        <v-expansion-panel-text
          v-for="tag in value"
          :key="tag.id"
        >
          {{ tag.name }}
        </v-expansion-panel-text>
      </v-expansion-panel>

    </v-expansion-panels>
  </v-container>
</template>

<script setup lang="ts">
  import { ref, defineProps} from 'vue';

  const panel = ref([0, 1, 2]);
  const props = defineProps({ tagGroups: Object })

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