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
            class="elevation-1"
          >
            <template v-slot:top>
              <v-dialog v-model="dialog" max-width="500px">
                <v-card>
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
                          <v-textarea
                            filled
                            name="board_content"
                            label="Content"
                            auto-grow
                            v-model="editedItem.content"
                          ></v-textarea>
                        </v-col>
                      </v-row>  
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                    <v-btn color="blue darken-1" text @click="save" @keyup.enter="save">Save</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </template>

            <template v-slot:item.title="{ item }">
              <span> {{ title_summury(item.title) }} </span>
            </template>

            <template v-slot:item.action="{ item }">
              <!-- <v-icon small class="mr-2" color="blue darken-2" @click="editItem(item)">{{ "mdi-pencil" }}</v-icon> -->
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
  name: "BoardList",
  props: {
    source: String
  },
  data: () => ({
    title: "Board",
    search: "",
    dialog: false,
    headers: [
      { text: "Id", value: "id" },
      { text: "Title", value: "title" },
      { text: "Created", value: "when" },
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
    this.getBoards();
  },
  methods: {
    ...mapActions("data", ["getAllUsers", "getAllNotices", "getAllBoards"]),
    getBoards() {
      this.getAllBoards().then(response => {
        this.dataLIst = response;
      });
    },
    editItem(item) {
      this.editedIndex = this.dataLIst.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.dataLIst.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.dataLIst.splice(index, 1) &&
        this.$store.dispatch("data/deleteBoard", item.id);
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
        this.$store.dispatch("data/boardUpdate", params);
      } else {
        this.dataLIst.push(this.editedItem);
      }
      this.close();
    },
  }
};
</script>

<style>
</style>