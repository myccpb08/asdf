<template>
  <v-container class="fill-height" fluid>
    <v-layout wrap>
      <v-flex xs12 sm6>
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
                <v-card>
                  <v-card-title>
                    <span class="headline">Edit Item</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field v-model="editedItem.username" label="User name"></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field v-model="editedItem.favorite" label="Favorite"></v-text-field>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                    <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </template>
            <template v-slot:item.action="{ item }">
              <v-icon small class="mr-2" @click="editItem(item)">edit</v-icon>
              <v-icon small @click="deleteItem(item)">delete</v-icon>
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

export default {
  name: "UserList",
  props: {
    source: String
  },
  data: () => ({
    title: "User",
    search: "",
    dialog: false,
    headers: [
      {
        text: "Id",
        // align: "left",
        // sortable: false,
        value: "id"
      },
      { text: "User Name", value: "username" },
      { text: "Favorite", value: "favorite" },
      { text: "Actions", value: "action", sortable: false }
    ],
    editedIndex: -1,
    editedItem: [
      {
        id: "",
        username: "",
        favorite: "",
      }
    ],
    dataLIst: []
  }),
  computed: {
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    ...mapActions("data", ["getAllUsers", "getAllNotices", "getAllBoards"]),
    getUsers() {
      this.getAllUsers().then(response => {
        this.dataLIst = response;
      });
    },
    editItem(item) {
      console.log(item);
      this.editedIndex = this.dataLIst.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item, idx) {
      const index = this.dataLIst.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
      this.dataLIst.splice(index, 1);
    },
    close() {
      this.dialog = false;
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(
          this.dataLIst[this.editedIndex],
          this.editedItem
        );
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