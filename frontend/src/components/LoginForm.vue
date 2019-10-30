<template>
    <v-form ref="form">
        <v-text-field v-model="username" label="ID"/>
        <v-text-field v-model="password" label="PASSWORD" type="password" @keyup.enter="onSubmit"/>
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
    created() {
        if(localStorage.getItem('token')!==null){
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
                if(data){
                    window.location.replace('/')
                }else{
                    alert('ID 또는 Password가 맞지 않습니다.')
                    window.location.reload()
                }
            });
        },
    }
};
</script>