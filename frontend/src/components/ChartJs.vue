<template>
  <div class="chart-canva">
    <h3 v-if="title != 'null'">{{ title }}</h3>
    <div class="chart">
      <canvas class="chart" ref="chart"></canvas>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

export default {
  props: {
    data: Object,
    title: String,
    width: Number,
    height: Number,
  },
  data() {
    return {
      chartHeight: this.height + "vh",
      chartWidth: this.width + "vw",
    };
  },
  methods: {
    renderChart() {
      const ctx = this.$refs.chart.getContext("2d");
      new Chart(ctx, this.data);
    },
  },
  mounted() {
    this.renderChart();
  },
  updated() {
    this.renderChart();
  },
};
</script>

<style scoped>
.chart {
  height: v-bind(chartHeight);
  width: v-bind(chartWidth);
  margin: 1rem 1rem 1rem 1rem;
}

h3 {
  padding-top: 2vh;
}
</style>
