<template>
  <v-card
    max-width="600"
    class="mx-auto"
  >

    <v-container>
      <v-row dense>

        <v-col cols="12">
            <v-card
                color="#1F7087"
                theme="dark"
            >


                <div class="d-flex flex-no-wrap justify-space-between">
                    <v-avatar
                        class="ma-3"
                        size="150"
                        rounded="0"
                    >
                        <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
                    </v-avatar>
                    
                    <div>
                        <v-card-title class="text-h5">
                        Supermodel
                        </v-card-title>

                        <v-card-subtitle>Foster the People</v-card-subtitle>

                        <v-card-actions>
                        <v-btn
                            class="ml-2"
                            variant="outlined"
                            size="small"
                        >
                            START RADIO
                        </v-btn>
                        </v-card-actions>
                    </div>
                    <v-btn size="small" color="surface-variant" variant="text" icon="fas fa-heart"></v-btn>
                    <v-btn size="small" color="surface-variant" variant="text" icon="fas fa-eye"></v-btn>
                </div>
                
            </v-card>
        </v-col>

      </v-row>
    </v-container>
  </v-card>
</template>

<script setup lang="ts">
    import { ref } from 'vue';


</script>
  

<style>

</style>