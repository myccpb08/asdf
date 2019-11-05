<template>
    <v-form class="editForm" ref="form">
        <v-text-field v-model="name" :label='this.$store.state.data.user.name' type="name" :rules="[nameRules.required]"/>
        <!-- <v-text-field v-model="password" label="PASSWORD" type="password" :rules="[passwordRules.required, passwordRules.min]"/> -->
        <v-select
            v-model="this.userSeleted"
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
            <v-btn large color="green white--text" @click="onSubmit">수정</v-btn>
            <v-btn large color="red white--text" @click="deleteUser">회원탈퇴</v-btn>
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
    mounted() {
        this.setFavorite()
    },
    data: () => ({
        userSeleted: [],
        selected: "",
        name: "",
        password: "",
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
        nameRules: {
            required: value => !!value || "Name is Required",
        },
        passwordRules: {
            required: value => !!value || "Password is Required",
            min: v => v.length >= 8 || "Min 8 characters"
        },
    }),
    methods: {
        onSubmit() {
            const params = {
                username: this.$store.state.data.user.username,
                name: this.name,
                // password: this.password,
                favoriteValue: this.selected,
            }
            this.submit(params)
            window.location.replace("/")
        },
        setFavorite() {
            var userFavorite = this.$store.state.data.user.favorite
            if(userFavorite!=null){
                for(var f in userFavorite){
                    if(f=='00'){
                        break
                    }else{
                        this.userSeleted.push(this.items[f*1-1])
                    }
                }
            }
        },
        setSelected(value) {
            this.selected = value
        },
        async deleteUser() {
            if(confirm("탈퇴하겠습니까?")){
                await this.$store.dispatch('data/deleteUser')
                localStorage.removeItem('token')
                window.location.replace("/")
            }
        }
    }
}
</script>

<style>
    .editForm {
        width: 70%;

    }
</style>
