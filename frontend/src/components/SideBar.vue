<template>
    <!-- <v-navigation-drawer
        expand-on-hover
        rail
    >
        <v-list>
        <v-list-item
            :prepend-avatar="currentUser.avatar"
            :title="currentUser.username"
            :subtitle="currentUser.email"
        ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
            <v-list-item v-for="item in items" :key="item.id" :prepend-icon="item.icon" :title="item.title" :value="item.value"></v-list-item>
        </v-list>
    </v-navigation-drawer> -->
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
            <!-- <template v-slot:append>
                <v-btn
                    variant="text"
                    icon="fas fa-angle-left"
                    @click="rail = true"
                ></v-btn>
            </template> -->
        </v-list-item>

        <v-divider></v-divider>

        <v-list density="compact" nav>
            <v-list-item v-for="item in items" :key="item.id" :prepend-icon="item.icon" :title="item.title" :value="item.value" :active="item.active"></v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script setup lang="ts">
    import { ref, defineProps, onMounted } from 'vue'


    const props = defineProps({ baseURL: String})

    const rail = ref(true)
    const drawer = ref(true)
    const items = ref([
        { id: 1, title: 'Manage content', icon: 'fas fa-bars-progress', value: 'manage', active: true },
        { id: 2, title: 'Statistic', icon: 'fas fa-chart-simple', value:'statistic', active: false },
    ])
    
    const accessToken = 'gOQ8wdVSmMxnvv72av0PVYmmjZWkJh'
    // gOQ8wdVSmMxnvv72av0PVYmmjZWkJh

    const myHeaders = new Headers({
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/x-www-form-urlencoded'
    })
    const currentUser = ref({})

    async function fetchGetUser() {
        const response = await fetch(`${props.baseURL}/users/self/`,
        {   method: 'GET', 
            headers: myHeaders
        });
        if (!response.ok) {return {}}
        const user = await response.json()
        return user
    }

    onMounted(async () =>{
        currentUser.value = await fetchGetUser()
    })


</script>

<style>

</style>