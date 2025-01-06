
<template>
    <button class="btn btn-info" @click="activateProfessional(professionalId)">Activate</button>
</template>

<script setup>
    import { defineProps } from 'vue';

    defineProps({
        professionalId: {
            type: Number,
            required: true,
        },
    });

    const emit = defineEmits(['update']);

    const activateProfessional = async (professional_id) => {
        try {
            const response = await fetch('http://localhost:5000/api/professional/activate', {
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