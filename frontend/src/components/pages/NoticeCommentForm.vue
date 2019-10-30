<template>
  <v-layout wrap>
    <v-flex pa-1>
      <form>
        <v-text-field v-model="content" placeholder="내용을 입력해주세요"></v-text-field>
      </form>
    </v-flex>

    <v-btn rounded color="primary" dark @click="onSubmit">테스트작성</v-btn>
    <!-- <v-flex shrink pa-1>
      <v-btn
        style="padding-top:5px;"
        small
        outlined
        rounded
        flat
        color="gray"
        v-on:click="postComment(mentor, content)"
        class="movebtn"
      >submit</v-btn>
    </v-flex> -->
  </v-layout>
</template>

<script>
import router from "../../router/index.js";

export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    },
    Id: {
      // type: String,
    }
  },

  data: () => ({
    content:''
  }),

    mounted() {
    },

  methods: {
    onSubmit: function() {
      const params = {
        content : this.content,
        noticeId : this.Id
      };
      console.log(params);
      this.submit(params);
      window.location.reload()
    }
  }
};
</script>