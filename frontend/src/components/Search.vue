<template>
    <div class="container mt-4 d-flex justify-content-center mb-4">
      <input type="text" class="form-control w-50" :placeholder="placeholder" v-model="searchTerm" @input="onSearch"/>
    </div>
</template>
  
<script setup>
    import { ref } from 'vue';

    defineProps({
        placeholder: {
            type: String,
        },
    });

    const searchTerm = ref('');
    const emit = defineEmits(['search']);

    const onSearch = () => {
        emit('search', searchTerm.value);
    }

</script>
  