import { ref } from 'vue';


const services = ref([]);

const fetchServices = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/services');

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.message);
    }
    services.value = data;
  } catch (error) {
    console.error("ERROR", error.message);
  }
};

const addService = async (serviceName, servicePrice, serviceDescription, serviceCategory) => {
  try {
      const response = await fetch('http://localhost:5000/api/services', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': localStorage.getItem('token')
          },
          body: JSON.stringify({ 
            name: serviceName, 
            price: servicePrice,
            description: serviceDescription,
            category_id: serviceCategory 
          })
      });

      const data = await response.json()
      if (!response.ok) {
          throw new Error(data.message);
      }
      services.value.push(data)
  } catch (error) {
      console.log("ERROR", error.message)
      throw error
  }
}

const updateService = async (serviceId, serviceName, servicePrice, serviceDescription, serviceCategory) => {
  try {
      const response = await fetch(`http://localhost:5000/api/services`, {
          method: 'PUT',
          headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': localStorage.getItem('token')
          },
          body: JSON.stringify({ 
            existingServiceId: serviceId, 
            name: serviceName, 
            price: servicePrice,
            description: serviceDescription,
            category_id: serviceCategory
          })
      });

      const data = await response.json();
      if (!response.ok) {
          throw new Error(data.message);
      }

      const index = services.value.findIndex(ser => ser.id === serviceId);
      if (index !== -1) {
          services.value[index] = data;
      }
  } catch (error) {
      console.log("ERROR", error.message);
      throw error
  }
};

const deleteService = async (serviceId) => {
  try {
    const response = await fetch(`http://localhost:5000/api/services`, {
      method: 'DELETE',
      headers: {
          'Content-Type': 'application/json',
          'Authentication-Token': localStorage.getItem('token')
      },
      body: JSON.stringify({ id: serviceId })
    })
    
    const data = await response.json();
      if (!response.ok) {
          throw new Error(data.message);
      }
    
    services.value = services.value.filter(ser => ser.id !== parseInt(serviceId))
  } catch (error) {
    console.log("ERROR", error.message)
    throw error
  }
}


export function useServices() {
  return {
    services,
    fetchServices,
    addService,
    updateService,
    deleteService
  };
}
