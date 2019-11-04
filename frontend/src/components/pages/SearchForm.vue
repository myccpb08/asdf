<template>
  <v-form ref="form">
    <v-text-field v-model="title" label="정책명" 
    :append-icon="icons.search" 
    @click:append="onSubmit" />
  </v-form>
</template>

<script>
import { mdiMagnify } from "@mdi/js";
import router from "../../router"

export default {
  props: {
    submit: { type: Function, default: () => {} }
  },

  data: () => ({
    title: "",
    icons: { search: mdiMagnify }
  }),

  methods: {
    onSubmit: function() {
      router.push("/policy/search/"+this.title);/* data.searchPolicy : 시행 */
    }
  }                        
};
</script>