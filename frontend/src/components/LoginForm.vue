<template>
    <v-form ref="form">
        <v-text-field v-model="username" label="ID"/>
        <v-text-field v-model="password" label="PASSWORD"/>
        <v-layout justify-center pa-10>
            <v-btn large color="indigo white--text" @click="onSubmit">로그인</v-btn>
            <router-link to="/signup">
                <v-btn large color="indigo white--text">회원가입</v-btn>
            </router-link>
        </v-layout>
    </v-form>
</template>

<script>
import router from "../router"
import store from "../store";

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
    }),
    beforemount() {
        if(store.state.user=='undefined' || store.state.user==null){
            router.push('/')
        }
    },
    methods: {
        onSubmit: function() {
            const params = {
                username: this.username,
                password: this.password,
            };
            this.submit(params).then(data => {
                console.log("data" + data)
            });
        },
    }
};
</script>