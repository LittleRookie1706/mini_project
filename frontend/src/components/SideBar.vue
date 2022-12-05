<template>
    <v-navigation-drawer
        v-model="drawer"
        :rail="rail"
        permanent
        fixed
    >
        <v-list-item
            :prepend-avatar="currentUser.avatar"
            :title="currentUser.username"
            :subtitle="currentUser.email"
            @click="rail = !rail"
            nav
        >
        </v-list-item>
        <v-divider></v-divider>
        <v-list density="compact" nav>
            <v-list-item v-for="item in items" :key="item.id" :prepend-icon="item.icon" :title="item.title" :value="item.value" :active="item.active" :href="item.href"></v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script setup lang="ts">
    import { ref, defineProps, onMounted } from 'vue'
    import * as fetchAPI from '@/assets/ts/fetch.ts'

    const props = defineProps({ activeIcon: String })

    const rail = ref(true)
    const drawer = ref(true)
    const items = ref([
        { id: 1, title: 'Manage content', icon: 'fas fa-bars-progress', value: 'manage', active: false, href: '/admin/manage-content' },
        { id: 2, title: 'Statistic', icon: 'fas fa-chart-simple', value:'statistic', active: false, href: '/admin/statistic' },
    ])

    const currentUser = ref({})

    onMounted(async () =>{

        for (const i of Object.keys(items.value)) {
            if(items.value[i]['value']==props.activeIcon){
                items.value[i].active = true
            }
        }
        currentUser.value = await fetchAPI.fetchGetUser()
        
    })


</script>

<style>

</style>