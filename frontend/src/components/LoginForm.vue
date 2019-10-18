<template>
    <v-form ref="form">
        <v-text-field v-model="email" label="ID"/>
        <v-text-field v-model="password" label="PASSWORD"/>
        <v-layout justify-center pa-10>
            <v-btn large color="indigo white--text" @click="onSubmit">Login</v-btn>
        </v-layout>
    </v-form>
</template>

<script>
import router from "../router"
export default {
    props: {
        submit: {
            type: Function,
            default: () => {}
        }
    },
    data: () => ({
        email: "",
        password: "",
    }),
    methods: {
        onSubmit: function() {
            const params = {
                email: this.email,
                password: this.password,
            };
            this.submit(params);

            router.push("/login")
        }
    }
};
</script>