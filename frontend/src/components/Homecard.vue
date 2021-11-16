<template>
    <div class="card text-center">
        <div class="card-header">
            Random employee
        </div>
        <!-- <img class="card-img-top" alt="Pic"> -->
        <div class="card-body">
            <div class="py-2 p-2">
                <div class="mt-3 d-flex flex-row justify-content-center">
                    <h5 class="card-title">{{ employee.first_name + " " + employee.last_name }}</h5>
                </div>
                 <p class="card-text">{{ employee.job_title }}</p>
            </div>
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item flex-fill d-flex justify-content-center align-items-center">
                <div>
                    <div class="fw-bold">Current manager</div>
                    {{ employee.manager_full_name }}
                </div>
            </li>
            <li class="list-group-item flex-fill d-flex justify-content-center align-items-center">
                <div>
                    <div class="fw-bold">Department</div>
                    {{ employee.department_name }}
                </div>
            </li>
                        <li class="list-group-item d-flex justify-content-center align-items-center">
                <div>
                    <div class="fw-bold">Current Location</div>
                    {{ employee.current_location }}
                </div>
            </li>
            <li class="list-group-item d-flex flex-fill justify-content-center align-items-center">
                <div>
                    <div class="fw-bold">Salary</div>
                    {{ employee.ceiled_salary }}
                </div>
            </li>
            <li class="list-group-item d-flex flex-fill justify-content-center align-items-center">
                <div>
                    <div class="fw-bold">Salary Count</div>
                    {{ employee.salary_count }}
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Test',
  data() {
    return {
      employee: {},
    };
  },
  methods: {
    getList() {
      axios.get('/')
        .then((res) => {
          this.employee = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getList();
  },
}
</script>