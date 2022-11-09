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

        <v-avatar id="avatar-dropdown" color="surface-variant"></v-avatar>
        <v-menu activator="#avatar-dropdown">
            <v-list>
                <v-list-item
                v-for="(item, index) in items"
                :key="index"
                :value="index"
                >
                <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>

    </v-app-bar>

</template>

<script setup lang="ts">
    import { ref } from 'vue';

    const items=ref([
        { title: 'Settings' },
        { title: 'Favourite' },
        { title: 'Logout' },
        ])

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