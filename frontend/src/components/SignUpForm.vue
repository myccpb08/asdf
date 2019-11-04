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
        <v-text-field
            v-model="name"
            label="NAME"/>
        <v-select
            v-model="items.value"
            :items="items"
            :menu-props="{ top: true, offsetY: true }"
            attach
            chips
            outlined
            label="FAVORITE"
            multiple
            @input="setSelected"
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
        name: "",
        selected: "",
        items: [
            {text: '임신/출산', value: '01'},
            {text: '영유아', value: '02'},
            {text: '아동/청소년', value: '03'},
            {text: '청년', value: '04'},
            {text: '중장년', value: '05'},
            {text: '노년', value: '06'},
            {text: '장애인', value: '07'},
            {text: '한부모', value: '08'},
            {text: '다문화(새터민)', value: '09'},
            {text: '저소득층', value: '10'},
            {text: '교육', value: '11'},
            {text: '고용', value: '12'},
            {text: '주거', value: '13'},
            {text: '건강', value: '14'},
            {text: '서민금융', value: '15'},
            {text: '문화', value: '16'}
        ],
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
            console.log("selected : " + this.selected)
            const params = {
                username: this.username,
                password: this.password,
                name: this.name,
                favoriteValue: this.selected,
            };
            this.submit(params);

            router.push("/login")
        },
        setSelected(value) {
            this.selected = value
        }
    }
};
</script>