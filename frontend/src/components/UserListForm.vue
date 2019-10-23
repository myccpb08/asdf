<template>
    <v-container class="pa-2" fluid grid-list-md>
        <v-layout>
            <v-flex :loading="loading">
                <div v-for="user in userList">
                    {{user}}
                </div>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import store from '../store/modules/data.js'

export default {
    props: {
      getAllUsers: {
          type: Function,
          default: ()=>{}
      }  
    },
    data: () => ({
        loading: false,
        userList: [],
    }),
    async mounted(){
        await this.getList()
    },
    methods: {
        setLoading() {
            if(this.loading){
                this.loading = false
            }else{
                this.loading = true
            }
        },
        async getList() {
            await this.setLoading()
            this.userList = await this.getAllUsers()
            await this.setLoading()
        }
    }
}
</script>