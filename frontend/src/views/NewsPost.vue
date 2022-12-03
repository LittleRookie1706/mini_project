<template>
    <v-app>
        <TopBar :baseURL="baseURL" :loginURL="loginURL" />
        <v-main v-if="news.content">
            <v-container class="d-flex justify-center mt-16">

                <div class="w3-large">
                    <!-- Content container -->
                    <div class="w3-container" id="about">
                        <div class="w3-content" style="max-width:800px">
                            <h1 class="w3-center w3-padding-64"><span class="w3-tag w3-wide">{{news.title}}</span></h1>
                            <span v-html="news.content"></span>
                        </div>
                    </div>
                    
                    <v-container>
                        <RateAndComment :newsId="news.id" />
                    </v-container>
                </div>
            </v-container>
        </v-main>
        <Footer />
    </v-app>

</template>

<script setup lang="ts">
    // vue
    import { ref, defineAsyncComponent, onBeforeMount } from 'vue'
    import { useRoute } from 'vue-router'
    import { loginURL, fetchGetNews } from '@/assets/ts/fetch'

    // types
    import News from '@/types/News'

    // components
    const TopBar = defineAsyncComponent(() => import("@/components/TopBar.vue"))
    import RateAndComment from '@/components/RateAndComment.vue'
    import Footer from '@/components/Footer.vue'

    const route = useRoute()
    
    const news = ref<News>({})

    onBeforeMount(async () =>{
        news.value = await fetchGetNews(route.params.newsId)
    })
    
</script>

<style src="@/assets/css/newspost.css"></style>
<style>
    @import '@/assets/fonts/Inconsolata.css';

    p, ul{
        margin-bottom: 1rem;
    }

    a{
        color: #007bff;
        text-decoration: none;
        background-color: transparent;
    }

    h1{
        color: #fff;
        font-weight: 900;
    }

    h2{
        font-weight: 700;
        font-family: "Inconsolata", sans-serif;
    }

    img{
        object-fit: scale-down;
        max-width: 100%;
    }

</style>
<style src="@/assets/css/comment.css" scoped></style>
