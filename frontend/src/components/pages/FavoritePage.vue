<template>
    <div>
        <v-card class="mx-auto">
      <v-toolbar color="lightgray" white>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-toolbar-title><img src="../../glass_row.png" class="header_left"></v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
      <br>
      <v-container fluid grid-list-md pa-2>
        <v-layout style="margin-left:10%;">
          <div class="favoritebox">
          <!-- <v-flex class="favoritebox" v-for="i in totalfavorite"> -->
            <div class="favoritecontents">찜 해놓은 정책
              <hr>
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
            </div>
            <div class="favoritecontents">진행중인 정책
              <hr>
              <div class="favoritecontent">
                <h4>내집마련 정책</h4>
              </div>
              <div class="favoritecontent">
                <h4>내집마련 정책</h4>
              </div>
              <div class="favoritecontent">
                <h4>내집마련 정책</h4>
              </div>
            </div>
            <div class="favoritecontents">결과나온 정책
              <hr>
              <div class="favoritecontent">
                <h4>한 부모 가정 지원</h4>
              </div>
            </div>
              <!-- <div class="favoritecontent" color="white">
                  
                  
                  {{ i }}
                <v-btn @click='openmodal(i.favorite)' style="width:80%; box-shadow:none; min-height:110px; backgroundColor:white">
                  <v-img aspect-ratio=1 :src='i.favorite.logo' contain style="width:10%; margin-left:5%; "></v-img>
                  <div style="width:80%; ">
                    {{i.favorite.name}}<br>
                    <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-if="i.favorite.end===undefined">채용시 마감</p>
                    <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-else>{{i.favorite.start}} ~ {{i.favorite.end}}
                    </p>
                  </div>
                </v-btn>
                <v-btn icon @click='delfavorite(i.favorite)'>
                  <v-icon color="red" style="width:5%;">delete</v-icon>
                </v-btn>
              </div>
            <br>
          </v-flex> -->
          </div>
        </v-layout>
      </v-container>
      <br>
    </v-card>

    </div>
</template>

<script>
// export default {
//     data : () => ({
//         totalfavorite : ['관심정책명 1', '관심정책명 2', '관심정책명 3']
//     })
// }


</script>
<style>
.header_left{
  width:17%;
}
.favoritebox{
  display: flex;
  text-align:center;
  width:33.3%;
  min-width: 100%;
  min-height: 400px;
}
.favoritecontents{
  margin: 2%;
  padding: 2%;
  border-radius: 7px;
  min-height:110px;
  width:100%;
  border: 4px solid rgb(187, 187, 187);
  text-align: center;
}
.favoritecontent{
  margin: 2%;
  padding: 1%;
  border-radius: 7px;
  width:40%;
  border: 1px solid gray;
  text-align: center;
  display: inline-flex;
}
</style>