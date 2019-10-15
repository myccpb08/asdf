<!-- 회원가입 페이지 --> 
<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
            <!-- 회원가입 폼-->
            <v-flex xs6>
                <div>회원가입!!</div>
                <JoinForm :submit="addMember"/>
            </v-flex>
        </v-layout> 
    </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import JoinForm from "../JoinForm";
export default {
    components: {
        JoinForm
    },
    data: () => ({}),
    methods: mapActions("data", ["addMember"])
};
</script>