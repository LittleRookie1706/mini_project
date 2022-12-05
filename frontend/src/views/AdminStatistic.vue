<template>
    <v-app>
        <SideBar :activeIcon="activeIcon" />
        <v-main class="ml-10">
            <v-container>
                <p class="text-h4 font-weight-bold">Filter</p>
            </v-container>
            <v-container>
                <p class="text-h4 font-weight-bold">Statistic</p>
                
            </v-container>
        </v-main>
    </v-app>
    
</template>

<script setup lang="ts">
    // default
    import { ref, onBeforeMount } from 'vue'
    import { useRoute } from 'vue-router'
    import * as fetchAPI from '@/assets/ts/fetch.ts'

    // components
    import SideBar from '@/components/SideBar.vue'

    const route = useRoute()
    var pageNumber = parseInt(route.params.pageNumber)
    const activeIcon = ref<string>('statistic')


</script>

<style>

</style>