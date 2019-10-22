<!-- 회원리스트 페이지 --> 
<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
            <!-- 회원가입 폼-->
            <v-flex xs6>
                <div>회원리스트!!</div>
                <UserList :getAllUsers="getAllUsers"/>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserList from "../UserListForm";
import router from "../../router";


export default {
    components: {
        UserList,
    },
    methods: {
        ...mapActions("data", [
        "getAllUsers"
        ])
    }

}
</script>