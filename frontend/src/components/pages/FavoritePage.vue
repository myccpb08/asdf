<template>
    <div>
        <v-card class="mx-auto">
      <v-toolbar color="pink" dark>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-toolbar-title>내가 지원할 정책</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
      <br>
      <v-container fluid grid-list-md pa-2>
        <v-layout wrap style="width:80%; margin-left:10%;">
          <v-flex style="text-align:center; width:100%;" v-for="i in totalfavorite">
            <div color="white" style="min-height:110px; width:100%; border: 4px solid gray;">
                {{ i }}
              <!-- <v-btn @click='openmodal(i.favorite)' style="width:80%; box-shadow:none; min-height:110px; backgroundColor:white">
                <v-img aspect-ratio=1 :src='i.favorite.logo' contain style="width:10%; margin-left:5%; "></v-img>
                <div style="width:80%; ">
                  {{i.favorite.name}}<br>
                  <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-if="i.favorite.end===undefined">채용시 마감</p>
                  <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-else>{{i.favorite.start}} ~ {{i.favorite.end}}
                  </p>
                </div>
              </v-btn> -->
              <!-- <v-btn icon @click='delfavorite(i.favorite)'>
                <v-icon color="red" style="width:5%;">delete</v-icon>
              </v-btn> -->
            </div>
            <br>
          </v-flex>
        </v-layout>
      </v-container>
      <br>
    </v-card>

    </div>
</template>

<script>
export default {
    data : () => ({
        totalfavorite : ['관심정책명 1', '관심정책명 2', '관심정책명 3']
    })

}


</script>