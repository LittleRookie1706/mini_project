<template>
  <v-card
    max-width="700"
    class="mx-auto mt-5"
  >

      <v-row dense>

        <v-col cols="12">
            <v-card
                color="#1F7087"
                theme="dark"
            >
                <div class="d-flex flex-no-wrap justify-space-between">
                    <v-avatar
                        class="ma-5 rounded-lg"
                        size="150"
                        rounded="0"
                    >
                        <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
                    </v-avatar>
                    
                    <div>
                        <v-card-title class="text-h4">
                        Supermodel
                        </v-card-title>

                        <v-card-text>Foster the People</v-card-text>
                        <!-- <div class="d-flex align-center flex-row"> -->
                            <v-icon size="small" variant="text" icon="fas fa-heart"></v-icon>50
                            <v-icon size="small" variant="text" icon="fas fa-eye"></v-icon>100
                        <!-- </div> -->
                    </div>
                </div>
                
            </v-card>
        </v-col>

      </v-row>
  </v-card>
</template>

<script setup lang="ts">
    import { ref } from 'vue';


</script>
  

<style>

</style>