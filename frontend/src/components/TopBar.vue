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
            class="mx-2"
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

        <v-avatar id="avatar-dropdown" :image="currentUser.avatar"></v-avatar>
        <v-menu activator="#avatar-dropdown">
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

    </v-app-bar>

</template>

<script setup lang="ts">
    import { ref, defineProps, onBeforeMount } from 'vue';

    const props = defineProps({ baseURL: String })
    var currentUser = ref({})
    const items=ref([])

    const accessToken = 'gOQ8wdVSmMxnvv72av0PVYmmjZWkJh'

    const myHeaders = new Headers({
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/x-www-form-urlencoded'
    })


    async function fetchGetUser() {
        const response = await fetch(`${props.baseURL}/get-user`,
        {   method: 'GET', 
            headers: myHeaders
        });
        if (!response.ok) {throw new Error(`An error has occured: ${response.status}`)}
        const user = await response.json()
        return user
    }

    function setAvatarDropdownFields() {
        var avatarDropdownFields = [
            { title: 'Settings' },
            { title: 'Favourite' },
            { title: 'Logout' },
        ]

        if(currentUser.value.is_admin){
            const avatarDropdownAdminFields=[
                { type: 'subheader', title: 'Admin' },
                {title: 'Manage page'},
                { type: 'divider' },
                { type: 'subheader', title: 'User' },
            ]
            avatarDropdownFields = [...avatarDropdownAdminFields, ...avatarDropdownFields]
        }

        return avatarDropdownFields
    }

    
    onBeforeMount(async () => {

        currentUser.value = await fetchGetUser()
        items.value = setAvatarDropdownFields()

    })



</script>

<style>
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
</style>