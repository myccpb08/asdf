<template>
    <p>{{latestView}}</p>
</template>

<script>
import { mapActions } from "vuex";
import store from "../store/modules/data.js";

export default {
    data: () => ({
        latestView: "",
    }),
    created() {
        console.log("SearchList!!!!!!!!!!")
        // localStorage.removeItem('token')
        if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
            var result = this.getSession(localStorage.getItem('token')).then(function(value){
                console.log(value)
                console.log(store.state.user)
                console.log(store.state.user.username)
                this.latestView = store.user.lastestView
                if(value==false){
                    router.push('/')
                }
            });
        }else{
            router.push("/");
        }
    },
    methods: {
        ...mapActions("data", ["getSession"]),
    }
}
</script>

<style>
    .editForm {
        width: 70%;

    }
</style>
