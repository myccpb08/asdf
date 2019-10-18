<template>
    <v-form ref="form">
        <v-text-field v-model="username" label="이름"/>
        <v-text-field v-model="email" label="ID"/>
        <v-text-field v-model="password" label="PASSWORD"/>
        <v-text-field v-model="gender" label="GENDER"/>
        <v-text-field v-model="location" label="LOCATION"/>
        <v-text-field v-model="marriage" label="MARRIAGE"/>
        <v-text-field v-model="job" label="JOB"/>
        <v-text-field v-model="disability" label="DISABILITY"/>
        <v-text-field v-model="familysize" label="FAMILYSIZE"/>
        <v-text-field v-model="insurance" label="INSURANCE"/>
        <v-text-field v-model="incomequintile" label="INCOMEQUINTILE"/>
        <v-layout justify-center pa-10>
            <v-btn large color="indigo white--text" @click="onSubmit">Join</v-btn>
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
        username: "",
        password: "",
        email: "",
        gender: "",
        location: "",
        marriage: "",
        job: "",
        disability: "",
        familysize: "",
        insurance: "",
        incomequintile: "",
    }),
    methods: {
        onSubmit: function() {
            const params = {
                username: this.username,
                email: this.email,
                password: this.password,
                gender: this.gender,
                location: this.location,
                marriage: this.marriage,
                job: this.job,
                disability: this.disability,
                familysize: this.familysize,
                insurance: this.insurance,
                incomequintile: this.incomequintile,
            };
            this.submit(params);

            router.push("/user/list")
        }
    }
};
</script>