<template>
    <v-app>
        <v-main>
            <v-container>
                <p class="text-h4">Content</p>
                <div class="mt-10">
                        <v-row v-for="item in items" :key="item.subheader" class="ma-auto justify-center align-center">
                            <v-col cols="1">
                                <v-list-subheader>{{item.subheader}}</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-img v-if="item.type=='file' && item.modelValue!=''"
                                    :src="item.modelValue" 
                                    :max-width="item.length" 
                                    :max-height="item.height">
                                </v-img>
                                <v-file-input v-if="item.type=='file'"></v-file-input>
                                <v-combobox
                                    v-else-if="item.type=='multi-choice'"
                                    v-model="item.modelValue"
                                    :items="tagsList.map(tag => tag.name)"
                                    multiple
                                    chips
                                ></v-combobox>
                                <v-text-field v-else
                                    :model-value="item.modelValue"
                                    :type="item.type"
                                ></v-text-field>
                            </v-col>
                        </v-row>
                    </div>
                <v-container>
                    <v-row>
                        <v-col cols="1">
                            <v-list-subheader>Title</v-list-subheader>
                        </v-col>
                        <v-col cols="11">
                            <v-text-field v-model="news.title"></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="1">
                            <v-list-subheader>Content</v-list-subheader>
                        </v-col>
                        <v-col cols="11">
                            <v-textarea
                                v-model="news.content"
                                name="input-7-1"
                                variant="filled"
                                label="Label"
                                auto-grow
                            ></v-textarea>
                        </v-col>
                    </v-row>
                </v-container>
                <div class="d-flex justify-center">
                    <v-btn v-if="newsId==0" class="elevation-10 mx-5"><v-icon icon="fas fa-plus"></v-icon>Create</v-btn>
                    <v-btn class="elevation-10 mx-5" color="#4F77AA"><v-icon icon="fas fa-upload"></v-icon>Update</v-btn>
                    <v-btn class="elevation-10 mx-5" color="#FF6961"><v-icon icon="fas fa-trash"></v-icon>Delete</v-btn>
                </div>
            </v-container>
            <v-container>
                <p class="text-h4">Preview</p>
                <v-container class="d-flex justify-center mt-16">
                    <div class="w3-large">
                        <!-- Content container -->
                        <div class="w3-container" id="about">
                            <div class="w3-content" style="max-width:800px">
                                <h1 class="w3-center w3-padding-64"><span class="w3-tag w3-wide">{{news.title}}</span></h1>
                                <span v-html="news.content"></span>
                            </div>
                        </div>
                        <!-- list comment -->
                    </div>
                </v-container>
            </v-container>
        </v-main>
    </v-app>

</template>

<script setup lang="ts">
    // vue
    import { ref, defineAsyncComponent, onBeforeMount, watch  } from 'vue'
    import { useRoute } from 'vue-router'

    // types
    import News from '@/types/News'
    import Tags from '@/types/Tags'

    // components
    const TopBar = defineAsyncComponent(() => import("@/components/TopBar.vue"))
    import Footer from '@/components/Footer.vue'

    const baseURL = ref("http://localhost:8000")
    const route = useRoute()

    const newsId = parseInt(route.params.newsId)
    
    const news = ref<News>({})
    const newsTags = ref<Tags[]>([])
    const tagsList = ref<Tags[]>([])

    const items = ref([
        { subheader: 'Description', type:'text', modelValue:'', prefix:'', required: true },
        { subheader: 'Keywords', type:'text', modelValue:'', prefix:'', required: true },
        { subheader: 'Tags', type:'multi-choice', modelValue: [], prefix:'', required: true },
        { subheader: 'Thumnail_image', type:'file', modelValue: '', length: 200, height: 200, prefix:'', required: false },
        { subheader: 'Banner_image(Optional)', type:'file', modelValue:'', length: 650, height: 340, prefix:'', required: true },
        { subheader: 'Og_image(Optional)', type:'file', modelValue:'', length: 650, height: 340, prefix:'', required: false },
    ])

    async function fetchGetNews(newsId: number) {
        const response = await fetch(`${baseURL.value}/news/${newsId}`);
        if (!response.ok) {return {}}
        const result = await response.json()
        return result
    }

    async function fetchGetTags() {
        const response = await fetch(`${baseURL.value}/tags`);
        if (!response.ok) {return []}
        const result = await response.json()
        return result
    }

    async function fetchGetNewsTags(newsId: number) {
        const response = await fetch(`${baseURL.value}/news/${newsId}/tags`);
        if (!response.ok) {return []}
        const result = await response.json()
        return result
    }

    onBeforeMount(async () =>{    
        
        await Promise.all([
            fetchGetNews(newsId),
            fetchGetNewsTags(newsId),
            fetchGetTags(),
        ]).then((values) => {
            console.log(values)
            news.value = values[0]
            newsTags.value = values[1]
            tagsList.value = values[2]
        });

        items.value = [
            { subheader: 'Description', type:'text', modelValue: news.value.description, prefix:'', required: true },
            { subheader: 'Keywords', type:'text', modelValue: news.value.keywords, prefix:'', required: true },
            { subheader: 'Tags', type:'multi-choice', modelValue: newsTags.value.map(tag => tag.name), prefix:'', required: true },
            { subheader: 'Thumnail_image', type:'file', modelValue: news.value.thumbnail_img, length: 200, height: 200, prefix:'', required: false },
            { subheader: 'Banner_image(Optional)', type:'file', modelValue: news.value.banner_img, length: 650, height: 340, prefix:'', required: true },
            { subheader: 'Og_image(Optional)', type:'file', modelValue: news.value.og_img, length: 650, height: 340, prefix:'', required: false },
        ]

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
<style src="@/assets/css/rate.css" scoped></style>
<style src="@/assets/css/comment.css" scoped></style>
