<template>

    <v-expansion-panels v-model="panel" multiple class="elevation-1 rounded-lg">

        <v-expansion-panel class="rounded-lg">
            <v-expansion-panel-title 
            :style="[
                {backgroundImage: 'url(' + require('../assets/images/header_banner_1.png') + ')' },
                {backgroundSize:'100%'},
                {backgroundPosition:'center bottom'}
            ]"
            :hide-actions="true"
            disable-icon-rotate
            class="d-flex justify-center align-center"
            disabled
            >
                <h3>Xem nhiều nhất</h3>  
            </v-expansion-panel-title>

            <router-link v-for="news in mostViewList" :key="news.id" :to="{ name:'newspost', params: { newsId: news.id }}">
                <v-card max-width="1000" class="mt-1 elevation-0" :id="news.id">
                    <v-row>
                        <v-col cols="12">
                            <v-card>
                                <div class="d-flex justify-space-between align-center">

                                    <v-avatar
                                        class="ml-5 my-5 rounded-lg"
                                        size="130"
                                        rounded="0"
                                    >
                                        <v-img :src="news.thumbnail_img"></v-img>
                                    </v-avatar>
                                    
                                    <v-row no-gutters>
                                        <v-container class="news-card-content">
                                            <v-card-title class="most-view-card-title">{{ news.title }}</v-card-title>
                                        </v-container>
                                    </v-row>

                                </div>
                            </v-card>
                        </v-col>
                    </v-row>    
                    <v-divider></v-divider>
                </v-card>
            </router-link>
            



        </v-expansion-panel>

    </v-expansion-panels>

</template>

<script setup lang="ts">
    import { ref, defineProps } from 'vue';

    const panel = ref([0, 0]);
    const props = defineProps({ mostViewList: Array })

</script>

<style>
    .most-view-card-title{
        font-size: medium;
        font-weight: 700;
        white-space: normal;
        line-height: 1.4rem !important;
    }


</style>