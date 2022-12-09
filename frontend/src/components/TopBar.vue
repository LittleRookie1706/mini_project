<template>
    <v-app-bar
        app
        absolute
        color="#fcb69f"
        light
        :image="require('../assets/images/header_banner_1.png')" 
        height="200px"
    >

        <v-img
            class="ml-2"
            :src="require('../assets/images/logo3.png')"
            max-height="45"
            max-width="45"
            contain
        ></v-img>

        <v-toolbar-title>BETTERME</v-toolbar-title>
        
        <v-responsive
            class="mx-auto"
            max-width="800"
        >

            <v-card-actions class="d-flex justify-center align-center">
                <v-select
                    v-model="tagSelected"
                    :items="tagsList.map(tag => tag.name)"
                    variant="solo"
                    color="black"
                    single-line
                    hide-details
                    style="max-width: 140px;"
                ></v-select>
                <v-text-field
                    id="search-bar"
                    v-model="searchContent"
                    color="black"
                    label="Searching..."
                    variant="outlined"
                    hide-details
                ></v-text-field>
                <!-- prepend-icon="fa-sharp fa-solid fa-magnifying-glass" -->
                <v-menu 
                    activator="#search-bar" 
                    transition="slide-y-transition"
                    persistent
                >
                    <v-list v-show="showSearchResult">
                        <v-list-item-group>
                            <v-list-item
                                v-for="(item, i) in searchBarItems"
                                :key="i"
                                :href="item.id"
                            >
                                <v-row class="ma-auto justify-center">
                                    <v-col cols="2">
                                        <v-img :src="item.thumbnail_img" width="80"></v-img>
                                    </v-col>
                                    <v-col cols="10">
                                        <v-list-item-title v-text="item.title" ></v-list-item-title>
                                    </v-col>
                                </v-row>
                                <v-divider></v-divider>
                        </v-list-item>
                    </v-list-item-group>
                    </v-list>

                </v-menu>
            </v-card-actions>
        </v-responsive>

        <v-spacer></v-spacer>

        <div v-if="currentUser.id">
            <v-avatar id="avatar-dropdown" :image="currentUser.avatar"></v-avatar>
            <v-menu activator="#avatar-dropdown" transition="fab-transition">
                <v-list :items="userItems"></v-list>
            </v-menu>
        </div>
        <div v-else>
            <a :href="fetchAPI.loginURL" id="login-url">Login</a>
        </div>

    </v-app-bar>

</template>

<script setup lang="ts">
    import { ref, defineProps, onBeforeMount, watch } from 'vue'
    import * as fetchAPI from '@/assets/ts/fetch.ts'

    const prop = defineProps({ tagsList: Array })
    
    var currentUser = ref({})
    const userItems = ref([])

    const tagSelected = ref<string>('Tất cả')
    const searchContent = ref<string>('')
    const showSearchResult = ref<boolean>(false)

    const searchBarItems = ref([])


    function setAvatarDropdownFields() {
        var avatarDropdownFields = [
            { type: 'item', title: 'Settings' },
            { type: 'item', title: 'Favourite' },
            { type: 'item', title: 'Logout' },
        ]

        if(currentUser.value.is_admin){
            const avatarDropdownAdminFields=[
                { type: 'subheader', title: 'Admin' },
                { type: 'item', title: 'Manage page', props: { href: '/admin/manage-content' } },
                { type: 'divider' },
                { type: 'subheader', title: 'User' },
            ]
            avatarDropdownFields = [...avatarDropdownAdminFields, ...avatarDropdownFields]
        }

        return avatarDropdownFields
    }

    onBeforeMount(async () => {
        currentUser.value = await fetchAPI.fetchGetUser()
        userItems.value = setAvatarDropdownFields()
        console.log(tagId('Sinh học'))
    })

    function tagId(name: string){
        const object = prop.tagsList
        for (const i in object) {
            if(object[i]['name']==name){
                return object[i]['id']
            }
        }
        return null
    }

    watch(searchContent, async (content) => {
        if(content!=''){
            showSearchResult.value = true
            if(tagSelected.value=="Tất cả"){
                searchBarItems.value = await fetchAPI.fetchGetSearch(content, 0)
            }
            else{
                searchBarItems.value = await fetchAPI.fetchGetSearch(content, tagId(tagSelected.value))
            }
        }
        else{
            showSearchResult.value = false
        }  
    })

    watch(tagSelected, async (tag) => {
        console.log(tag, tagId(tag))
        if(searchContent.value!=''){
            if(tag=="Tất cả"){
                searchBarItems.value = await fetchAPI.fetchGetSearch(searchContent.value, 0)
            }
            else{
                searchBarItems.value = await fetchAPI.fetchGetSearch(searchContent.value, tagId(tag))
            }
        }
    })

</script>

<style>
    .v-field{
        color: #fff;
        background-color: #1c1f2f;
    }

    .v-toolbar-title{
        margin-left: 0px;
    }

    .v-toolbar-title__placeholder{
        color: #fff;
        font-family: fira sans,sans-serif;
        font-weight: 900;
    }

    .v-avatar{
        margin-right: 15px;
    }

    #avatar-dropdown{
        cursor: pointer;
    }

    #login-url{
        font-family: fira sans,sans-serif;
        font-weight: 700;
        color: #fff;
        text-decoration: none;
        margin-right: 25px;
    }

</style>