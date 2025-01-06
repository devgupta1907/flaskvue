<script setup>

    defineProps({
        message: String,
        messageType: String
    })

    const emitClose = defineEmits(['close'])

</script>

<template>
    <div :class="['alert', `alert-${messageType}`, 'alert-dismissible', 'fade', 'show']" role="alert">
        {{ message }}
        <button type="button" @click="emitClose('close')" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
</template>