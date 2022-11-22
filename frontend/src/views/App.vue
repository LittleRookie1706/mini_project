<template>

<v-app>
<TopBar :baseURL="baseURL" :loginURL="loginURL" />

<v-main>
  <v-container>Content area</v-container>

  <Carousel :slideshowList="slideshowList" />

  <v-container>
    <v-row class="d-flex justify-center">
      <v-col :cols="3" class="tags-group">
        <TagGroup :tagGroups="tagGroups" />
      </v-col>
      <v-col :cols="6" >
        <NewsCard :news="news" v-for="news in newsList" :key="news.id"/>
      </v-col>
      <v-col :cols="3" class="most-view">
        <NewsGroup :mostViewList="mostViewList" />
      </v-col>
    </v-row>
  </v-container>

  <div class="d-flex align-center flex-column pa-6">
    <v-btn-toggle>
      <v-btn border="solid" color="#E0E0E0" variant="outlined">Prev</v-btn>
      <v-btn color="#E0E0E0" variant="outlined">Next</v-btn>
    </v-btn-toggle>
  </div>

</v-main>

<Footer />
</v-app>

</template>

<script setup lang="ts">
import { ref, defineAsyncComponent, onBeforeMount } from 'vue';
import News from '../types/News';
const TopBar = defineAsyncComponent(() => import("../components/TopBar.vue"));
const Carousel = defineAsyncComponent(() => import("../components/Carousel.vue"));
const TagGroup = defineAsyncComponent(() => import("../components/TagGroup.vue"));
const NewsCard = defineAsyncComponent(() => import("../components/NewsCard.vue"));
const NewsGroup = defineAsyncComponent(() => import("../components/NewsGroup.vue"));
import Footer from '../components/Footer.vue';


const baseURL = ref("http://localhost:8000");
const loginURL = ref("https://discord.com/api/oauth2/authorize?client_id=937351409198829681&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fdiscord_oauth&response_type=code&scope=identify%20email%20connections%20guilds%20guilds.members.read");

const newsList = ref<News[]>([])
const slideshowList = ref<News[]>([])
const mostViewList = ref<News[]>([])
const tagsList = ref([])
const tagGroups = ref({})

async function fetchGetSlideshow() {
const response = await fetch(`${baseURL.value}/news/slideshow${1}`);
if (!response.ok) {return []}
const result = await response.json()
return result
}

async function fetchGetNews() {
const response = await fetch(`${baseURL.value}/news/news${1}`);
if (!response.ok) {return []}
const result = await response.json()
return result
}

async function fetchGetMostView() {
const response = await fetch(`${baseURL.value}/news/most-view`);
if (!response.ok) {return []}
const result = await response.json()
return result
}

async function fetchGetTags() {
const response = await fetch(`${baseURL.value}/news/tags`);
if (!response.ok) {return []}
const result = await response.json()
return result
}

onBeforeMount(async () =>{
// fetch
slideshowList.value = await fetchGetSlideshow()
newsList.value = await fetchGetNews()
mostViewList.value = await fetchGetMostView()
tagsList.value = await fetchGetTags()
// const slideshowPromise = fetchGetSlideshow()
// const newsPromise = fetchGetNews()
// const mostViewPromise = fetchGetMostView()
// const tagsPromise = fetchGetTags()

// async handle
// slideshowList.value, newsList.value, mostViewList.value, tagsList.value = await Promise.all([
//   slideshowPromise,
//   newsPromise,
//   mostViewPromise,
//   tagsPromise
// ])

// process data
for(var i in tagsList.value){
  var tagGroupName = tagsList.value[i].tag_group
  delete tagsList.value[i].tag_group
  if(!tagGroups.value[tagGroupName]){ tagGroups.value[tagGroupName]=[] }
  tagGroups.value[tagGroupName].push(tagsList.value[i])
}

})

</script>

<style>
.tags-group{
max-width: 400px;
}

.most-view{
max-width: 400px;
}

</style>
