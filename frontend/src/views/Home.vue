<template>

<v-app>
<TopBar :baseURL="baseURL" :loginURL="loginURL" />

<v-main>
  <v-container>Content area</v-container>
  <v-container>
    <v-row class="d-flex justify-center mt-10">
      <v-col :cols="2" class="tags-group mt-1">
        <TagGroup :tagGroups="tagGroups"/>
      </v-col>
      <v-col :cols="7" >
        <Carousel :slideshowList="slideshowList"/>
        <NewsCard v-for="news in newsList" :key="news.id" :news="news"/>
        <div class="d-flex align-center flex-column pa-6">
          <v-btn-toggle>
            <v-btn v-if="pageNumber > 1" border="solid" color="#E0E0E0" variant="outlined" :href="`/page/${pageNumber-1}`">Prev</v-btn>
            <v-btn color="#E0E0E0" variant="outlined" :href="`/page/${pageNumber+1}`">Next</v-btn>
          </v-btn-toggle>
        </div>
      </v-col>
      <v-col :cols="3" class="most-view mt-3">
        <NewsGroup :mostViewList="mostViewList" />
      </v-col>
    </v-row>
  </v-container>

</v-main>

<Footer />
</v-app>

</template>

<script setup lang="ts">
  // vue
  import { ref, defineAsyncComponent, onBeforeMount } from 'vue'
  import { useRoute } from 'vue-router'

  // typescript
  import MinimumNews from '@/types/MinimumNews'
  import Tags from '@/types/Tags'
  import TagGroups from '@/types/TagGroups'

  // components
  const TopBar = defineAsyncComponent(() => import("@/components/TopBar.vue"))
  const Carousel = defineAsyncComponent(() => import("@/components/Carousel.vue"))
  const TagGroup = defineAsyncComponent(() => import("@/components/TagGroup.vue"))
  const NewsCard = defineAsyncComponent(() => import("@/components/NewsCard.vue"))
  const NewsGroup = defineAsyncComponent(() => import("@/components/NewsGroup.vue"))
  const Footer = defineAsyncComponent(() => import("@/components/Footer.vue"))


  const baseURL = ref("http://localhost:8000");
  const loginURL = ref("https://discord.com/api/oauth2/authorize?client_id=937351409198829681&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fdiscord_oauth&response_type=code&scope=identify%20email%20connections%20guilds%20guilds.members.read");
  const route = useRoute()

  let pageNumber = parseInt(route.params.pageNumber)

  const newsList = ref<MinimumNews[]>([])
  const slideshowList = ref<MinimumNews[]>([])
  const mostViewList = ref<MinimumNews[]>([])
  const tagsList = ref<Tags[]>([])
  const tagGroups = ref({})

  async function fetchGetSlideshow(pageNumber: number) {
    const response = await fetch(`${baseURL.value}/news?page_number=${pageNumber}&is_slideshow=true`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
  }

  async function fetchGetNewsList(pageNumber: number) {
    const response = await fetch(`${baseURL.value}/news?page_number=${pageNumber}`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
  }

  async function fetchGetMostView() {
    const response = await fetch(`${baseURL.value}/news?order_by_view=true`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
  }

  async function fetchGetTags() {
    const response = await fetch(`${baseURL.value}/tags`);
    if (!response.ok) {return []}
    const result = await response.json()
    return result
  }

  onBeforeMount(async () =>{
    if(!pageNumber){pageNumber=1}
    
    // fetch
    // slideshowList.value = await fetchGetSlideshow(pageNumber)
    // newsList.value = await fetchGetNewsList(pageNumber)
    // mostViewList.value = await fetchGetMostView()
    // tagsList.value = await fetchGetTags()
    const slideshowPromise = fetchGetSlideshow(pageNumber)
    const newsPromise = fetchGetNewsList(pageNumber)
    const mostViewPromise = fetchGetMostView()
    const tagsPromise = fetchGetTags()

    // // async handle
    // [slideshowList.value, newsList.value, mostViewList.value, tagsList.value] = await Promise.all([
    //   slideshowPromise,
    //   newsPromise,
    //   mostViewPromise,
    //   tagsPromise,
    // ])
    slideshowList.value = await slideshowPromise
    newsList.value = await newsPromise
    mostViewList.value = await mostViewPromise
    tagsList.value = await tagsPromise

    // process data
    for(var i in tagsList.value){
      var tagGroupName = tagsList.value[i].tag_group
      delete tagsList.value[i].tag_group
      if(!tagGroups.value[tagGroupName]){ tagGroups.value[tagGroupName]=[] }
      tagGroups.value[tagGroupName].push(tagsList.value[i])
    }

  })

</script>

<style scoped>

  .tags-group{
    /* position: fixed; */
    max-width: 400px;
  }

</style>
