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
          data: [28, 29, 33, 36, 32]
        },
        {
          name: "board",
          data: [12, 11, 14, 18, 17]
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
        colors: ["#77B6EA", "#545454"],
        dataLabels: {
          enabled: true
        },
        stroke: {
          curve: "smooth"
        },
        title: {
          text: "Average High & Low Temperature",
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
            text: "Month"
          }
        },
        yaxis: {
          title: {
            text: "Temperature"
          },
          min: 5,
          max: 40
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
        ]
      },
      // 정책 가로 막대 차트
      seriesPolicy: [
        {
          data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
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
            "France",
            "Japan",
            "United States",
            "China",
            "Germany"
          ]
        },
      },
      // 최근 회원 가입수
      seriesUser: [
        {
          name: "Desktops",
          data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
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
          text: "Product Trends by Month",
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
            "Aug",
            "Sep"
          ]
        }
      },
      now: new Date(),
      categories: [],
      notices: [],
      boards: [],
      users: []
    };
  },
  mounted() {
    this.setAxis();
    // this.plot();
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
            text: "Month"
          }
        }
      };
      console.log(this.chartPostOptions.xaxis.categories);
    },
    async getNotices() {
      await this.getAllNotices().then(response => {
        this.notices = response;
        console.log("notice");
        console.log(this.notices);
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
    async setPostChart() {
      let len = this.notices.length;
      if (this.notices.length >= 5) {
        len = 5;
      }
      for (let i = 0; i < len; i++) {
        this.seriesPost[0].data[i] = i;
      }
      console.log(this.series[0].data);
      for (let i = 0; i < len; i++) {
        this.seriesPost[1].data[i] = i;
      }
    },
    async plot() {
      await this.getNotices();
      await this.setPostChart();
    }
  }
};
</script>

