
<template>
    <button class="btn btn-danger" @click="blockUser(userId)">Block</button>
</template>

<script setup>
    import { defineProps } from 'vue';

    defineProps({
        userId: {
            type: Number,
            required: true,
        },
    });

    const emit = defineEmits(['update']);

    const blockUser = async (user_id) => {
        try {
            const response = await fetch('http://localhost:5000/api/user/block', {
                method: "POST",
                headers: {
                    "Content-Type": 'application/json',
                    "Authentication-Token": localStorage.getItem("token")
                },
                body: JSON.stringify({ user_id })
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