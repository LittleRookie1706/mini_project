<template>
    <v-app>
        
        <v-main class="ml-10">
            <SideBar :activeIcon="activeIcon" />
            <v-container>
                <p class="text-h4 font-weight-bold">Filter</p>
                <v-container class="d-flex align-center">
                    <v-select
                        v-model="timeRangeSelected"
                        :items="['Daily', 'Weekly', 'Monthly']"
                        variant="solo"
                        color="black"
                        single-line
                        hide-details
                        style="max-width: 140px"
                    ></v-select>
                    <Datepicker v-model="date" :format="formatDate" range multi-calendars class="mx-5"/>
                    <!-- <Datepicker v-model="startDate" range class="mx-5"></Datepicker>
                    <Datepicker v-model="endDate" range class="mx-5"></Datepicker> -->
                </v-container>
            </v-container>
            <v-container>
                <p class="text-h4 font-weight-bold">Statistic</p>
                <v-row class="d-flex justify-center align-center">
                    <v-col :cols="8">
                        <v-hover v-slot="{ isHovering, props }">
                            <v-card id="view-by-date" class="ma-5 pa-5 rounded-xl" :class="{ 'on-hover': isHovering }" :elevation="isHovering ? 16 : 5"  v-bind="props">
                                <BarChart />
                            </v-card>
                        </v-hover>
                    </v-col>
                    <v-col :cols="4">
                        <v-hover v-slot="{ isHovering, props }">
                            <v-card id="view-by-date" class="mxa-5 pa-5 rounded-xl" :class="{ 'on-hover': isHovering }" :elevation="isHovering ? 16 : 5"  v-bind="props">
                                <BarChart />
                            </v-card>
                        </v-hover>
                    </v-col>
                </v-row>
                <v-hover v-slot="{ isHovering, props }">
                    <v-card id="view-by-date" class="ma-5 pa-5 rounded-xl" :class="{ 'on-hover': isHovering }" :elevation="isHovering ? 16 : 5"  v-bind="props">
                        <BarChart />
                    </v-card>
                </v-hover>
                <v-hover v-slot="{ isHovering, props }">
                    <v-card id="view-by-date" class="mx-5 mt-10 pa-5 rounded-xl" :class="{ 'on-hover': isHovering }" :elevation="isHovering ? 16 : 5"  v-bind="props">
                        <BarChart />
                    </v-card>
                </v-hover>
            </v-container>
        </v-main>
    </v-app>
    
</template>

<script setup lang="ts">
    // default
    import { ref, onBeforeMount, watch } from 'vue'
    import * as fetchAPI from '@/assets/ts/fetch'
    import Datepicker from '@vuepic/vue-datepicker'
    import '@vuepic/vue-datepicker/dist/main.css'
    import { getDateString } from '@/assets/ts/module'

    // components
    import SideBar from '@/components/SideBar.vue'
    import BarChart from '@/components/BarChart.vue'

    const activeIcon = ref<string>('statistic')

    const timeRangeSelected = ref<string>('Daily')
    const endDate: Date = new Date()
    const startDate: Date = new Date(new Date().setDate(endDate.getDate() - 7))
    const date = ref<Array<Date>>([startDate, endDate])
    const formatDate = (date: Array<Date>) => {return `${getDateString(date[0])} -> ${getDateString(date[1])}`}
    
    const chartData = ref({
        labels: [],
        datasets: [ { data: [] } ]
    })

    // const monthLabel: Array<string> = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October', 'November','December' ]
    // const weekLabel: Array<string> = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

    onBeforeMount(async () => {
        await fetchAPI.fetchGetStatistic(getDateString(date.value[0]), getDateString(date.value[1]), true, true, true, true)
    })

    watch(date, async (newDate) => {
        await fetchAPI.fetchGetStatistic(getDateString(newDate[0]), getDateString(newDate[1]), true, true, true, true)
    })

</script>

<style>
    .widget{
        max-height: 500px;
    }

    #bar-chart{
        max-height: 450px;
    }
</style>