<template>
    <NewsCard v-for="news in newsList" :key="news.id" :news="news"/>    
</template>

<script setup lang="ts">
    import { ref, defineProps, onBeforeMount } from 'vue'

    import MinimumNews from '../types/News';

    const props = defineProps({ pageNumber: Number })
    const baseURL = "http://localhost:8000";

    const newsList = ref<MinimumNews[]>([])

    async function fetchGetNewsList(pageNumber: number) {
        const response = await fetch(`${baseURL}/news?page_number=${pageNumber}`)
        if (!response.ok) {return []}
        const result = await response.json()
        return result
    }

    onBeforeMount(async () =>{
        // if(!props.pageNumber){props.pageNumber=1}
        console.log(props.pageNumber)
        newsList.value = await fetchGetNewsList(props.pageNumber)
        console.log(newsList.value)
    })
</script>

<style>
</style>