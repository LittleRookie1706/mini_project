<template>
  <v-card
    max-width="1000"
    class="mx-auto mt-5"
  >
      <v-row dense>
        <v-col cols="12">
            <v-card
                :class="['elevation-20', `rounded-lg`]"
            >
                <div class="d-flex flex-no-wrap justify-space-between">

                    <!-- thumbnail -->
                    <v-avatar
                        class="ml-5 my-5 rounded-lg"
                        size="150"
                        rounded="0"
                    >
                        <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
                    </v-avatar>
                    
                    <!-- Minimum content -->
                    <v-row no-gutters>
                        <v-container class="news-card-content">
                            <v-card-title class="news-card-title">Cộng hòa xã hội chủ nghĩa Việt Nam. Doc lap tu do hanh phuc</v-card-title>
                            <v-card-text>News Description asdklfhjs adf sdahfiokjsdaklf s adfjskda fjoisad fjksdahfjasdfklj asdfojiowaef awsf jasdkfjawspd f\</v-card-text>
                        </v-container>

                        <v-container class="d-flex align-end flex-column">
                            <v-sheet class="ma-1 mt-auto"><div>
                                <v-icon size="small" variant="text" icon="fas fa-heart"></v-icon> 50
                                <v-icon class="ml-1" size="small" variant="text" icon="fas fa-eye"></v-icon> 100
                            </div></v-sheet>
                            
                        </v-container>
                    </v-row>

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

    .news-card-title{
        white-space: normal;
    }

</style>