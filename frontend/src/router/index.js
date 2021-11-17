import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },
  {
    path: '/employees',
    name: 'Employees Page',
    component: () => import(/* webpackChunkName: "about" */ '../views/employees/EmployeesPage.vue'),
    children: [
      {
        path: '',
        name: 'Employee List',
        component: () => import(/* webpackChunkName: "about" */ '../views/employees/EmployeesList.vue'),
      },
      {
        path: '/employees/:id',
        name: 'Single Employee',
        component: () => import(/* webpackChunkName: "about" */ '../views/employees/SingleEmployee.vue')
      },
    ]
  },
  {
    path: '/countries',
    name: 'Countries',
    component: () => import(/* webpackChunkName: "about" */ '../views/Countries.vue')
  },
  {
    path: '/regions',
    name: 'Regions',
    component: () => import(/* webpackChunkName: "about" */ '../views/Regions.vue')
  },
  {
    path: '/locations',
    name: 'Locations',
    component: () => import(/* webpackChunkName: "about" */ '../views/Locations.vue')
  },
  {
    path: '/departments',
    name: 'Departments',
    component: () => import(/* webpackChunkName: "about" */ '../views/Departments.vue')
  },
  {
    path: '/jobs',
    name: 'Jobs',
    component: () => import(/* webpackChunkName: "about" */ '../views/Jobs.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
