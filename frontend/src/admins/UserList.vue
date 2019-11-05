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
                <v-card>
                  <v-card-title>
                    <span class="headline">Edit Item</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container fluid>
                      <!-- <v-layout >
                        <v-flex xs12>
                          <v-text-field v-model="editedItem.username" color="info" label="User name"></v-text-field>
                        </v-flex>
                      </v-layout>-->

                      <v-layout>
                        <v-flex xs12>
                          <v-select
                            :items="gradeItem"
                            v-model="editedItem.is_staff"
                            :label="editedItem.is_staff"
                            single-line
                            item-value="text"
                          ></v-select>
                        </v-flex>
                      </v-layout>
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
            <template v-slot:item.action="{ item }">
              <v-icon
                small
                class="mr-2"
                color="blue darken-2"
                @click="editItem(item)"
              >{{ "mdi-pencil" }}</v-icon>
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
        align: "left",
        sortable: false,
        value: "id"
      },
      { text: "User Name", align: "left", value: "username" },
      { text: "Favorite", align: "left", sortable: false, value: "favorite" },
      { text: "Grade", value: "is_staff" },
      { text: "Created", value: "when" },
      { text: "Actions", value: "action", sortable: false }
    ],
    editedIndex: -1,
    editedItem: [
      {
        id: "",
        username: "",
        favorite: "",
        is_staff: ""
      }
    ],
    gradeItem: [{ text: "staff" }, { text: "user" }],
    dataLIst: []
  }),
  computed: {},
  mounted() {
    this.getUsers();
  },
  methods: {
    ...mapActions("data", ["getAllUsers", "getAllNotices", "getAllBoards"]),
    getUsers() {
      this.getAllUsers().then(response => {
        this.dataLIst = response;
        console.log(this.dataLIst);
      });
    },
    editItem(item) {
      this.editedIndex = this.dataLIst.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item, idx) {
      if (item.is_staff != "staff") {
        const params = {
          username: item.username
        };
        this.$store.dispatch("data/deleteUser", params).then(response => {
          const index = this.dataLIst.indexOf(item);
          confirm("Are you sure you want to delete this item?") &&
            this.dataLIst.splice(index, 1);
        });
      } else {
        alert("관리자는 삭제할 수 없습니다.");
      }
      // TODO: 위 라인과 &&로 연결해서 유저 삭제
    },
    close() {
      this.dialog = false;
    },

    save() {
      if (this.editedItem.username != "admin") {
        const params = {
          username: this.editedItem.username,
          name: this.editedItem.name,
          password: this.editedItem.password,
          favoriteValue: this.editedItem.favorite,
          grade: this.editedItem.is_staff
        };
        this.$store.dispatch("data/editUser", params).then(response => {
          if (this.editedIndex > -1) {
            Object.assign(this.dataLIst[this.editedIndex], this.editedItem);
          } else {
            this.dataLIst.push(this.editedItem);
          }
          this.close();
        });
      } else {
        alert("해당 계정의 권한은 변경할 수 없습니다.");
        this.close();
      }
    }
  }
};
</script>

<style>
</style>