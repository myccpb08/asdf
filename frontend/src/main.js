import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import { mapState, mapActions } from "vuex";

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),
  created() {
    console.log("Create!!!!!!!!!!")
    if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
      var result = this.getSession(localStorage.getItem("token"));
      console.log("result")
      if (result == false) {
        //토큰이 잘못된 값일 때
        router.push("/");
      }
    } else {
      //토큰 없을 때
      router.push("/");
    }
  },
  methods: mapActions("data", ["getSession"])
}).$mount('#app')
