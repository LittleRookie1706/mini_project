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
                    <!-- comment -->
                    <RateAndComment />
                    <!-- list comment -->
                    <v-container>
                        <CommentList :newsId="news.id" />
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
    import { newsConverter } from '@/assets/ts/newsConverter'

    // types
    import News from '@/types/News'

    // components
    const TopBar = defineAsyncComponent(() => import("@/components/TopBar.vue"))
    const CommentList = defineAsyncComponent(() => import("@/components/CommentList.vue"))
    import RateAndComment from '@/components/RateAndComment.vue'
    import Footer from '@/components/Footer.vue'

    const baseURL = ref("http://localhost:8000");
    const loginURL = ref("https://discord.com/api/oauth2/authorize?client_id=937351409198829681&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fdiscord_oauth&response_type=code&scope=identify%20email%20connections%20guilds%20guilds.members.read");
    const route = useRoute()
    
    const news = ref<News>({})

    async function fetchGetNews(newsId: number) {
        const response = await fetch(`${baseURL.value}/news/${newsId}`);
        if (!response.ok) {return {}}
        const result = await response.json()
        return result
    }

    onBeforeMount(async () =>{
        news.value = await fetchGetNews(route.params.newsId)
        news.value.content = newsConverter(news.value.content);
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
