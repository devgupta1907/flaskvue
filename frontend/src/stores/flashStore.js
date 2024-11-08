import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useFlashStore = defineStore('flash', () => {
  const flashMessage = ref("");
  const flashMessageType = ref("");
  const showFlash = ref(false);

  const showFlashMessage = (message, type) => {
    flashMessage.value = message;
    flashMessageType.value = type;
    showFlash.value = true;
  };

  const handleFlashClose = () => {
    showFlash.value = false;
  };

  return {
    flashMessage,
    flashMessageType,
    showFlash,
    showFlashMessage,
    handleFlashClose
  };
});
