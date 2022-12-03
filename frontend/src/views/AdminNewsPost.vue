<template>
    <v-app>
        <v-main>
            <v-container>
                <p class="text-h4">Content</p>
                <v-container class="mt-10">
                    <v-form>
                        <!-- <v-row v-for="item in items" :key="item.subheader" class="ma-auto justify-center align-center">
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
                                    :v-model="item.modelValue"
                                    :type="item.type"
                                ></v-text-field>
                            </v-col>
                        </v-row> -->
                        <!-- start -->
                        <v-row class="ma-auto justify-center align-center">
                            <v-col cols="1">
                                <v-list-subheader>Description</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-text-field
                                    v-model="news.description"
                                    type="text"
                                ></v-text-field>
                            </v-col>
                        </v-row>
                        <v-row class="ma-auto justify-center align-center">
                            <v-col cols="1">
                                <v-list-subheader>Keywords</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-text-field
                                    v-model="news.keywords"
                                    type="text"
                                ></v-text-field>
                            </v-col>
                        </v-row>
                        <v-row class="ma-auto justify-center align-center">
                            <v-col cols="1">
                                <v-list-subheader>Tags</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-combobox
                                    v-model="tagsSelect"
                                    :items="tagsList.map(tag => tag.name)"
                                    multiple
                                    chips
                                ></v-combobox>
                            </v-col>
                        </v-row>
                        <v-row class="ma-auto justify-center align-center">
                            <v-col cols="1">
                                <v-list-subheader>Thumbnail image</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-img
                                    :src="news.thumbnail_img" 
                                    :max-width="200" 
                                    :max-height="200">
                                </v-img>
                                <v-file-input id="thumbnail-image"></v-file-input>
                            </v-col>
                        </v-row>
                        <v-row class="ma-auto justify-center align-center">
                            <v-col cols="1">
                                <v-list-subheader>Banner image</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-img
                                    :src="news.banner_img" 
                                    :max-width="650" 
                                    :max-height="340">
                                </v-img>
                                <v-file-input id="banner-image"></v-file-input>
                            </v-col>
                        </v-row>
                        <v-row class="ma-auto justify-center align-center">
                            <v-col cols="1">
                                <v-list-subheader>Opengraph image</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-img
                                    :src="news.og_img" 
                                    :max-width="650" 
                                    :max-height="340">
                                </v-img>
                                <v-file-input id="og-image"></v-file-input>
                            </v-col>
                        </v-row>
                        <!-- end -->
                        <v-row>
                            <v-col cols="1">
                                <v-list-subheader>Title</v-list-subheader>
                            </v-col>
                            <v-col cols="11">
                                <v-text-field v-model="news.title"></v-text-field>
                            </v-col>
                        </v-row>
                        <editor
                            :init="{
                                height: 900,
                                menubar: false,
                                plugins: [
                                'advlist autolink lists link image charmap print preview anchor',
                                'searchreplace visualblocks code fullscreen',
                                'insertdatetime media table paste code help wordcount'
                                ],
                                toolbar:
                                'undo redo | formatselect | bold italic backcolor | \
                                alignleft aligncenter alignright alignjustify | \
                                bullist numlist outdent indent | removeformat | help'
                            }"
                            v-model="news.content"
                        />
                    </v-form>
                </v-container>
                <div class="d-flex justify-center">
                    <v-btn v-if="newsId==0" class="elevation-10 mx-5" @click="createNews()"><v-icon icon="fas fa-plus"></v-icon>Create</v-btn>
                    <v-btn v-else class="elevation-10 mx-5" color="#4F77AA" @click="updateNews(news.id)"><v-icon icon="fas fa-upload"></v-icon>Update</v-btn>
                    <v-btn class="elevation-10 mx-5" color="#FF6961"><v-icon icon="fas fa-trash" ></v-icon>Delete</v-btn>
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
    import { ref, defineAsyncComponent, onBeforeMount } from 'vue'
    import { useRoute } from 'vue-router'
    import Editor from '@tinymce/tinymce-vue'
    import { fetchGetTags, fetchGetNewsTags, fetchGetNews, fetchDeleteNews, fetchUpdateNews, fetchCreateNews } from '@/assets/ts/fetch'
    import { compareObject } from '@/assets/ts/module'

    // types
    import News from '@/types/News'
    import Tags from '@/types/Tags'
    interface UpdateObject{
        [key: string]: any
    }

    // components
    const TopBar = defineAsyncComponent(() => import("@/components/TopBar.vue"))
    import Footer from '@/components/Footer.vue'
    const editor = Editor

    const route = useRoute()

    const newsId: number = parseInt(route.params.newsId)
    
    const news = ref<News>({})
    let originalNews = {}
    const newsTags = ref<Tags[]>([])
    const tagsList = ref<Tags[]>([])
    const tagsSelect = ref([])

    // const items = ref([
    //     { subheader: 'Description', type:'text', modelValue: '', prefix:'', required: true },
    //     { subheader: 'Keywords', type:'text', modelValue: '', prefix:'', required: true },
    //     { subheader: 'Tags', type:'multi-choice', modelValue: [], prefix:'', required: true },
    //     { subheader: 'Thumnail_image', type:'file', modelValue: '', length: 200, height: 200, prefix:'', required: false },
    //     { subheader: 'Banner_image(Optional)', type:'file', modelValue: '', length: 650, height: 340, prefix:'', required: true },
    //     { subheader: 'Og_image(Optional)', type:'file', modelValue: '', length: 650, height: 340, prefix:'', required: false },
    // ])



    onBeforeMount(async () =>{    
        if(newsId!=0){
            await Promise.all([
                fetchGetNews(newsId),
                fetchGetNewsTags(newsId),
                fetchGetTags(),
            ]).then((values) => {
                news.value = values[0]
                newsTags.value = values[1]
                tagsList.value = values[2]
                originalNews = JSON.parse(JSON.stringify(values[0]))
            });
            
            // items.value = [
            //     { subheader: 'Description', type:'text', modelValue: news.value.description, prefix:'', required: true },
            //     { subheader: 'Keywords', type:'text', modelValue: news.value.keywords, prefix:'', required: true },
            //     { subheader: 'Tags', type:'multi-choice', modelValue: newsTags.value.map(tag => tag.name), prefix:'', required: true },
            //     { subheader: 'Thumnail_image', type:'file', modelValue: news.value.thumbnail_img, length: 200, height: 200, prefix:'', required: false },
            //     { subheader: 'Banner_image(Optional)', type:'file', modelValue: news.value.banner_img, length: 650, height: 340, prefix:'', required: true },
            //     { subheader: 'Og_image(Optional)', type:'file', modelValue: news.value.og_img, length: 650, height: 340, prefix:'', required: false },
            // ]
            tagsSelect.value = newsTags.value.map(tag => tag.name)
        }
        else{
            await Promise.all([
                fetchGetTags(),
            ]).then((values) => {
                tagsList.value = values[0]
            }); 
        }

    })

    function createNews(){

        const thumbnailImage = document.getElementById('thumbnail-image')
        const bannerImage = document.getElementById('banner-image')
        const ogImage = document.getElementById('og-image')

        Promise.all([
            fetchCreateNews(
                news.value, 
                thumbnailImage, bannerImage, ogImage, 
                tagsList.value.filter(tag => tagsSelect.value.includes(tag.name)).map(tag => tag.id)
            )
        ]).then((values) => {
            console.log(values)
        });

    }

    function updateNews(news_id: number){

        const thumbnailImage = document.getElementById('thumbnail-image')
        const bannerImage = document.getElementById('banner-image')
        const ogImage = document.getElementById('og-image')
        const result: UpdateObject = compareObject(originalNews, news.value)

        Promise.all([
            fetchUpdateNews(
                news.value.id, 
                result, 
                thumbnailImage, bannerImage, ogImage, 
                tagsList.value.filter(tag => tagsSelect.value.includes(tag.name)).map(tag => tag.id)
            )
        ]).then((values) => {
            console.log(values)
        });

    }
    

    function deleteNews(newsId: number){
        // Promise.all([fetchDeleteNews(newsId)]).then((values) => {
        //     if(values[0].status === 'success'){
        //         console.log(123)
        //     }
        // });
        console.log('xyz')
        
    }
    

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
