
<template>
    <button class="btn btn-warning me-2" @click="flagProfessional(professionalId)">Flag</button>
</template>

<script setup>

    defineProps({
        professionalId: {
            type: Number,
            required: true,
        },
    });

    const emit = defineEmits(['update']);

    const flagProfessional = async (professional_id) => {
        try {
            const response = await fetch('http://localhost:5000/api/professional/flag', {
                method: "PATCH",
                headers: {
                    "Content-Type": 'application/json',
                    "Authentication-Token": localStorage.getItem("token")
                },
                body: JSON.stringify({ professional_id })
            })
            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}`);
            }
            const data = await response.json();   
            alert(data.message)

            emit('update');
             
        } catch (error) {
            console.error("ERROR", error.message);
        }
    }
</script>