import { ref } from 'vue';

// Shared state
const professionals = ref([]);


const fetchProfessionals = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/professionals', {
      method: "GET",
      headers: {
        "Authentication-Token": localStorage.getItem('token')
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }
    const data = await response.json();
    professionals.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};


const fetchProfessionalsByService = async (service_id) => {
  try {
    const response = await fetch(`http://localhost:5000/api/services/${service_id}/service_professionals`, {
      method: "GET",
      headers: {
        "Authentication-Token": localStorage.getItem('token'),
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }
    const data = await response.json();
    professionals.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};

export function useProfessionals() {
  return {
    professionals,
    fetchProfessionals,
    fetchProfessionalsByService
  };
}
