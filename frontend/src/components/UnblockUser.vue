
<template>
    <button class="btn btn-info" @click="unblockUser(userId)">Unblock</button>
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

    const unblockUser = async (user_id) => {
        try {
            const response = await fetch('http://localhost:5000/api/unblock_user', {
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