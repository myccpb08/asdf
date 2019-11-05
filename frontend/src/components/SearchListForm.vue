<template>
    <v-container class="pa-2" fluid grid-list-md>
        <div v-for="p in policy">
            <p class="latestView" @click="goService(p.id)">{{p.title}}</p>
        </div>
    </v-container>
</template>

<script>
import { mapActions } from "vuex";

export default {
    data: () => ({
        result: null,
        latestView: null,
        policy: [],
    }),
    created() {
        console.log("SearchList!!!!!!!!!!")
        // localStorage.removeItem('token')
        // if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
        //     var result = this.getSession(localStorage.getItem('token')).then(function(value){
        //         this.setList(store.state.user.lastestView)
        //     });
        // }
    },
    mounted() {
        this.getLatestViewList()
    },
    methods: {
        ...mapActions("data", ["getSession"]),
        async getLatestViewList() {
           this.result = await this.$store.dispatch('data/getLatestView')
           this.latestView = this.result.data.latestViewList
           console.log(this.latestView)
           this.savePolicyInfo()
        },
        savePolicyInfo() {
            for(var lv in this.latestView){
                console.log(this.latestView[lv])
                this.getPolicyInfo(this.latestView[lv]).then(result => {
                    this.policy.push(result)
                    console.log(this.policy)
                })
            }
        },
        async getPolicyInfo(policyId) {
            return this.$store.dispatch(
                "data/getService",
                policyId
            )
        },
        goService(id){
            this.$router.push('/detailPolicy/'+id)
        }
    }
}
</script>

<style>
    .editForm {
        width: 70%;

    }
    .latestView {
        cursor: pointer;
    }
</style>
