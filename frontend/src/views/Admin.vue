<template>
    <v-app>
        <SideBar />
        <v-main class="ml-10">
            <v-container>
                <p class="text-h4 font-weight-bold">Filter</p>
            </v-container>
            <v-container>
                <p class="text-h4 font-weight-bold">News</p>
                <div class="d-flex justify-center">
                    <router-link :to="{ name:'ad-newspost', params: { newsId: 0 } }">
                        <v-btn class="elevation-10"><v-icon icon="fas fa-plus"></v-icon> Create new post</v-btn>
                    </router-link>
                </div>
                
                <v-row class="d-flex justify-center">
                    <v-col :cols="2">
                    </v-col>
                    <v-col :cols="8" >
                        <AdminNewsCard v-for="news in newsList" :key="news.id" :news="news"/>    
                        <div class="d-flex align-center flex-column pa-6 ma-5">
                            <v-btn-toggle>
                                    <v-btn v-if="pageNumber > 1" border="solid" color="#E0E0E0" variant="outlined" @click="pageLoad(pageNumber-1)">
                                        <router-link :to="{ name:'ad-page', params: { pageNumber: pageNumber-1 } }">Prev</router-link>
                                    </v-btn>
                                    <v-btn color="#E0E0E0" variant="outlined" @click="pageLoad(pageNumber+1)">
                                        <router-link :to="{ name:'ad-page', params: { pageNumber: pageNumber+1 } }">Next</router-link>
                                    </v-btn>
                            </v-btn-toggle>
                        </div>
                    </v-col>
                    <v-col :cols="2">
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
    
</template>

<script setup lang="ts">
    // default
    import { ref, onBeforeMount } from 'vue'
    import { useRoute } from 'vue-router'
    import * as fetchAPI from '@/assets/ts/fetch.ts'

    // typescripts
    import MinimumNews from '../types/News';

    // components
    import SideBar from '@/components/SideBar.vue'
    import AdminNewsCard from '@/components/AdminNewsCard.vue'

    const route = useRoute()
    var pageNumber = parseInt(route.params.pageNumber)

    const newsList = ref<MinimumNews[]>([])

    onBeforeMount(async () =>{
        if(!pageNumber){pageNumber=1}
        Promise.all([
        fetchAPI.fetchGetNewsList(pageNumber),
        ]).then((values) => {
            newsList.value = values[0]
        });
    })

    function pageLoad(num: number) {
        pageNumber = num
        Promise.all([
        fetchAPI.fetchGetNewsList(pageNumber),
        ]).then((values) => {
            newsList.value = values[0]
        });
        window.scrollTo(0,0);
    }

</script>

<style>

</style>