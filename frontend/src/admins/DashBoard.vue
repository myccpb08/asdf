<template>
  <div>
    <apexchart width="500" 
    type="bar" 
    :options="chartOptions" 
    :series="series"></apexchart>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../router";

export default {
  name: "DashBoard",
  data: function() {
    return {
      
      chartOptions: {
        chart: {
          id: "vuechart-1"
        },
        xaxis: {
          categories: ["2019-10-26", "2019-10-27", "2019-10-28", "2019-10-29", "2019-10-30"]
        }
      },
      series: [
        {
          name: "users",
          data: [{},{},{},{},{}]
        },
        {
          name: "boards",
          data: [{},{},{},{},{}]
        }
      ],
      now: new Date(),
      boards: [],
      categories: [],
      users: [],
    };
  },
  mounted() {
    this.now = new Date();
    this.setAxis();
  },
  methods: {
    setAxis() {
      this.categories = [
      this.now.getFullYear() + '-' + (this.now.getMonth()+1) + '-' + (this.now.getDate() - 4) +'T00:00:00',
      this.now.getFullYear() + '-' + (this.now.getMonth()+1) + '-' + (this.now.getDate() - 3) +'T00:00:00',
      this.now.getFullYear() + '-' + (this.now.getMonth()+1) + '-' + (this.now.getDate() - 2) +'T00:00:00',
      this.now.getFullYear() + '-' + (this.now.getMonth()+1) + '-' + (this.now.getDate() - 1) +'T00:00:00',
      this.now.getFullYear() + '-' + (this.now.getMonth()+1) + '-' + (this.now.getDate()) +'T00:00:00',
      ];
    }
  }
};
</script>

<style>
</style>