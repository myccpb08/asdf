<template>
    <v-form ref="form">
        <v-text-field
            v-model="username"
            label="EMAIL"
            :rules="emailRules"/>
        <v-text-field
            v-model="password"
            label="PASSWORD"
            type="password"
            hint="At least 8 characters"
            :rules="[passwordRules.required, passwordRules.min]"/>
        <v-select
            v-model="favoriteValue"
            :items="favoriteList"
            attach
            chips
            label="FAVORITE"
            multiple
        ></v-select>
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
        favoriteValue: ['01', '02', '03', '04', '05', ' 06', 
                        '07', '08', '09', '10', '11', '12', 
                        '13', '14', '15', '16'],
        favoriteList: ['임신/출산', '영유아', '아동/청소년', '청년', '중장년', '노년', 
                        '장애인', '한부모', '다문화(새터민)', '저소득층', '교육', '고용', 
                        '주거', '건강', '서민금융', '문화'],
        emailRules: [ 
            v => !!v || "ID is Required!",
            v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
        ], 
        passwordRules: {
            required: value => !!value || "Password is Required",
            min: v => v.length >= 8 || "Min 8 characters"
        },

    }),
    methods: {
        onSubmit: function() {
            const params = {
                username: this.username,
                password: this.password,
            };
            this.submit(params);

            router.push("/user/list")
        }
    }
};
</script>