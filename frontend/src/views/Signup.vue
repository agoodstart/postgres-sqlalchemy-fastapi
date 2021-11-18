<template>

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
