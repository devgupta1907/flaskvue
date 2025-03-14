import { ref } from 'vue';

const professionals = ref([]);
const professionalsByService = ref([])
const current_professional = ref([])


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
    professionalsByService.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};

const fetchCurrentProfessional = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/professionals/current_professional', {
      method: "GET",
      headers: {
        "Authentication-Token": localStorage.getItem('token')
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }
    const data = await response.json();
    current_professional.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};

export function useProfessionals() {
  return {
    professionals,
    fetchProfessionals,
    fetchProfessionalsByService,
    current_professional,
    professionalsByService,
    fetchCurrentProfessional,

  };
}
