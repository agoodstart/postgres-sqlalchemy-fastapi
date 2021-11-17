<template>
  <section class="employee-list container">
    <div class="input-group">
      <input type="text" v-model="search" class="form-control" aria-label="Text input" placeholder="Filter employee by name" />
      <select v-model="select" class="form-select" id="inputGroupSelect01">
        <option value="full_name">Full Name</option>
        <option value="job_title">Job Title</option>
      </select>
    </div>
  <div class="results">
    <div class="row">
      <div v-for="employee in employees" :key="employee.employee_id" class="col-sm-4">
      <a href="#" class="card btn btn-light">
        <div class="card-body">
          <h5 class="card-title">
            {{ employee.full_name }}
          </h5>
          <p class="card-text">{{employee.job_title}}</p>
        </div>
      </a>
    </div>
    </div>
  </div>
  </section>
</template>

<style scoped>
.results {
  margin-top: 3rem;
  height: 500px;
}

.card {
  flex-direction: row;
}

.row {
  --bs-gutter-y: 1.5rem;
}
</style>

<script>
import axios from 'axios'
// import {ref} from 'vue'


export default {
  name: 'Test',
  data() {
    return {
      employees: [],
      search: '',
      select: 'full_name'
    };
  },
  watch: {
    search: function(value) {
      console.log(this.select);
      this.doSearch(value)
    },
    select: function(value) {
      console.log(value)
    }
  },
  methods: {
    getList() {
      axios.get('employees/')
        .then((res) => {
          this.employees = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    doSearch(value) {
      axios.get(`employees/search/?query=${value}`)
        .then(response => {
          this.employees = response.data;
      })
    }
  },
  created() {
    this.getList();
  },
}
</script>

