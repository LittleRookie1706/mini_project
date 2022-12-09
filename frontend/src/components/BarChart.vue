<template>
        <Bar
            :chart-options="chartOptions"
            :chart-data="chartData"
            :chart-id="chartId"
            :dataset-id-key="datasetIdKey"
            :plugins="plugins"
            :css-classes="cssClasses"
            :styles="styles"
            :width="width"
            :height="height"
        />

</template>

<script setup lang="ts">
    import { ref, PropType, onBeforeMount } from 'vue'

    // chartjs
    import { Bar } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Plugin } from 'chart.js'
    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

    const chartId = ref<string>('bar-chart')
    const datasetIdKey = ref<string>('label')
    const width = ref<number>(400)
    const height = ref<number>(400)
    const cssClasses = ref<string>('')
    const styles = ref<PropType<Partial<CSSStyleDeclaration>>>()
    const plugins = ref<PropType<Plugin<'bar'>>>()
    const chartData = ref({
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
    })
    const chartOptions = ref({
        responsive: true
    })

                                    

</script>

<style>

</style>