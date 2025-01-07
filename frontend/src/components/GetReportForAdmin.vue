<template>
    <button class="btn btn-info" @click="createReport">Get Report</button>
</template>

<script setup>

    const createReport = async () => {
        const response = await fetch('http://localhost:5000/create_report', {
            method: "GET",
            headers: {
                "Authentication-Token": localStorage.getItem("token")
            }
        })
        const task_id = (await response.json()).task_id

        const interval = setInterval(async () => {
            const response = await fetch(`http://localhost:5000/get_report/${task_id}`)
            if (!response.ok) {
                console.log('Report is being processed')
            }

            console.log('Report is ready to download')
            window.open(`http://localhost:5000/get_report/${task_id}`)
            alert('Report is downloaded')
            clearInterval(interval)

        }, 100)

    }
</script>