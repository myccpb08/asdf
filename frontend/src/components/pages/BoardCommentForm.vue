<template>
  <v-layout wrap>
    <v-flex pa-1>
      <form>
        <v-text-field v-model="content" placeholder="내용을 입력해주세요" @keypress.enter.prevent="onSubmit"></v-text-field>
      </form>
    </v-flex>
    <v-btn rounded color="primary" dark @click="onSubmit" >작성</v-btn>
  </v-layout>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    },
    Id: {}
  },

  data: () => ({
    content: "",
    pageIndex: 0,
    preUrl: ""
  }),

  mounted() {},

  methods: {
    onSubmit: function() {
      const params = {
        content: this.content,
        boardId: this.Id,
        writer: this.$store.state.data.user
      };
      this.submit(params);
      this.content=''
      this.$emit('reload')

      // window.location.reload()
    },
  }
};
</script>