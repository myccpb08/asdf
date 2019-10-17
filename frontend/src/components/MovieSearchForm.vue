<template>
  <v-form ref="form" class="search_form_div">
    <v-text-field 
      v-model="title" 
      append-icon="mdi-magnify"
      label="여기는 app.vue"
      @click:append="onSubmit">
    </v-text-field>
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
  data: () => ({
    title: ""
  }),
  methods: {
    onSubmit: function() {
      const params = {
        title: this.title,
      };
      this.submit(params);
    }
  }
};
</script>
<style>
.search_form_div{
  width: 80%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>