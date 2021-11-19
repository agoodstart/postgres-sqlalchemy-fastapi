<template>
  <div class="card">
    <div class="card-body">
        <img src="../assets/generic_profile_pic.png" class="rounded" width="100">
      <Form @submit="handleRegister" :validation-schema="schema">
        <div v-if="!successful">
          <div class="form-group">
            <label for="email">Email</label>
            <Field name="email" type="email" class="form-control" />
            <ErrorMessage name="email" class="error-feedback" />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <Field name="password" type="password" class="form-control" />
            <ErrorMessage name="password" class="error-feedback" />
          </div>

          <div class="form-group">
            <button class="btn btn-primary btn-block" :disabled="loading">
              <span
                v-show="loading"
                class="spinner-border spinner-border-sm"
              ></span>
              Sign Up
            </button>
          </div>
        </div>
      </Form>

      <div
        v-if="message"
        class="alert"
        :class="successful ? 'alert-success' : 'alert-danger'"
      >
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from 'vee-validate'
import * as yup from 'yup'

export default {
    name: 'Signup',
    components: {
        Form,
        Field,
        ErrorMessage
    },
    data() {
        const schema = yup.object().shape({
            email: yup
                .string()
                .required("Email is required")
                .email("EMail is invalid")
                .max(50, "Must have a maximum of 50 characters"),
            password: yup
                .string()
                .required("Password is required!")
                .min(6, "Must be at least 6 characters")
                .max(20, "Must have a maximum of 20 characters")
        });

        return {
            successful: false,
            loading: false,
            message: "",
            schema,
        };
    },
    
}
</script>
