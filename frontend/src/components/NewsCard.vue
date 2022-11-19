<template>
  <v-card
    max-width="1000"
    class="mt-5 mx-auto elevation-7"
    :id="news.id" 
    :href="news.id"
  >
      <v-row dense>
        <v-col cols="12">
            <v-card class="rounded-lg">
                <div class="d-flex flex-no-wrap justify-space-between align-center">

                    <!-- thumbnail -->
                    <v-avatar
                        class="ml-5 my-5 rounded-lg"
                        size="150"
                        rounded="0"
                    >
                        <v-img :src="news.thumbnail_img"></v-img>
                    </v-avatar>
                    
                    <!-- Minimum content -->
                    <v-row no-gutters>
                        <v-container class="news-card-content">
                            <v-card-title class="news-card-title">{{ news.title }}</v-card-title>
                            <v-card-text>{{ news.description }}</v-card-text>
                        </v-container>

                        <v-container class="d-flex align-end flex-column">
                            <v-sheet class="ma-1 mt-auto ">
                                <div>
                                <v-icon size="small" variant="text" icon="fas fa-star" color="#FFB144"></v-icon> {{ news.rating }}
                                <v-icon class="ml-1" size="small" variant="text" icon="fas fa-eye" color="#4F77AA"></v-icon> {{ news.view }}
                                </div>
                            </v-sheet>
                            
                        </v-container>
                    </v-row>

                </div>
            </v-card>
        </v-col>

      </v-row>
  </v-card>
</template>

<script setup lang="ts">
    import { defineProps} from 'vue';
    // import News from '../types/News';

    // const props = defineProps = ({
    //     type: Object as PropType<News[]>,
    //     required: true
    // })
    const props = defineProps({ news: Object })

</script>
  

<style>

    .news-card-title{
        white-space: normal;
    }

</style>