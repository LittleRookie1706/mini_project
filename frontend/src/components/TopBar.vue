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
            max-width="700"
        >
            <v-card-actions class="justify-center">
                <v-text-field
                    color="#fff"
                    label="Searching..."
                    prepend-icon="fa-sharp fa-solid fa-magnifying-glass"
                    variant="outlined"
                    hide-details
                ></v-text-field>
            </v-card-actions>
        </v-responsive>

        <v-spacer></v-spacer>

        <div v-if="currentUser.id">
            <v-avatar id="avatar-dropdown" :image="currentUser.avatar"></v-avatar>
            <v-menu activator="#avatar-dropdown" transition="fab-transition">
                <!-- <v-list>
                    <v-list-item
                    v-for="(item, index) in items"
                    :key="index"
                    :value="index"
                    >
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item>
                </v-list> -->
                <v-list :items="items"></v-list>
            </v-menu>
        </div>
        <div v-else>
            <a :href="fetchAPI.loginURL" id="login-url">Login</a>
        </div>

    </v-app-bar>

</template>

<script setup lang="ts">
    import { ref, defineProps, onBeforeMount } from 'vue'
    import * as fetchAPI from '@/assets/ts/fetch.ts'
    
    var currentUser = ref({})
    const items = ref([])


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
        items.value = setAvatarDropdownFields()
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