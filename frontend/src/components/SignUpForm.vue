<template>
    <v-form ref="form">
        <v-text-field v-model="username" label="이름"/>
        <v-text-field v-model="email" label="ID"/>
        <v-text-field v-model="password" label="PASSWORD"/>
        <v-layout justify-center pa-10>
            <v-btn large color="indigo white--text" @click="onSubmit">Join</v-btn>
        </v-layout>
    </v-form>
</template>

<script>
export default {
    props: {
        submit: {
            type: Function,
            default: () => {}
        }
    },
    data: () => ({
        username: "",
        password: "",
        email: "",
    }),
    methods: {
        onSubmit: function() {
            const params = {
                username: this.username,
                password: this.password,
                email: this.email,
            };
            this.submit(params);
        }
    }
};
</script>