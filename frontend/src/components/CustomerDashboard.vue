<template>
    <div class="container mt-4">
        <h3 class="text-center display-6 my-2">{{ customer.name }}</h3>
        <div class="row">
        <div class="text-center">
            <p class="lead">
                {{ customer.email }} | 
                <span class="badge rounded-pill text-bg-info">{{ customer.pincode }}</span>
                <!-- <a href="{{ url_for('update_customer') }}" type="submit" class="btn badge text-bg-warning">Update Profile</a> -->
            </p>
        </div>
        </div>
    </div>

    <div class="container">
      <p class="lead">- Booking History</p>
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Professional Name</th>
            <th scope="col">Service Name</th>
            <th scope="col">Status</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
      
        <tbody>
          <tr v-for="request in customer.service_requests">
            <th scope="row">{{ request.request_id }}</th>
            <td>{{ request.professional_name }}</td>
            <td>{{ request.service_name }}</td>
            <td>{{ request.status }}</td>
            <td>
              <button v-if="request.status === 'REQUESTED'" class="btn btn-danger" @click="updateServiceRequest('customer', request.request_id, 'DELETED')">Delete</button>
              <!-- <button v-if="request.status === 'APPROVED'" class="btn btn-danger" @click="updateServiceRequest('customer', request.request_id, 'CLOSED')">Close</button> -->
              <div v-if="request.status === 'APPROVED'">
                <button class="btn btn-danger" @click="request.showRatingInput = true">Close</button>
                <div v-if="request.showRatingInput" class="mt-2">
                  <input v-model="request.rating" type="number" min="1" max="5" class="form-control d-inline-block w-auto" />
                  <button class="btn btn-primary ms-2" @click="closeAndRate(request.request_id, request.rating)">Submit Rating</button>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
</template>

<script setup>
    import { onMounted } from 'vue';
    import { useCustomers } from '@/composables/useCustomers';
    import { useServiceRequests } from '@/composables/useServiceRequests';

    const customer = useCustomers().current_customer

    const closeAndRate = async (service_request_id, rating) => {
      if (!rating || rating < 1 || rating > 5) {
        alert('Please provide a rating between 1 and 5.');
        return;
      }

      try {
        await useServiceRequests().rateServiceRequest(service_request_id, rating);
        await useServiceRequests().updateServiceRequestStatus('customer', service_request_id, 'CLOSED');

        const requestToUpdate = customer.value.service_requests.find(r => r.request_id === service_request_id);
        if (requestToUpdate) {
          requestToUpdate.status = 'CLOSED';
          requestToUpdate.showRatingInput = false;
          alert('Service request rated and closed successfully.');
        }
      } catch (error) {
        alert(error.message);
      }
    };

    const updateServiceRequest = async (role, service_request_id, status) => {
      try {
        await useServiceRequests().updateServiceRequestStatus(role, service_request_id, status)
        if (status === "DELETED") alert('Request deleted successfully')
        else if (status === "CLOSED") alert('Request closed successfully')

        const requestToUpdate = customer.value.service_requests.find(r => r.request_id === service_request_id) 
        if (requestToUpdate) {
          requestToUpdate.status = status;
        }
      } catch (error) {
        alert(error.message)
      }
    }

    onMounted(() => {
        useCustomers().fetchCurrentCustomer()
    })
</script>