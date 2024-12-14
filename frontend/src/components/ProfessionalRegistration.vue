<template>
    <div>
        <div class="mb-3">
            <label for="pincode" class="form-label">Work Experience</label>
            <input type="number" class="form-control" v-model="customerData.work_exp" required>
			<div id="pincodeHelp" class="form-text text-danger">{{ validateWorkExp }}</div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';

    const customerData = defineModel({
		work_exp: ''
	})

	const validateWorkExp = computed(() => {
		if (customerData.value.work_exp < 0) {
			return "Work experience cannot be negative"
		} else if (customerData.value.work_exp > 25) {
            return "Work experience cannot be greater than 25 years"
        } else return null
	})


    const emit = defineEmits(['validationStatus'])

	watch(validateWorkExp, (newVal) => {
		emit('validationStatus', newVal === null)
	})
</script>