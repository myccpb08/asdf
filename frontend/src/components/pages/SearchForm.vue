<template>
  <v-form ref="form">
    <v-text-field v-model="title" label="정책명" 
    :append-icon="icons.search" 
    @click:append="onSubmit" />
  </v-form>
</template>

<script>
import { mdiMagnify } from "@mdi/js";

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
      const params = {
        title: this.title
      };
      this.submit(params); /* data.searchPolicy : 시행 */
    }
  }
};
</script>