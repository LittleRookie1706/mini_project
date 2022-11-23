<template>
    <v-app>
        <SideBar :baseURL="baseURL" />
        <v-main class="ml-10">
            <v-container>
                <p class="text-h4 font-weight-bold">Filter</p>
            </v-container>
            <v-container>
                <p class="text-h4 font-weight-bold">News</p>
                <v-row class="d-flex justify-center mt-10">
                    <v-col :cols="2">
                    </v-col>
                    <v-col :cols="7" >
                        <router-view/>
                        <div class="d-flex align-center flex-column pa-6 ma-5">
                            <v-btn-toggle>
                                    <v-btn v-if="pageNumber > 1" border="solid" color="#E0E0E0" variant="outlined">
                                        <router-link :to="{ name:'ad-news', params: { pageNumber: pageNumber-1 } }">Prev</router-link>
                                    </v-btn>
                                    <v-btn color="#E0E0E0" variant="outlined">
                                        <router-link :to="{ name:'ad-news', params: { pageNumber: pageNumber+1 } }">Next</router-link>
                                    </v-btn>
                            </v-btn-toggle>
                        </div>
                    </v-col>
                    <v-col :cols="3">
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
    
</template>

<script setup lang="ts">
    import { ref, onBeforeMount } from 'vue'
    import { useRoute } from 'vue-router'

    import SideBar from '@/components/SideBar.vue'
    // import NewsCard from '@/components/NewsCard.vue'

    const baseURL = "http://localhost:8000"
    const route = useRoute()
    var pageNumber = parseInt(route.params.pageNumber)

    onBeforeMount(async () =>{
        if(!pageNumber){pageNumber=1}
    })

</script>

<style>

</style>