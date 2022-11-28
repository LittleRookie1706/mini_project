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
            <v-btn v-if="pageNumber > 1" border="solid" color="#E0E0E0" variant="outlined" @click="pageLoad(pageNumber-1)">
              <router-link :to="{ name:'page', params: { pageNumber: pageNumber+1 } }">Prev</router-link>
            </v-btn>
            <v-btn color="#E0E0E0" variant="outlined" @click="pageLoad(pageNumber+1)" >
              <router-link :to="{ name:'page', params: { pageNumber: pageNumber+1 } }">Next</router-link>
            </v-btn>
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
  import * as fetchModule from '@/assets/ts/fetch.ts'

  // typescript
  import MinimumNews from '@/types/MinimumNews'
  import Tags from '@/types/Tags'

  // components
  const TopBar = defineAsyncComponent(() => import("@/components/TopBar.vue"))
  const Carousel = defineAsyncComponent(() => import("@/components/Carousel.vue"))
  const TagGroup = defineAsyncComponent(() => import("@/components/TagGroup.vue"))
  const NewsCard = defineAsyncComponent(() => import("@/components/NewsCard.vue"))
  const NewsGroup = defineAsyncComponent(() => import("@/components/NewsGroup.vue"))
  const Footer = defineAsyncComponent(() => import("@/components/Footer.vue"))

  const route = useRoute()

  let pageNumber = parseInt(route.params.pageNumber)

  const newsList = ref<MinimumNews[]>([])
  const slideshowList = ref<MinimumNews[]>([])
  const mostViewList = ref<MinimumNews[]>([])
  const tagsList = ref<Tags[]>([])
  const tagGroups = ref({})

  onBeforeMount(async () =>{
    if(!pageNumber){pageNumber=1}
    
    // fetch
    await Promise.all([
      fetchModule.fetchGetSlideshow(pageNumber),
      fetchModule.fetchGetNewsList(pageNumber),
      fetchModule.fetchGetMostView(),
      fetchModule.fetchGetTags()
    ]).then((values) => {
      slideshowList.value = values[0]
      newsList.value = values[1]
      mostViewList.value = values[2]
      tagsList.value = values[3]
    });

    // process data
    for(var i in tagsList.value){
      var tagGroupName = tagsList.value[i].tag_group
      delete tagsList.value[i].tag_group
      if(!tagGroups.value[tagGroupName]){ tagGroups.value[tagGroupName]=[] }
      tagGroups.value[tagGroupName].push(tagsList.value[i])
    }

  })

  function pageLoad(num: number) {
    console.log(num)
    pageNumber = num

    Promise.all([
      fetchModule.fetchGetSlideshow(pageNumber),
      fetchModule.fetchGetNewsList(pageNumber),
    ]).then((values) => {
      slideshowList.value = values[0]
      newsList.value = values[1]
    });
    window.scrollTo(0,0);
  }


</script>

<style scoped>

  .tags-group{
    /* position: fixed; */
    max-width: 400px;
  }

</style>
