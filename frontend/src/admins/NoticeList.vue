<template>
  <v-container class="fill-height" fluid>
    <v-layout wrap>
      <v-flex xs12 sm8>
        <v-card>
          <v-card-title>
            {{ title }}
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="dataLIst"
            :search="search"
            sort-by="calories"
            class="elevation-1"
          >
            <template v-slot:top>
              <v-dialog v-model="dialog" max-width="500px">
                <v-card v-on:keyup.enter="save">
                  <v-card-title>
                    <span class="headline">Edit Item</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12" >
                          <v-text-field v-model="editedItem.title" label="Title"></v-text-field>
                        </v-col>
                      </v-row>  
                      <v-row>
                        <v-col cols="12">
                          <!-- <v-text-field v-model="editedItem.content" label="Content"></v-text-field> -->
                          <v-textarea rows="15" solo v-model="editedItem.content" label="Content"></v-textarea>
                        </v-col>
                      </v-row>  
                      
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                    <v-btn color="blue darken-1" text @click="save" >Save</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </template>

            <template v-slot:item.title="{ item }">
              <span> {{ title_summury(item.title) }} </span>
            </template>

            <template v-slot:item.action="{ item }">
              <v-icon small class="mr-2" color="blue darken-2" @click="editItem(item)">{{ "mdi-pencil" }}</v-icon>
              <v-icon small color="red" @click="deleteItem(item)">{{ "mdi-delete" }}</v-icon>
            </template>
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../router";
import store from "../store/modules/data.js";

export default {
  name: "NoticeList",
  props: {
    source: String
  },
  data: () => ({
    title: "Notice",
    search: "",
    dialog: false,
    headers: [
      { text: "Id", value: "id" },
      { text: "Title", value: "title" },
      // { text: "Content", value: "content" },
      { text: "Actions", value: "action", sortable: false }
    ],
    editedIndex: -1,
    editedItem: [
      {
        id: "",
        title: "",
        content: ""
      }
    ],
    dataLIst: []
  }),
  computed: {
    title_summury() {
      return (title) => {
        if (title.length > 20) {
          return title.slice(0, 20) + "...";
        } 
        return title
      };
    }
  },
  mounted() {
    this.getNotices();
  },
  methods: {
    ...mapActions("data", ["getAllUsers", "getAllNotices", "getAllBoards"]),
    getNotices() {
      this.getAllNotices().then(response => {
        this.dataLIst = response;
      });
    },
    editItem(item) {
      this.editedIndex = this.dataLIst.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item, idx) {
      const index = this.dataLIst.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.dataLIst.splice(index, 1) &&
        this.$store.dispatch("data/deleteNotice", item.id);
    },
    close() {
      this.dialog = false;
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.dataLIst[this.editedIndex], this.editedItem);
        const params = {
          id: this.editedItem.id,
          title: this.editedItem.title,
          body: this.editedItem.content
        };
        this.$store.dispatch("data/noticeUpdate", params);
      } else {
        this.dataLIst.push(this.editedItem);
      }
      this.close();
    }
  }
};
</script>

<style>
</style>