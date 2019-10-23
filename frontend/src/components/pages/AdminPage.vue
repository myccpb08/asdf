<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item @click="getDash">
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="getChart">
          <v-list-item-action>
            <v-icon>mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <p>{{ admin_selected }}</p>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left scroll-target="#scrolling-techniques-5">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="width: 200px" class="ml-0 pl-4">
        <span class="hidden-sm-and-down">DJE Admin</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-search"
        label="Search"
        v-model="search_text"
        v-on:keyup.enter="getSearchResult"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn icon>
        <i class="fas fa-home fa-2x"></i>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-bell</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <v-container v-if="admin_selected == 0" class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col class="shrink">
            <v-tooltip right>
              <template v-slot:activator="{ on }">
                <v-btn :href="source" icon large target="_blank" v-on="on">
                  <v-icon large>mdi-code-tags</v-icon>
                </v-btn>
              </template>
              <span>Source</span>
            </v-tooltip>
            <v-tooltip right>
              <template v-slot:activator="{ on }">
                <v-btn
                  icon
                  large
                  href="https://codepen.io/johnjleider/pen/bXNzZL"
                  target="_blank"
                  v-on="on"
                >
                  <v-icon large>mdi-codepen</v-icon>
                </v-btn>
              </template>
              <span>Codepen</span>
            </v-tooltip>
          </v-col>
        </v-row>
      </v-container>

      <v-container v-else class="fill-height" fluid>
        <v-layout wrap>
          <v-flex xs12 sm6>
            <v-card>
              <v-tabs v-model="tab" background-color="transparent">
                <v-tab v-for="item in items" :key="item">{{ item }}</v-tab>
              </v-tabs>
              <v-tabs-items v-model="tab">
                <v-card>
                  <v-card-title>
                    {{ items[tab] }}
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
                    :headers="headers[tab]"
                    :items="dashBoardAllData[tab]"
                    :search="search"
                    sort-by="calories"
                    class="elevation-1"
                  >
                    <template v-slot:top>
                      <!-- <v-toolbar flat color="white"> -->
                      <!-- <v-toolbar-title>My CRUD</v-toolbar-title> -->
                      <!-- <v-divider class="mx-4" inset vertical></v-divider>
                      <v-spacer></v-spacer>-->
                      <v-dialog v-model="dialog" max-width="500px">
                        <!-- <template v-slot:activator="{ on }">
                        <v-btn color="primary" dark class="mb-2" v-on="on">New Item</v-btn>
                        </template>-->
                        <v-card>
                          <v-card-title>
                            <span class="headline">{{ formTitle }}</span>
                          </v-card-title>

                          <v-card-text>
                            <v-container>
                              <v-row>
                                <v-col cols="12" sm="6" md="4">
                                  <v-text-field v-model="editedItem[tab].title" :label="text"></v-text-field>
                                </v-col>
                                <!-- <v-col cols="12" sm="6" md="4">
                                  <v-text-field v-model="editedItem.name" :label="text"></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="4">
                                  <v-text-field v-model="editedItem.calories" label="Calories"></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="4">
                                  <v-text-field v-model="editedItem.fat" label="Fat (g)"></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="4">
                                  <v-text-field v-model="editedItem.carbs" label="Carbs (g)"></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="4">
                                  <v-text-field v-model="editedItem.protein" label="Protein (g)"></v-text-field>
                                </v-col> -->
                              </v-row>
                            </v-container>
                          </v-card-text>

                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                            <v-btn color="blue darken-1" text @click="save(tab)">Save</v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                      <!-- </v-toolbar> -->
                    </template>
                    <template v-slot:item.action="{ item }">
                      <v-icon small class="mr-2" @click="editItem(item, tab)">edit</v-icon>
                      <v-icon small @click="deleteItem(item, tab)">delete</v-icon>
                    </template>
                  </v-data-table>
                </v-card>
              </v-tabs-items>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserList from "../UserListForm";
import router from "../../router";

