import { ref } from 'vue';

const customers = ref([]);
const current_customer = ref([])


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


const fetchCurrentCustomer = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/customers/current_customer', {
      method: "GET",
      headers: {
        "Authentication-Token": localStorage.getItem('token')
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }
    const data = await response.json();
    current_customer.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};

export function useCustomers() {
  return {
    customers,
    fetchCustomers,
    current_customer,
    fetchCurrentCustomer
  };
}
