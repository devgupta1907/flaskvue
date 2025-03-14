<template>
    <div class="container mt-2">
        <h3 class="text-center display-6 my-2">MadyPro Admin Dashboard</h3>
        <div class="row">
            <div class="text-center">
                <p class="lead">The Control Center of MadyPro Household Services Application</p>
            </div>
        </div>
        <GetReportForAdmin />

        <!-- Chart Section -->
        <div class="row justify-content-center mt-4">
            <div class="col-md-8 text-center">
                <img v-if="chartSrc" :src="chartSrc" alt="Services Chart" class="img-fluid"/>
                <p v-else>Loading chart...</p>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import GetReportForAdmin from './GetReportForAdmin.vue';

    const chartSrc = ref('');

    const createChart = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/chart');
            const data = await response.json();

            if (response.ok) {
                chartSrc.value = `/src/assets/graphs/${data.filename}`;
            } else {
                console.error('Error fetching chart:', data);
            }
        } catch (error) {
            console.error('Network error:', error);
        }
    };

    
    onMounted(() => {
        createChart();
    });
</script>