export default {
  name: "AdminPage",
  props: {
    source: String
  },

  data: () => ({
    drawer: null,
    admin_selected: 0,
    search_text: null,

    tab: null,
    items: ["User", "Policy", "Notice", "Post"],
    search: "",
    text: "babo",
    dialog: false,
    headers: [
      [
        {
          text: "Id",
          // align: "left",
          // sortable: false,
          value: "id"
        },
        { text: "User Name", value: "username" },
        { text: "Favorite", value: "favorite" },
        { text: "Password", value: "password" },
        { text: 'Actions', value: 'action', sortable: false },
      ],
      [
        {
          text: "Id",
          // align: "left",
          // sortable: false,
          value: "id"
        },
        { text: "User Name", value: "username" },
        { text: "Favorite", value: "favorite" },
        { text: "Password", value: "password" },
        { text: 'Actions', value: 'action', sortable: false },
      ],
      [
        { text: "Id", value: "id" },
        { text: "Title", value: "title" },
        { text: "Content", value: "content" },
        { text: 'Actions', value: 'action', sortable: false },
      ],
      [
        { text: "Id", value: "id" },
        { text: "Title", value: "title" },
        { text: "Content", value: "content" },
        { text: 'Actions', value: 'action', sortable: false },
      ]
    ],
    editedIndex: -1,
    editedItem: [
      [{
        id: "",
        username: "",
        favorite : "",
        password: "",
      }],
      [{
        id: "",
        username: "",
        favorite : "",
        password: "",
      }],
      [{
        id: "",
        title: "",
        content: "",
      }],
       [{
        id: "",
        title: "",
        content: "",
      }],
    ],
    dashBoardAllData: [[], [], [], []],
    userData: [],
    noticeData: [],
    boardData: []
  }),
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Edit Item" : "Edit Item";
    }
  },
  watch: {
    group() {
      this.drawer = false;
    },
    dialog(val) {
      val || this.close();
    }
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
  mounted() {
    this.$store.state.data.userPage = false;
    this.getAllData();
  },
  methods: {
    ...mapActions("data", ["getAllUsers", "getAllNotices", "getAllBoards"]),
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    getSearchResult() {
      console.log(this.search_text);
    },
    getDash() {
      this.admin_selected = 0;
    },
    getChart() {
      this.admin_selected = 1;
    },
    getAllData() {
      this.getUsers();
      this.getNotices();
      this.getBoards();
    },
    getUsers() {
      this.getAllUsers().then(response => {
        this.dashBoardAllData[0] = response;
      });
    },
    getNotices() {
      this.getAllNotices().then(response => {
        this.dashBoardAllData[2] = response;
      });
    },
    getBoards() {
      this.getAllBoards().then(response => {
        this.dashBoardAllData[3] = response;
      });
    },
    editItem(item, idx) {
      console.log(item)
      this.editedIndex = this.dashBoardAllData[idx].indexOf(item);
      this.editedItem[idx] = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item, idx) {
      console.log(idx)
      console.log(item)
      console.log(this.dashBoardAllData[idx])
      console.log(idx)
      const index = this.dashBoardAllData[idx].indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.dashBoardAllData[idx].splice(index, 1);
      console.log(this.dashBoardAllData[idx])
      console.log(idx)
    },

    close() {
      this.dialog = false;
      // setTimeout(() => {
      //   this.editedItem = Object.assign({}, this.defaultItem);
      //   this.editedIndex = -1;
      // }, 300);
    },

    save(idx) {
      if (this.editedIndex > -1) {
        Object.assign(this.dashBoardAllData[idx][this.editedIndex], this.editedItem[idx]);
      } else {
        this.desserts.push(this.editedItem[idx]);
      }
      this.close();
    }
  },
  components: {
    UserList
  }
};
</script>

<style lang="scss" scoped>
.md-app {
  min-height: 350px;
  border: 1px solid rgba(#000, 0.12);
}

// Demo purposes only
.md-drawer {
  width: 230px;
  max-width: calc(100vw - 125px);
}
</style>