<template>
  <v-container fluid>
    <v-layout row>
      <v-flex xs12 md6>
       <apexchart height="350" type="line" :options="chartPostOptions" :series="seriesPost"></apexchart>
      </v-flex>
      <v-flex xs12 md6>
       <apexchart
          type="donut"
          height="350"
          :options="chartFavoriteOptions"
          :series="seriesFavorite"
        />
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12 md6>
       <apexchart type="bar" height="350" :options="chartPolicyOptions" :series="seriesPolicy" />
      </v-flex>
      <v-flex xs12 md6>
       <apexchart type="line" height="350" :options="chartUserOptions" :series="seriesUser" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../router";
import store from "../store/modules/data.js";

export default {
  name: "DashBoard",
  data: function() {
    return {
      // 공지사항, 자유게시판 차트
      seriesPost: [
        {
          name: "notice",
          data: [2,0,0,2,1]
        },
        {
          name: "board",
          data: [5,8,9,13,3]
        },
        {
          name: "policy",
          data: [0, 0, 0, 0, 0]
        }
      ],
      chartPostOptions: {
        chart: {
          shadow: {
            enabled: false,
            color: "#000",
            top: 18,
            left: 7,
            blur: 10,
            opacity: 1
          },
          toolbar: {
            show: false
          }
        },
        colors: ["#77B6EA", "#545454", "#FF7F50"],
        dataLabels: {
          enabled: true
        },
        stroke: {
          curve: "smooth"
        },
        title: {
          text: "일별 작성된 게시글 수",
          align: "left"
        },
        grid: {
          borderColor: "#e7e7e7",
          row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5
          }
        },
        markers: {
          size: 5
        },
        xaxis: {
          categories: ["Jan", "Feb", "Mar", "Apr", "May"],
          title: {
            text: "date"
          }
        },
        yaxis: {
          title: {
            text: "작성 수"
          },
          min: 0,
          max: 20
        },
        legend: {
          position: "top",
          horizontalAlign: "right",
          floating: true,
          offsetY: -25,
          offsetX: -5
        }
      },
      // User Favorite 도넛 차트
      seriesFavorite: [
        44,
        55,
        13,
        43,
        22,
        44,
        55,
        13,
        43,
        22,
        44,
        55,
        13,
        43,
        22,
        1
      ],
      chartFavoriteOptions: {
        labels: [
          "임신/출산",
          "영유아",
          "아동/청소년",
          "청년",
          "중장년",
          "노년",
          "장애인",
          "한부모",
          "다문화(새터민)",
          "저소득층",
          "교육",
          "고용",
          "주거",
          "건강",
          "서민금융",
          "문화"
        ],
        colors: [
          "#003366",
          "#33cccc",
          "#3333ff",
          "#9933ff",
          "#cc66ff",
          "#ff99cc",
          "#ff0066",
          "#ff6600",
          "#993333",
          "#cc6699",
          "#66ff66",
          "#ffcc66",
          "#77B6EA",
          "#00cc00",
          "#996633",
          "#00ffcc"
        ],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 350
              },
              legend: {
                position: "bottom"
              }
            }
          }
        ],
        title: {
          text: "유저들의 선호 복지정책 선택 수",
          align: "left"
        },
      },
      // 정책 가로 막대 차트
      seriesPolicy: [
        {
          data: [40, 22, 10, 5, 3]
        }
      ],
      
      chartPolicyOptions: {
        plotOptions: {
          bar: {
            horizontal: true
          }
        },
        dataLabels: {
          enabled: false
        },
        xaxis: {
          categories: [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
          ]
        },
        title: {
          text: "가장 많이 본 정책",
          align: "left"
        },
      },
      // 최근 회원 가입수
      seriesUser: [
        {
          name: "Signup",
          data: [0, 0, 0, 5, 13]
        }
      ],
      chartUserOptions: {
        chart: {
          height: 350,
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: "straight"
        },
        title: {
          text: "최근 회원가입 수",
          align: "left"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5
          }
        },
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
          ]
        }
      },
      now: new Date(),
      categories: [],
      notices: [],
      boards: [],
      users: [],
      policies: [],
    };
  },
  created() {
  },
  mounted() {
    this.setAxis();    
    this.draw();
  },
  methods: {
    ...mapActions("data", ["getAllUsers", "getAllNotices", "getAllBoards"]),
    setAxis() {
      this.chartPostOptions = {
        xaxis: {
          categories: [
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 4),
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 3),
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 2),
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 1),
            this.now.getMonth() + 1 + "-" + this.now.getDate()
          ],
          title: {
            text: "date"
          }
        }
      };
      this.chartUserOptions = {
        xaxis: {
          categories: [
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 4),
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 3),
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 2),
            this.now.getMonth() + 1 + "-" + (this.now.getDate() - 1),
            this.now.getMonth() + 1 + "-" + this.now.getDate()
          ]
        }
      }
      console.log(this.chartPostOptions.xaxis.categories);
    },
    async draw() {
      await this.getNotices()
      await this.getBoards()
      await this.getUsers()
      await this.getPolicies()
      await this.setPostChart()    
    },
    async getNotices() {
      await this.getAllNotices().then(response => {
        this.notices = response
        return;
      });
    },
    async getBoards() {
      await this.getAllBoards().then(response => {
        this.boards = response;
      });
    },
    async getUsers() {
      await this.getAllUsers().then(response => {
        this.users = response;
      });
    },
    async getPolicies() {
      await this.$store.dispatch("data/policySearch", '00').then(response => {
        this.policies = response
        // console.log(this.policies)
      });
    },
    async setPostChart() {
        let notice_cnt = [0, 0, 0, 0, 0]
        let board_cnt = [0, 0, 0, 0, 0]
        for(let i=4; i >= 0; i--){
          let yyyy = this.now.getFullYear().toString();
          let mm = (this.now.getMonth() + 1).toString();
          let dd = (this.now.getDate() - i).toString();
          const date = yyyy + "-" + (mm[1] ? mm : "0" + mm[0]) + "-" + (dd[1] ? dd : "0" + dd[0]);
          
          for(let j=0; j < this.notices.length; j++){
            if (date == this.notices[j].when){
              notice_cnt[4-i] += 1  
            }
          }
          for(let j=0; j < this.boards.length; j++){
            if (date == this.boards[j].when){
              board_cnt[4-i] += 1  
            }
          }
        }
      this.seriesPost[0].data = notice_cnt
      this.seriesPost[1].data = board_cnt

      // 유저 선호 정책 수
      let favorite_cnt = [0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,]

      for(let i=0;i < this.users.length; i++){
        let Favorite = this.users[i].favorite
        for(let j =0; j <Favorite.length; j++){
            let f = Favorite[j]
            if (f=='00') continue;
            else if (f=='01'){favorite_cnt[0] += 1} 
            else if (f=='02'){favorite_cnt[1] += 1}
            else if (f=='03'){favorite_cnt[2] += 1}
            else if (f=='04'){favorite_cnt[3] += 1}
            else if (f=='05'){favorite_cnt[4] += 1}
            else if (f=='06'){favorite_cnt[5] += 1}
            else if (f=='07'){favorite_cnt[6] += 1}
            else if (f=='08'){favorite_cnt[7] += 1}
            else if (f=='09'){favorite_cnt[8] += 1}
            else if (f=='10'){favorite_cnt[9] += 1}
            else if (f=='11'){favorite_cnt[10] += 1}
            else if (f=='12'){favorite_cnt[11] += 1}
            else if (f=='13'){favorite_cnt[12] += 1}
            else if (f=='14'){favorite_cnt[13] += 1}
            else if (f=='15'){favorite_cnt[14] += 1}
            else if (f=='16'){favorite_cnt[15] += 1}
            else continue
        }
      }
      this.seriesFavorite = favorite_cnt

      // 조회수 높은 정책 5개
      let views = [0, 0, 0, 0, 0]
      this.$store.dispatch("data/getMostPolicy").then(response => {
        for(let i =0 ; i <response.length; i++){
          console.log(response[i].clicked)
          this.seriesPolicy[0].data[i] = response[i].clicked;
          this.chartPolicyOptions.xaxis.categories[i] = response[i].title;
        }
      })

      // 최근 가입한 유저 수
      let user_cnt = [0, 0, 0, 0, 0]
      for(let i=4; i >= 0; i--){
          let yyyy = this.now.getFullYear().toString();
          let mm = (this.now.getMonth() + 1).toString();
          let dd = (this.now.getDate() - i).toString();
          const date = yyyy + "-" + (mm[1] ? mm : "0" + mm[0]) + "-" + (dd[1] ? dd : "0" + dd[0]);
          
          for(let j=0; j < this.users.length; j++){
            if (date == this.users[j].when){
              user_cnt[4-i] += 1  
            }
          }
        }
      this.seriesUser[0].data = user_cnt
      

    },
    async plot() {
      await this.getNotices();
      await this.setPostChart();
    }
  }
};
</script>

