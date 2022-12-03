<template>
    <v-card
        max-width="1000"
        class="mt-5 mx-auto elevation-7"
        v-if="show" 
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
                                    <v-row class="d-flex justify-center">
                                        <v-col cols="10">
                                            <v-card-title class="news-card-title">{{ news.title }}</v-card-title>
                                            <v-card-text>{{ news.description }}</v-card-text>
                                        </v-col>

                                        <v-col cols="2" class="d-flex">
                                            <router-link :to="{ name:'ad-newspost', params: { newsId: news.id } }">
                                                <v-btn icon="fas fa-pen"  color="white" class="elevation-5"></v-btn>  
                                            </router-link>
                                            <v-spacer></v-spacer>
                                            <v-btn icon="fas fa-trash" color="#FF6961" class="elevation-5" @click="deleteNews(news.id)"></v-btn>
                                        </v-col>
                                    </v-row>
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
    import { ref, defineProps } from 'vue';
    import * as fetchAPI from '@/assets/ts/fetch'
    const props = defineProps({ news: Object })
    let show = ref<boolean>(true)

    function deleteNews(news_id: number){
        Promise.all([
            fetchAPI.fetchDeleteNews(news_id)
        ]).then((values) => {
            if(values[0].status === 'success'){
                show.value = false
            }
        });
        
    }

</script>

<style>

    .news-card-title{
        white-space: normal;
    }

</style>