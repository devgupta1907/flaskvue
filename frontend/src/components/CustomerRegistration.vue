<template>
    <div>
        <div class="mb-3">
            <label for="pincode" class="form-label">Pincode</label>
            <input type="number" class="form-control" v-model="customerData.pincode" required>
			<div id="pincodeHelp" class="form-text text-danger">{{ validatePincode }}</div>
        </div>
    </div>
</template>

<script setup>
	import { computed, watch } from 'vue';

    const customerData = defineModel({
		pincode: ''
	})

	const validatePincode = computed(() => {
		if (customerData.value.pincode < 100000 || customerData.value.pincode > 999999) {
			return "Please enter a valid pincode"
		} else return null
	})

	const emit = defineEmits(['validationStatus'])

	watch(validatePincode, (newVal) => {
		emit('validationStatus', newVal === null)
	})
</script>