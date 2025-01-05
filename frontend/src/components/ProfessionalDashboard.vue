<template>
    <div class="container mt-4">
        <h3 class="text-center display-6 my-2">{{ professional.name }}</h3>
        <div class="row">
        <div class="text-center">
            <p class="lead">
                {{ professional.email }} |
                <span class="badge rounded-pill text-bg-info">{{ professional.rating }}</span>
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
            <th scope="col">Customer Name</th>
            <th scope="col">Status</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
      
        <tbody>
          <tr v-for="request in professional.service_requests">
            <th scope="row">{{ request.request_id }}</th>
            <td>{{ request.customer_name }}</td>
            <td>{{ request.status }}</td>
            <td>
              <button v-if="request.status === 'REQUESTED'" class="btn btn-info me-2" @click="updateServiceRequest(request.request_id, 'APPROVED')">Approve</button>
              <button v-if="request.status === 'REQUESTED'" class="btn btn-danger" @click="updateServiceRequest(request.request_id, 'REJECTED')">Reject</button>
              <p v-else>No further actions available</p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
</template>

<script setup>
    import { onMounted } from 'vue';
    import { useProfessionals } from '@/composables/useProfessionals';
    import { useServiceRequests } from '@/composables/useServiceRequests';

    const professional = useProfessionals().current_professional


    const updateServiceRequest = async (service_request_id, status) => {
      try {
        await useServiceRequests().updateServiceRequestStatus('professional', service_request_id, status)
        if (status === "APPROVED") alert('Request approved successfully')
        else if (status === "REJECTED") alert('Request rejected successfully')
        const requestToUpdate = professional.value.service_requests.find(r => r.request_id === service_request_id) 
        if (requestToUpdate) {
          requestToUpdate.status = status;
        }
      } catch (error) {
        alert(error.message)
      }
    }

    onMounted(() => {
      useProfessionals().fetchCurrentProfessional()
    })
</script>