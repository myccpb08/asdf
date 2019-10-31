<template>
  <v-app id="inspire">
    <!-- TODO: navigation drawer component로 분리 -->
    <v-navigation-drawer v-model="drawer" app>
      <v-list dense>
        <v-list-item @click="getDash" v-for="menu in menus" :key="menu.title">
          <v-list-item-action @click="move_route(menu.route)">
              <v-icon>{{ menu.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content @click="move_route(menu.route)">
              <v-list-item-title>{{ menu.title }}</v-list-item-title>
            </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app
      color="warning"
      dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="width: 200px" class="ml-0 pl-4">
        <span class="hidden-sm-and-down">DJE Admin</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <i class="fas fa-home fa-2x" @click="goHome"></i>
      </v-btn>
    </v-app-bar>

    <v-content>
        <router-view />
    </v-content>

    <v-footer color="warning" app padless max-height="35">
      <v-col class="text-center" cols="12" style="padding: 4px; font-size: 80%;">
        <span class="white--text">&copy; 2019</span>
        <strong style="color:white"> — 딱정이</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";

import UserList from "../../admins/UserList";
import router from "../../router";

export default {
  name: "AdminPage",
  props: {
    source: String
  },

  data: () => ({
    drawer: null,
    admin_selected: 0,
    menus: [
      {
        title: "DASHBOARD",
        route: "/admin",
        icon: "mdi-view-dashboard"
      },

      {
        title: "USER",
        route: "/admin/user",
        icon: "mdi-account"
      },
      {
        title: "POLICY",
        route: "/admin/policy",
        icon: "mdi-message-draw"
      },
      {
        title: "NOTICE",
        route: "/admin/notice",
        icon: "mdi-sign-text"
      },
      {
        title: "BOARD",
        route: "/admin/board",
        icon: "mdi-message-draw"
      }
    ],
    tab: null,
    items: ["User", "Policy", "Notice", "Post"],
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
        { text: "Actions", value: "action", sortable: false }
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
        { text: "Actions", value: "action", sortable: false }
      ],
      [
        { text: "Id", value: "id" },
        { text: "Title", value: "title" },
        { text: "Content", value: "content" },
        { text: "Actions", value: "action", sortable: false }
      ],
      [
        { text: "Id", value: "id" },
        { text: "Title", value: "title" },
        { text: "Content", value: "content" },
        { text: "Actions", value: "action", sortable: false }
      ]
    ],
    editedIndex: -1,
    editedItem: [
      [
        {
          id: "",
          username: "",
          favorite: "",
          password: ""
        }
      ],
      [
        {
          id: "",
          username: "",
          favorite: "",
          password: ""
        }
      ],
      [
        {
          id: "",
          title: "",
          content: ""
        }
      ],
      [
        {
          id: "",
          title: "",
          content: ""
        }
      ]
    ],
    dashBoardAllData: [[], [], [], []],
    userData: [],
    noticeData: [],
    boardData: []
  }),
  computed: {
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
    // this.$vuetify.theme.dark = true;
  },
  mounted() {
    this.$store.state.data.userPage = false;
    // this.getAllData();
  },
  methods: {
    ...mapActions("data", ["getAllUsers", "getAllNotices", "getAllBoards"]),
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    goHome() {
      location.replace('http://localhost:8080/')
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
      console.log(item);
      this.editedIndex = this.dashBoardAllData[idx].indexOf(item);
      this.editedItem[idx] = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item, idx) {
      const index = this.dashBoardAllData[idx].indexOf(item);
      // confirm("Are you sure you want to delete this item?") &&
      this.dashBoardAllData[idx].splice(index, 1);
    },

    close() {
      this.dialog = false;
    },

    save(idx) {
      if (this.editedIndex > -1) {
        Object.assign(
          this.dashBoardAllData[idx][this.editedIndex],
          this.editedItem[idx]
        );
      } else {
        this.desserts.push(this.editedItem[idx]);
      }
      this.close();
    },
    move_route(link){
      console.log(link)
      this.$router.push(link)
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
.admin-footer {
  text-align: center;
}
</style>