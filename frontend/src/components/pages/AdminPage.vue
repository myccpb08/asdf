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
        <p>{{ test }}</p>
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
                <!-- 데이터 테이블 -->
                <v-card>
                  <v-card-title>
                    {{ title[tab] }}
                    <v-spacer></v-spacer>
                    <v-text-field
                      v-model="search"
                      append-icon="mdi-magnify"
                      label="Search"
                      single-line
                      hide-details
                      v-on:keyup.enter="getSearchList"
                      @click:append="getSearchList"
                    ></v-text-field>
                  </v-card-title>
                  <v-data-table :headers="headers" :items="desserts" :search="search"></v-data-table>
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
    tab: null,
    items: ["User", "Policy", "Notice", "Post"],
    search_text: null,
    dash_datas: [],
    test: [],
    title: ["User", "Policy", "Notice", "Post"],
    search: "",
    headers: [
      {
        text: "Dessert (100g serving)",
        align: "left",
        sortable: false,
        value: "name"
      },
      { text: "Calories", value: "calories" },
      { text: "Fat (g)", value: "fat" },
      { text: "Carbs (g)", value: "carbs" },
      { text: "Protein (g)", value: "protein" },
      { text: "Iron (%)", value: "iron" }
    ],
    desserts: [
      {
        name: "Frozen Yogurt",
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
        iron: "1%"
      },
      {
        name: "Ice cream sandwich",
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
        iron: "1%"
      },
      {
        name: "Eclair",
        calories: 262,
        fat: 16.0,
        carbs: 23,
        protein: 6.0,
        iron: "7%"
      },
      {
        name: "Cupcake",
        calories: 305,
        fat: 3.7,
        carbs: 67,
        protein: 4.3,
        iron: "8%"
      },
      {
        name: "Gingerbread",
        calories: 356,
        fat: 16.0,
        carbs: 49,
        protein: 3.9,
        iron: "16%"
      },
      {
        name: "Jelly bean",
        calories: 375,
        fat: 0.0,
        carbs: 94,
        protein: 0.0,
        iron: "0%"
      },
      {
        name: "Lollipop",
        calories: 392,
        fat: 0.2,
        carbs: 98,
        protein: 0,
        iron: "2%"
      },
      {
        name: "Honeycomb",
        calories: 408,
        fat: 3.2,
        carbs: 87,
        protein: 6.5,
        iron: "45%"
      },
      {
        name: "Donut",
        calories: 452,
        fat: 25.0,
        carbs: 51,
        protein: 4.9,
        iron: "22%"
      },
      {
        name: "KitKat",
        calories: 518,
        fat: 26.0,
        carbs: 65,
        protein: 7,
        iron: "6%"
      }
    ]
  }),
  computed: {
    // 계산된 getter
  },
  watch: {
    group() {
      this.drawer = false;
    }
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
  mounted() {
    this.$store.state.data.userPage = false;
    this.getTest();
  },
  methods: {
    ...mapActions("data", ["getAllUsers"]),
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    getSearchResult() {
      console.log(this.search_text);
    },
    getSearchList() {
      console.log(this.search);
    },
    getDash() {
      this.admin_selected = 0;
      console.log(this.admin_selected);
    },
    getChart() {
      this.admin_selected = 1;
      console.log(this.admin_selected);
    },
    getTest() {
      for (var i = 0; i < 4; i++) {
        this.test.push(i)
        console.log(this.test)
      }
    },
    async getUserList() {
      
    },
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