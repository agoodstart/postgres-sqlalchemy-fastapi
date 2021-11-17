<template>
  <section id="single-employee">
    <div class="container height-100 d-flex justify-content-center align-items-center">
    <div class="card text-center">
        <div class="py-4 p-2">
            <div> <img src="../../assets/generic_profile_pic.png" class="rounded" width="100"> </div>
            <div class="mt-3 d-flex flex-column justify-content-center">
                <h5>{{employee.first_name + " " + employee.last_name}} <br>
                  <span style="font-size: 1rem;">{{employee.job_title}}</span>
                </h5>
            </div>
            <span>Hired {{employee.hire_date}}</span><br>
            <span>{{employee.current_location}}</span>
            <div class="mt-3">
              <a class="btn btn-outline-secondary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
                View contact info
              </a>
            </div>
            <div class="collapse" id="collapseExample">
                  <div class="card card-body">
                    <div class="row">
                      <div class="col-md-4">
                          <p>Tel nr</p>
                          <p>Email</p>
                      </div>
                      <div class="col-md-8">
                        <p>{{employee.phone_number}}</p>
                        <p>{{employee.email}}</p>
                      </div>
                    </div>
                    
            </div>
            </div>
        </div>
        <div>
            <ul class="list-unstyled list">
                <li> <span class="font-weight-bold">Department</span>
                    <div> <span class="mr-1">{{employee.department_name}}</span> <i class="fa fa-angle-right"></i> </div>
                </li>
                <li> <span class="font-weight-bold">Reports to</span>
                    <div> <span class="mr-1">{{employee.manager_full_name}}</span> <i class="fa fa-angle-right"></i> </div>
                </li>
                <li> <span class="font-weight-bold">Salary</span>
                    <div> <span class="mr-1">{{employee.ceiled_salary}}</span> <i class="fa fa-angle-right"></i> </div>
                </li>
            </ul>
        </div>
    </div>
</div>
  </section>
</template>

<style scoped>
body {
    background-color: #eee
}

#collapseExample .row .col-md-4:first-child p {
  text-align: left;
}

#collapseExample .row .col-md-8:last-child p {
  text-align: right;
}

.height-100 {
    height: 100vh
}

.card {
    width: 380px;
    border: none
}

.dots {
    height: 20px;
    width: 20px;
    margin-top: 4px;
    margin-left: 4px;
    background-color: #dc3545;
    border-radius: 50%;
    border: 2px solid #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 10px
}

.list li {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 13px;
    border-top: 1px solid #eee;
    cursor: pointer
}

.list li:hover {
    background-color: #dc3545;
    color: #fff
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'Single Employee',
  data() {
    return {
        employee: {},
        route: this.$route.params.id
    };
  },
  methods: {
    getEmployee() {
      axios.get(`employees/${this.route}`)
        .then((res) => {
          this.employee = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getEmployee();
  },
}
</script>
