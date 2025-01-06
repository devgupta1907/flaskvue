

const createServiceRequest = async (service_id, professional_id) => {
    try {
        const response = await fetch('http://localhost:5000/api/service_request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authentication-Token': localStorage.getItem('token')
            },
            body: JSON.stringify({ 
                service_id: service_id, 
                professional_id: professional_id
            })
        });
  
        const data = await response.json()
        if (!response.ok) {
            throw new Error(data.message);
        }
    } catch (error) {
        console.log("ERROR", error.message)
        throw error
    }
}

const updateServiceRequestStatus = async (role, serviceRequestId, status) => {
    try {
      const response = await fetch(`http://localhost:5000/api/${role}/service_request`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authentication-Token': localStorage.getItem('token')
        },
        body: JSON.stringify({ id: serviceRequestId, status: status })
      })
      
      const data = await response.json();
        if (!response.ok) {
            throw new Error(data.message);
        }
    } catch (error) {
      console.log("ERROR", error.message)
      throw error
    }
  }

  const rateServiceRequest = async (serviceRequestId, rating) => {
    try {
      const response = await fetch(`http://localhost:5000/api/customer/service_request/rate`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authentication-Token': localStorage.getItem('token')
        },
        body: JSON.stringify({ id: serviceRequestId, rating: rating })
      })
      
      const data = await response.json();
        if (!response.ok) {
            throw new Error(data.message);
        }
    } catch (error) {
      console.log("ERROR", error.message)
      throw error
    }
  }

export function useServiceRequests() {
    return {
        createServiceRequest,
        updateServiceRequestStatus,
        rateServiceRequest
    }
}