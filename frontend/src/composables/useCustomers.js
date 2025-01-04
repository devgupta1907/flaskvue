import { ref } from 'vue';

// Shared state
const customers = ref([]);


const fetchCustomers = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/customers', {
      method: "GET",
      headers: {
        "Authentication-Token": localStorage.getItem('token')
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }
    const data = await response.json();
    customers.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};

export function useCustomers() {
  return {
    customers,
    fetchCustomers,
  };
}
